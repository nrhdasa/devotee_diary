# Copyright (c) 2023, Narahari Dasa and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.utils.nestedset import NestedSet


class DEDDevotee(NestedSet):
    def validate(self):
        self.validate_duplicate_users()
        self.validate_primary()
        return

    def validate_duplicate_users(self):
        documents = []
        for au in self.get("allowed_users"):
            if au.user in documents:
                frappe.throw(
                    "Row#{0} Duplicate record not allowed for {1}".format(
                        au.idx, au.user
                    )
                )
            # if d.qty == 0:
            #     frappe.throw("Row#{0} contains zero quantity".format(d.idx))
            documents.append(au.user)

    def validate_primary(self):
        for au in self.get("allowed_users"):
            res = frappe.db.sql(
                """select dd.name
				from
					`tabDED Devotee User` ddu, `tabDED Devotee` dd
				where
					dd.name = ddu.parent and ddu.user = %s and dd.name != %s
					and ddu.primary=1""",
                (au.user, self.name),
            )

            if au.primary and res:
                frappe.msgprint(
                    _(
                        "Already set primary in Devoteee {0} for user {1}, kindly disabled primary"
                    ).format(res[0][0], au.user),
                    raise_exception=1,
                )
            elif not au.primary and not res:
                frappe.msgprint(
                    _(
                        "User {0} doesn't have any primary Devotee. Check Primary at Row {1} for this User."
                    ).format(au.user, au.idx)
                )
