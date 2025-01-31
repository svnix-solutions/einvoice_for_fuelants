from . import __version__ as app_version

app_name = "einvoice_for_fuelants"
app_title = "Einvoice For Fuelants"
app_publisher = "SVNIX Solutions"
app_description = "e-Invoicing for fuelants streamlines fuel transaction management by automating GST-compliant invoicing and connecting directly to e-Invoice registration portals. With this feature, users can configure fuel items, set up GST details, and automatically calculate taxes based on item specifications. Each e-Invoice generates an IRN (Invoice Reference Number) and a QR code upon submission, meeting regulatory standards. Additionally, ERPNext provides downloadable PDFs for easy record-keeping, along with automated reports to track invoice status and ensure compliance. This setup minimizes manual data entry and enhances efficiency for organizations handling high-volume fuel transactions."
app_email = "contact@svnix.solutions"
app_license = "GPLv3"

override_whitelisted_methods = {
    "india_compliance.gst_india.utils.e_invoice.generate_e_invoice": 
        "einvoice_for_fuelants.einvoice_for_fuelants.patches.fuelants.generate_e_invoice"
}

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/einvoice_for_fuelants/css/einvoice_for_fuelants.css"
# app_include_js = "/assets/einvoice_for_fuelants/js/einvoice_for_fuelants.js"

# include js, css files in header of web template
# web_include_css = "/assets/einvoice_for_fuelants/css/einvoice_for_fuelants.css"
# web_include_js = "/assets/einvoice_for_fuelants/js/einvoice_for_fuelants.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "einvoice_for_fuelants/public/scss/website"

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
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "einvoice_for_fuelants.utils.jinja_methods",
#	"filters": "einvoice_for_fuelants.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "einvoice_for_fuelants.install.before_install"
# after_install = "einvoice_for_fuelants.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "einvoice_for_fuelants.uninstall.before_uninstall"
# after_uninstall = "einvoice_for_fuelants.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "einvoice_for_fuelants.utils.before_app_install"
# after_app_install = "einvoice_for_fuelants.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "einvoice_for_fuelants.utils.before_app_uninstall"
# after_app_uninstall = "einvoice_for_fuelants.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "einvoice_for_fuelants.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"einvoice_for_fuelants.tasks.all"
#	],
#	"daily": [
#		"einvoice_for_fuelants.tasks.daily"
#	],
#	"hourly": [
#		"einvoice_for_fuelants.tasks.hourly"
#	],
#	"weekly": [
#		"einvoice_for_fuelants.tasks.weekly"
#	],
#	"monthly": [
#		"einvoice_for_fuelants.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "einvoice_for_fuelants.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "einvoice_for_fuelants.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "einvoice_for_fuelants.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["einvoice_for_fuelants.utils.before_request"]
# after_request = ["einvoice_for_fuelants.utils.after_request"]

# Job Events
# ----------
# before_job = ["einvoice_for_fuelants.utils.before_job"]
# after_job = ["einvoice_for_fuelants.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"einvoice_for_fuelants.auth.validate"
# ]
