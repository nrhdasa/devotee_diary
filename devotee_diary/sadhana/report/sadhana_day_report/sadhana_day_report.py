# Copyright (c) 2024, Narahari Dasa and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    if not filters:
        filters = {}

    filters.update(
        {
            "from_date": filters.get("date_range") and filters.get("date_range")[0],
            "to_date": filters.get("date_range") and filters.get("date_range")[1],
        }
    )

    columns = get_columns()
    data = {}
    for entry in frappe.db.sql(
        f"""
			select entry_date,devotee,tsd.parameter,tsd.grade,tsd.authorised_service,tsd.sick
			from `tabSadhana Entry` ts
			join `tabSadhana Entry Detail` tsd
			on ts.name = tsd.parent
			where entry_date between '{filters.get('from_date')}' and '{filters.get('to_date')}'
				""",
        as_dict=1,
    ):
        if entry["entry_date"] not in data:
            data.setdefault(entry["entry_date"], {})
        if entry["devotee"] not in data[entry["entry_date"]]:
            data[entry["entry_date"]].setdefault(
                entry["devotee"], {"devotee": entry["devotee"]}
            )
        temp_value = ""
        if entry["grade"]:
            temp_value = entry["grade"]
        elif entry["authorised_service"]:
            temp_value = "AS"
        elif entry["sick"]:
            temp_value = "SICK"
        data[entry["entry_date"]][entry["devotee"]][entry["parameter"]] = temp_value
    final_data = []
    for entry_date, devotees in data.items():
        final_data.append({"devotee": f"<b>{entry_date}</b>"})
        for v in devotees.values():
            final_data.append(v)
        final_data.append({})
    return columns, final_data


def get_columns():
    columns = [
        {
            "label": "Devotee",
            "fieldname": "devotee",
            "fieldtype": "Data",
            "width": 120,
        },
    ]
    for p in frappe.get_all("Sadhana Parameter", filters={"active": 1}, pluck="name"):
        columns.append(
            {
                "label": p,
                "fieldname": p,
                "fieldtype": "Data",
                "width": 120,
            },
        )
    return columns
