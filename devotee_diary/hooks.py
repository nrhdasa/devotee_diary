from . import __version__ as app_version

app_name = "devotee_diary"
app_title = "Devotee Diary"
app_publisher = "Narahari Dasa"
app_description = "Maintains all round information of a Temple Devotee"
app_email = "nrhdasa@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/devotee_diary/css/devotee_diary.css"
# app_include_js = "/assets/devotee_diary/js/devotee_diary.js"

# include js, css files in header of web template
# web_include_css = "/assets/devotee_diary/css/devotee_diary.css"
# web_include_js = "/assets/devotee_diary/js/devotee_diary.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "devotee_diary/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "devotee_diary.utils.jinja_methods",
# 	"filters": "devotee_diary.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "devotee_diary.install.before_install"
# after_install = "devotee_diary.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "devotee_diary.uninstall.before_uninstall"
# after_uninstall = "devotee_diary.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "devotee_diary.utils.before_app_install"
# after_app_install = "devotee_diary.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "devotee_diary.utils.before_app_uninstall"
# after_app_uninstall = "devotee_diary.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "devotee_diary.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

permission_query_conditions = {
    "Sadhana Entry": "devotee_diary.sadhana.doctype.sadhana_entry.sadhana_entry_filter.list",
}

has_permission = {
    "Sadhana Entry": "devotee_diary.sadhana.doctype.sadhana_entry.sadhana_entry_filter.single",
}

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"devotee_diary.tasks.all"
# 	],
# 	"daily": [
# 		"devotee_diary.tasks.daily"
# 	],
# 	"hourly": [
# 		"devotee_diary.tasks.hourly"
# 	],
# 	"weekly": [
# 		"devotee_diary.tasks.weekly"
# 	],
# 	"monthly": [
# 		"devotee_diary.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "devotee_diary.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "devotee_diary.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "devotee_diary.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["devotee_diary.utils.before_request"]
# after_request = ["devotee_diary.utils.after_request"]

# Job Events
# ----------
# before_job = ["devotee_diary.utils.before_job"]
# after_job = ["devotee_diary.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"devotee_diary.auth.validate"
# ]
scheduler_events = {
    # "cron": {"15 15,20 * * *": ["devotee_diary.tasks.sadhana_reminder"]},
    "cron": {"30 15,20 * * *": ["devotee_diary.tasks.sadhana_reminder_1"]},
    # "cron": {"30 20 * * *": ["devotee_diary.tasks.sadhana_reminder_2"]},
}
