// functions in this file will apply to most transactions
// POS Invoice is a notable exception since it doesn't get created from the UI

const TRANSACTION_DOCTYPES = [
    "Quotation",
    "Sales Order",
    "Delivery Note",
    "Sales Invoice",
    "Purchase Order",
    "Purchase Receipt",
    "Purchase Invoice",
];

for (const doctype of TRANSACTION_DOCTYPES) {
    frappe.ui.form.on(doctype, {
        update_exchange_rate: function(frm) {
            cur_frm.doc.__onload.load_after_mapping = false
            cur_frm.trigger("currency")
        }
    })
}
