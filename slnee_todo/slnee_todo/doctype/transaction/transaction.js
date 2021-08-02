// Copyright (c) 2021, erpcloud.systems and contributors
// For license information, please see license.txt

frappe.ui.form.on("Transaction", {
	setup: function(frm) {
		frm.set_query("employee", function() {
			return {
				filters: [
					["Employee","his_highness_employee", "=", 1]
				]
			};
		});
	}
});
