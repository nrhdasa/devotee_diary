import frappe
from frappe.exceptions import DoesNotExistError
from frappe.utils.nestedset import get_descendants_of


@frappe.whitelist()
def get_devotees(user = None,detailed=0):
    if not user:
        user = frappe.session.user
    try:
        devotee = frappe.get_doc("DED Devotee",{"erp_user":user})
        devotee_descendents = get_descendants_of("DED Devotee", devotee.name, ignore_permissions=True)
        print(devotee_descendents)
        final_list = [devotee.name] + devotee_descendents
        if detailed:
            detailed_list = frappe.get_all(
                "DED Devotee",
                filters=[["name", "in", final_list]],
                fields=["name", "full_name", "is_group", "parent_ded_devotee"],
            )
            ## Remove parent from top devotee
            for d in detailed_list:
                if d['name'] == devotee.name and d['parent_ded_devotee']:
                    d['parent_ded_devotee'] = None
            return detailed_list
        else:
            return final_list
    except DoesNotExistError as e:
        return []