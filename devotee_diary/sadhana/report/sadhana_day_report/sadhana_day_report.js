// Copyright (c) 2024, Narahari Dasa and contributors
// For license information, please see license.txt

frappe.query_reports["Sadhana Day Report"] = {
	"filters": [
		{
			"fieldname": "date_range",
			"label": __("Date Range"),
			"fieldtype": "DateRange",
			"default": [frappe.datetime.add_months(frappe.datetime.get_today(), -1), frappe.datetime.get_today()],
			"reqd": 1
		},
	]
};
