import json
import frappe

@frappe.whitelist()
def create_new_sadhana_entry():
    entry = json.loads(frappe.form_dict.data)
    frappe.errprint(entry)
    entry_doc =  frappe.new_doc('Sadhana Entry')
    entry_doc.date = entry.get('date')
    entry_doc.devotee = entry.get('devotee')
    entry_doc.parameters = format_parameters(entry.get('parameters'))
    frappe.errprint(entry_doc.parameters)
    entry_doc.insert(ignore_permissions=True)
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