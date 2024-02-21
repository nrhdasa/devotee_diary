import json
import frappe
from frappe.exceptions import DuplicateEntryError

@frappe.whitelist()
def create_new_sadhana_entry():
    entry = json.loads(frappe.form_dict.data)
    if not entry.get('devotee'):
        frappe.throw("Please select the devotee.")
    
    entry_doc = frappe.get_doc({
        'doctype': 'Sadhana Entry',
        'entry_date':entry.get('date'),
        'devotee':entry.get('devotee'),
        'parameters':format_parameters(entry.get('parameters'))
    })
    try:
        entry_doc.save(ignore_permissions=True)
    except DuplicateEntryError as exc:
        frappe.throw("Already Sadhana filled for this Date.")
    except:
        raise

def format_parameters(parameters:list):
    parameters = [ frappe._dict(
        parameter = p['name'],
        grade = p['selectedValue'],
        authorised_service = p['authorised_service'],
        sick = p['sick']
    )  for p in parameters ]
    return parameters

@frappe.whitelist()
def get_devotee_from_user(user=None):
    if not user:
        user = frappe.session.user
    try:
        doc = frappe.get_doc("DED Devotee",{"erp_user":user})
        return doc.name
    except:
        return None
    
@frappe.whitelist()
def get_sadhana_entries(devotee, start_date, end_date):
    entries = []
    for entry in frappe.get_all("Sadhana Entry",filters={'devotee':devotee,'entry_date':['between',[start_date,end_date]]}, pluck='name'):
        entry_doc = frappe.get_doc("Sadhana Entry",entry)
        entries.append(entry_doc.as_dict())
    return entries

