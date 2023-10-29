# Copyright (c) 2023, Narahari Dasa and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils.data import cint, getdate


class SadhanaEntry(Document):
    def autoname(self):
        dateF = getdate(self.date)
        dateStr = dateF.strftime("%y-%m-%d")
        self.name = f"{self.devotee}-{dateStr}"

    def validate(self):
        self.validate_grades()
        self.validate_duplicates()

    def validate_grades(self):
        for p in self.parameters:
            frappe.errprint(p.grade)
            if p.grade:
                points = frappe.get_value(
                "Sadhana Parameter Detail",
                filters=[["parent", "=", p.parameter], ["grade", "=", p.grade]],
                fieldname="points",
                )
                frappe.errprint("Points")
                frappe.errprint(points)
                frappe.errprint(p.parameter)
                frappe.errprint(p.grade)
                if points is None:
                    frappe.throw(f"Points for Grade <b>{p.grade}</b> is not SET in Sadhana Parameter <b>{p.parameter}</b>.")
                p.points = points
            elif not(p.authorised_service or p.sick):
                    frappe.throw(f"Grade is mandatory in case of no <b>AS or SICK</b>")
        return

    def validate_duplicates(self):
        documents = []
        for d in self.get("parameters"):
            if d.parameter in documents:
                frappe.throw("Row#{0} Duplicate record not allowed for {1}".format(d.idx, d.parameter))
            documents.append(d.parameter)
        return
