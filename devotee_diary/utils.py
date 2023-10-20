import frappe
from frappe.utils.nestedset import get_descendants_of


@frappe.whitelist()
def get_devotees(detailed=0):
    final_list = []
    devotees = set()
    for i in frappe.db.sql(
        f"""
                    select d.name
                    from `tabDED Devotee` d
                    join `tabDED Devotee User` du
                    on d.name = du.parent
                    where du.user = '{frappe.session.user}'
                    group by d.name
                    """,
        as_dict=1,
    ):
        devotee_descendents = get_descendants_of("DED Devotee", i["name"], ignore_permissions=True)
        final_list.append(i["name"])
        devotees.update(set(devotee_descendents))
    final_list.extend(list(devotees))
    if detailed:
        return frappe.get_all(
            "DED Devotee",
            filters=[["name", "in", final_list]],
            fields=["name", "full_name", "is_group", "parent_ded_devotee"],
        )
    else:
        return final_list


# ## This returns the Users, the preacher is assigned to.
# @frappe.whitelist()
# def get_preacher_users(preacher):
#     ## PRCH_REMAP
#     users = []

#     for i in frappe.db.sql(
#         f"""
#                     select pu.user
#                     from `tabLLP Preacher` p
#                     join `tabLLP Preacher User` pu
#                     on p.name = pu.parent
#                     where p.name = '{preacher}'
#                     group by pu.user
#                     """,
#         as_dict=1,
#     ):
#         users.append(i["user"])
#     return users
