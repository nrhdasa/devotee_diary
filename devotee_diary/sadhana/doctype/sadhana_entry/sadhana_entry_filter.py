import frappe
from devotee_diary.utils import get_devotees

from devotee_diary.constants import DED_EXCLUDE_ROLES


def list(user):
    if not user:
        user = frappe.session.user

    user_roles = frappe.get_roles(user)

    full_access = any(role in DED_EXCLUDE_ROLES for role in user_roles)

    if full_access:
        return "( 1 )"

    devotees = get_devotees()

    if len(devotees) == 0:
        return "( 0 )"
    else:
        devotees_str = ",".join([f"'{d}'" for d in devotees])
        return f" ( `devotee` in ( {devotees_str} ) ) "


def single(doc, user=None, permission_type=None):
    if not user:
        user = frappe.session.user

    user_roles = frappe.get_roles(user)

    full_access = any(role in DED_EXCLUDE_ROLES for role in user_roles)

    if full_access or doc.devotee in get_devotees():
        return True

    return False
