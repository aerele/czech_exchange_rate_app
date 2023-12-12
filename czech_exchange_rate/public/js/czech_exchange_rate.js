
frappe.ui.form.on('Currency Exchange Settings', {
	service_provider: function(frm) {
		if (frm.doc.service_provider == "czechexchange.app") {
			let result = ['rates'];
			let params = {
				date: '{transaction_date}'
			};
			add_param(frm, "https://api.cnb.cz/cnbapi/exrates/daily", params, result);
		}
	}
});
