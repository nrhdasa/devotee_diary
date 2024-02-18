import json
import frappe
from frappe.exceptions import DuplicateEntryError

@frappe.whitelist()
def create_new_sadhana_entry():
    entry = json.loads(frappe.form_dict.data)
    frappe.errprint(entry)
    if not entry.get('devotee'):
        frappe.throw("Please select the devotee.")
    
    entry_doc = frappe.get_doc({
        'doctype': 'Sadhana Entry',
        'date':entry.get('date'),
        'devotee':entry.get('devotee'),
        'parameters':format_parameters(entry.get('parameters'))
    })
    try:
        entry_doc.save(ignore_permissions=True)
    except DuplicateEntryError as exc:
        frappe.throw("Already Sadhana filled for this Date.")
    except:
        raise
    # entry_json = {
    #     "devotee"
    # }
    # # entry_doc = frappe.get_doc("Sadhana Entry", )
    # donor_doc.pan_no = donation["donor"]["pan_no"]
    # donor_doc.aadhar_no = donation["donor"]["aadhar_no"]
    # donor_doc.save(ignore_permissions=True)

def format_parameters(parameters:list):
    parameters = [ frappe._dict(
        parameter = p['name'],
        grade = p['selectedValue'],
        authorised_service = p['authorised_service'],
        sick = p['sick']
    )  for p in parameters ]
    return parameters

@frappe.whitelist()
def get_default_devotee(user:str = None):
    if not user:
        user = frappe.session.user
    entry = frappe.db.sql(f"""
                    select devotee.name
                    from `tabDED Devotee` devotee
                    join `tabDED Devotee User` duser
                    on duser.parent = devotee.name
                    where duser.user = '{user}'
                    """,)
    if entry:
        return entry[0][0]
    return None
@frappe.whitelist()
def get_sadhana_entries(devotee, start_date, end_date):
    entries = []
    for entry in frappe.get_all("Sadhana Entry",filters={'devotee':devotee,'date':['between',[start_date,end_date]]}, pluck='name'):
        entry_doc = frappe.get_doc("Sadhana Entry",entry)
        entries.append(entry_doc.as_dict())
    return entries

