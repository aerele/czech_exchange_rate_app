from . import __version__ as app_version

app_name = "czech_exchange_rate"
app_title = "Czech Exchange Rate"
app_publisher = "SDI Gifts"
app_description = "Fetching Exchange Rate From Czech Bank"
app_email = "sdigifts@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/czech_exchange_rate/css/czech_exchange_rate.css"

# include js, css files in header of web template
# web_include_css = "/assets/czech_exchange_rate/css/czech_exchange_rate.css"
# web_include_js = "/assets/czech_exchange_rate/js/czech_exchange_rate.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "czech_exchange_rate/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "Currency Exchange Settings": "/public/js/czech_exchange_rate.js"
    }
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
#	"methods": "czech_exchange_rate.utils.jinja_methods",
#	"filters": "czech_exchange_rate.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "czech_exchange_rate.install.before_install"
# after_install = "czech_exchange_rate.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "czech_exchange_rate.uninstall.before_uninstall"
# after_uninstall = "czech_exchange_rate.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "czech_exchange_rate.notifications.get_notification_config"

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

override_doctype_class = {
	"Currency Exchange Settings": "czech_exchange_rate.czech_api.CustomCurrencyExchangeSettings"
}

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
#		"czech_exchange_rate.tasks.all"
#	],
#	"daily": [
#		"czech_exchange_rate.tasks.daily"
#	],
#	"hourly": [
#		"czech_exchange_rate.tasks.hourly"
#	],
#	"weekly": [
#		"czech_exchange_rate.tasks.weekly"
#	],
#	"monthly": [
#		"czech_exchange_rate.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "czech_exchange_rate.install.before_tests"

# Overriding Methods
# ------------------------------
#

override_whitelisted_methods = {
	"erpnext.setup.utils.get_exchange_rate": "czech_exchange_rate.czech_api.get_exchange_rate"
}
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "czech_exchange_rate.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["czech_exchange_rate.utils.before_request"]
# after_request = ["czech_exchange_rate.utils.after_request"]

# Job Events
# ----------
# before_job = ["czech_exchange_rate.utils.before_job"]
# after_job = ["czech_exchange_rate.utils.after_job"]

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
#	"czech_exchange_rate.auth.validate"
# ]
