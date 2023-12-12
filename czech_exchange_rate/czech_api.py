import frappe
from frappe.utils import get_datetime_str, nowdate, flt, add_days
from frappe import _

from erpnext.accounts.doctype.currency_exchange_settings.currency_exchange_settings import CurrencyExchangeSettings
from erpnext.setup.utils import format_ces_api

class CustomCurrencyExchangeSettings(CurrencyExchangeSettings):
	def validate(self):
		if self.service_provider == "czechexchange.app":
			pass
		else:
			super().validate()

@frappe.whitelist()
def get_exchange_rate(from_currency, to_currency, transaction_date=None, args=None):
	if not (from_currency and to_currency):
		# manqala 19/09/2016: Should this be an empty return or should it throw and exception?
		return
	if from_currency == to_currency:
		return 1

	if not transaction_date:
		transaction_date = nowdate()
	currency_settings = frappe.get_doc("Accounts Settings").as_dict()
	allow_stale_rates = currency_settings.get("allow_stale")

	filters = [
		["date", "<=", get_datetime_str(transaction_date)],
		["from_currency", "=", from_currency],
		["to_currency", "=", to_currency]
	]

	if args == "for_buying":
		filters.append(["for_buying", "=", "1"])
	elif args == "for_selling":
		filters.append(["for_selling", "=", "1"])

	if not allow_stale_rates:
		stale_days = currency_settings.get("stale_days")
		checkpoint_date = add_days(transaction_date, -stale_days)
		filters.append(["date", ">", get_datetime_str(checkpoint_date)])

	# cksgb 19/09/2016: get last entry in Currency Exchange with from_currency and to_currency.
	entries = frappe.get_all(
		"Currency Exchange", fields=["exchange_rate"], filters=filters, order_by="date desc", limit=1
	)
	if entries:
		return flt(entries[0].exchange_rate)

	if frappe.get_cached_value(
		"Currency Exchange Settings", "Currency Exchange Settings", "disabled"
	):
		return 0.00

	try:
		cache = frappe.cache()
		key = "currency_exchange_rate_{0}:{1}:{2}".format(
			transaction_date, from_currency, to_currency)
		value = cache.get(key)

		if not value :
			import requests

			settings = frappe.get_cached_doc("Currency Exchange Settings")

			if settings.service_provider == "czechexchange.app":
				api_url = settings.api_endpoint
				response = requests.get(api_url, params={
					"date": transaction_date
				})
				response.raise_for_status()
				if response.ok:
					value = response.json()["rates"]

					for er in value:
						if er['currencyCode'] == from_currency:
							value = er['rate']
							break

					cache.setex(name=key, time=21600, value=flt(value))
				else:
					value = 0.0
					frappe.msgprint("API Link Expired")
			else:
				req_params = {
					"transaction_date": transaction_date,
					"from_currency": from_currency,
					"to_currency": to_currency,
				}
				params = {}
				for row in settings.req_params:
					params[row.key] = format_ces_api(row.value, req_params)
				response = requests.get(format_ces_api(
					settings.api_endpoint, req_params), params=params)
				# expire in 6 hours
				response.raise_for_status()
				value = response.json()
				for res_key in settings.result_key:
					value = value[format_ces_api(str(res_key.key), req_params)]
				cache.setex(name=key, time=21600, value=flt(value))
		return flt(value)
	except Exception:
		frappe.log_error("Unable to fetch exchange rate")
		frappe.msgprint(
			_(
				"Unable to find exchange rate for {0} to {1} for key date {2}. Please create a Currency Exchange record manually"
			).format(from_currency, to_currency, transaction_date)
		)
		return 0.0
