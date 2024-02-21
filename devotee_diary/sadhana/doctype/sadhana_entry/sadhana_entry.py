# Copyright (c) 2023, Narahari Dasa and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils.data import getdate
from datetime import date, timedelta

class SadhanaEntry(Document):
    def autoname(self):
        
        dateF = getdate(self.entry_date)
        dateStr = dateF.strftime("%y-%m-%d")
        self.name = f"{self.devotee}-{dateStr}"

    def validate(self):
        self.validate_grades()
        self.validate_duplicates()
        self.validate_threshold_days()
        self.validate_future_date()
        return
    def on_trash(self):
        self.validate_threshold_days()
        return

    def validate_threshold_days(self):
        settings = frappe.get_single("Sadhana Settings")
        if settings.admin_role in frappe.get_roles(frappe.session.user):
            return
        
        today = date.today()
        threshold_date = today - timedelta(days=settings.sadhana_threshold_days)
        
        if getdate(self.entry_date) < threshold_date:
            frappe.throw(f"Action on this date not allowed. Threshold Days : {settings.sadhana_threshold_days}")
        return

    def validate_future_date(self):
        today = date.today()
        if getdate(self.entry_date) > today:
            frappe.throw(f"Not allowed this action for future dates.")
        return

    def validate_grades(self):
        for p in self.parameters:
            if p.grade:
                points = frappe.get_value(
                "Sadhana Parameter Detail",
                filters=[["parent", "=", p.parameter], ["grade", "=", p.grade]],
                fieldname="points",
                )
                if points is None:
                    frappe.throw(f"Points for Grade <b>{p.grade}</b> is not SET in Sadhana Parameter <b>{p.parameter}</b>.")
                p.points = points
            elif not(p.authorised_service or p.sick):
                    frappe.throw(f"{p.parameter}: Grade is mandatory in case of no <b>AS or SICK</b>")
        return

    def validate_duplicates(self):
        documents = []
        for d in self.get("parameters"):
            if d.parameter in documents:
                frappe.throw("Row#{0} Duplicate record not allowed for {1}".format(d.idx, d.parameter))
            documents.append(d.parameter)
        return
