import frappe


@frappe.whitelist()
def get_parameters():
    parameters = []
    detail = frappe.qb.DocType("Sadhana Parameter Detail")
    for parameter in frappe.get_all("Sadhana Parameter", fields=["*"], order_by = "priority"):
        details = (
            frappe.qb.from_(detail)
            .select("grade")
            .orderby("grade")
            .where(detail.parent == parameter["name"])
            .run(as_dict=1)
        )
        details = [d["grade"] for d in details]
        parameter.update(options=details)
        parameters.append(parameter)
    return parameters
