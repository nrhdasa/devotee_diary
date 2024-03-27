import frappe
from datetime import datetime, timedelta


def sadhana_reminder_1():
    sadhana_reminder(hour=15)


def sadhana_reminder_2():
    sadhana_reminder(hour=20)


def sadhana_reminder(hour):
    yesterday = datetime.now() - timedelta(days=1)

    devotees_done = frappe.get_all(
        "Sadhana Entry", filters={"entry_date": yesterday}, pluck="devotee"
    )

    mobile_app = frappe.db.get_single_value("Sadhana Settings", "firebase_admin_app")

    message = ""
    if hour == 15:
        message = "You have not filled Sadhana for Yesterday. Please do."
    else:
        message = "Please fill Sadhana for Yesterday. It will be locked in few hours."

    for erp_user in frappe.get_all(
        "DED Devotee",
        filters=[["erp_user", "is", "set"], ["name", "not in", devotees_done]],
        pluck="erp_user",
    ):
        frappe.get_doc(
            {
                "doctype": "App Notification",
                "app": mobile_app,
                "user": erp_user,
                "subject": "Sadhana Reminder",
                "message": message,
            }
        ).insert()
    frappe.db.commit()
