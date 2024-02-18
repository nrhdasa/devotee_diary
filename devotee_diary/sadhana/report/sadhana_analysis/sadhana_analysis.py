# Copyright (c) 2024, Narahari Dasa and contributors
# For license information, please see license.txt


from datetime import datetime
import frappe
from frappe import _

def execute(filters=None):
	if not filters: filters = {}

	filters.update({"from_date": filters.get("date_range") and filters.get("date_range")[0], "to_date": filters.get("date_range") and filters.get("date_range")[1]})
	columns = get_columns(filters)
	parameters = frappe.get_all("Sadhana Parameter",filters = {"active":1}, pluck="name")
	devotee_data = {}
	for entry in frappe.db.sql(f"""
			select date,devotee,tsd.parameter,tsd.points,tsd.authorised_service,tsd.sick
			from `tabSadhana Entry` ts
			join `tabSadhana Entry Detail` tsd
			on ts.name = tsd.parent
			where date between '{filters.get('from_date')}' and '{filters.get('to_date')}'
				""",as_dict=1):
		if entry['devotee'] not in devotee_data:
			devotee_data.setdefault(entry['devotee'],{"devotee":entry['devotee'],"total":0})
			devotee_data[entry['devotee']].update({ p:0 for p in parameters})
		if entry['authorised_service'] or entry['sick']:
			devotee_data[entry['devotee']][entry['parameter']] += 1.0
		else:
			devotee_data[entry['devotee']][entry['parameter']] += entry['points']
	from_date = datetime.strptime(filters.get('from_date'), '%Y-%m-%d')
	to_date = datetime.strptime(filters.get('to_date'), '%Y-%m-%d')
	total_days = (to_date - from_date).days + 1
	data = list(devotee_data.values())

	for d in data:
		for p in parameters:
			if d[p] > total_days:
				d[p] = total_days
			d['total'] += d[p]
	data = sorted(data, key=lambda x: x['devotee'])
	# columns, data = [], []
	return columns, data

def get_columns(filters):
	columns = [
		{"label": "Devotee","fieldname": "devotee","fieldtype": "Data","width": 120,},
	]
	for p in frappe.get_all("Sadhana Parameter",filters = {"active":1}, pluck="name"):
		columns.append(
			{"label": p,"fieldname": p,"fieldtype": "Float","width": 120,},
		)
	columns.append({"label": "Total","fieldname": "total","fieldtype": "Float","width": 120,},)
	return columns