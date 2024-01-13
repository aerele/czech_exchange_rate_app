import frappe
from erpnext.controllers.taxes_and_totals import get_itemised_tax_breakup_data, get_rounded_tax_amount

def get_item_taxes(doctype= None, docname= None, decimal= 2):

    if not doctype or not docname : return

    doc = frappe.get_doc(doctype, docname)

    if not doc.get('other_charges_calculation'): return {}

    tax_breakup = get_itemised_tax_breakup_data(doc)

    get_rounded_tax_amount(tax_breakup, doc.precision("tax_amount", "taxes"))

    item_tax_percentage = {
                tax.get('item') : tax.popitem()[1].get('tax_rate', 0) for tax in tax_breakup
                }

    return item_tax_percentage
