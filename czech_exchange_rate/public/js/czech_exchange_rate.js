
frappe.ui.form.on('Currency Exchange Settings', {
	onload_post_render: function(frm){
		let options =  'czechexchange.app\n' + frm.fields_dict.service_provider.df.options;
		frm.fields_dict.service_provider.df.options = options
		cur_frm.refresh_fields()
	},

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
