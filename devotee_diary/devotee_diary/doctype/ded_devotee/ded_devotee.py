# Copyright (c) 2023, Narahari Dasa and contributors
# For license information, please see license.txt

import frappe
from frappe.utils.nestedset import NestedSet


class DEDDevotee(NestedSet):
    def validate(self):
        self.validate_duplicate_users()

    def validate_duplicate_users(self):
        documents = []
        for au in self.get("allowed_users"):
            if au.user in documents:
                frappe.throw("Row#{0} Duplicate record not allowed for {1}".format(au.idx, au.user))
            # if d.qty == 0:
            #     frappe.throw("Row#{0} contains zero quantity".format(d.idx))
            documents.append(au.user)
