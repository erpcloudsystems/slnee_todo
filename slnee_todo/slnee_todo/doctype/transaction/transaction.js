// Copyright (c) 2021, erpcloud.systems and contributors
// For license information, please see license.txt

frappe.ui.form.on("Transaction", {
	setup: function(frm) {


		frm.set_query('employee', () => {
    return {
        filters: {
            role_profile_name: ['in', ['Todo User', 'Todo System Manager']]
        }
    }
})
	}
});
