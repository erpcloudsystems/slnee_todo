// Copyright (c) 2016, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Transactions Following Report"] = {
	"filters": [
		{
			"fieldname": "from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"default": frappe.defaults.get_user_default("year_start_date"),
			"reqd": 1
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"default": frappe.defaults.get_user_default("year_end_date"),
			"reqd": 1
		},
	],
	    "formatter": function (value, row, column, data, default_formatter) {
                value = default_formatter(value, row, column, data);


                if (column.fieldname == "transaction_number" && data && data.workflow_state == "Done") {
                     value = "<span style='color:green;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "workflow_state" && data && data.workflow_state == "Done") {
                     value = "<span style='color:green;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "transaction_owner_name" && data && data.workflow_state == "Done") {
                     value = "<span style='color:green;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "transaction_name" && data && data.workflow_state == "Done") {
                     value = "<span style='color:green;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "transaction_type" && data && data.workflow_state == "Done") {
                     value = "<span style='color:green;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "start_date" && data && data.workflow_state == "Done") {
                     value = "<span style='color:green;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "end_date" && data && data.workflow_state == "Done") {
                     value = "<span style='color:green;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "current_situation" && data && data.workflow_state == "Done") {
                     value = "<span style='color:green;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "remarks" && data && data.workflow_state == "Done") {
                     value = "<span style='color:green;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "attachments_no" && data && data.workflow_state == "Done") {
                     value = "<span style='color:green;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "attachments" && data && data.workflow_state == "Done") {
                     value = "<span style='color:green;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "transaction_number" && data && data.workflow_state == "Under Process") {
                     value = "<span style='color:orange;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "workflow_state" && data && data.workflow_state == "Under Process") {
                     value = "<span style='color:orange;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "transaction_owner_name" && data && data.workflow_state == "Under Process") {
                     value = "<span style='color:orange;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "transaction_name" && data && data.workflow_state == "Under Process") {
                     value = "<span style='color:orange;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "transaction_type" && data && data.workflow_state == "Under Process") {
                     value = "<span style='color:orange;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "start_date" && data && data.workflow_state == "Under Process") {
                     value = "<span style='color:orange;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "end_date" && data && data.workflow_state == "Under Process") {
                     value = "<span style='color:orange;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "current_situation" && data && data.workflow_state == "Under Process") {
                     value = "<span style='color:orange;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "remarks" && data && data.workflow_state == "Under Process") {
                     value = "<span style='color:orange;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "attachments_no" && data && data.workflow_state == "Under Process") {
                     value = "<span style='color:orange;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "attachments" && data && data.workflow_state == "Under Process") {
                     value = "<span style='color:orange;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "transaction_number" && data && data.workflow_state == "With Office Manager") {
                     value = "<span style='color:blue;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "workflow_state" && data && data.workflow_state == "With Office Manager") {
                     value = "<span style='color:blue;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "transaction_owner_name" && data && data.workflow_state == "With Office Manager") {
                     value = "<span style='color:blue;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "transaction_name" && data && data.workflow_state == "With Office Manager") {
                     value = "<span style='color:blue;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "transaction_type" && data && data.workflow_state == "With Office Manager") {
                     value = "<span style='color:blue;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "start_date" && data && data.workflow_state == "With Office Manager") {
                     value = "<span style='color:blue;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "end_date" && data && data.workflow_state == "With Office Manager") {
                     value = "<span style='color:blue;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "current_situation" && data && data.workflow_state == "With Office Manager") {
                     value = "<span style='color:blue;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "remarks" && data && data.workflow_state == "With Office Manager") {
                     value = "<span style='color:blue;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "attachments_no" && data && data.workflow_state == "With Office Manager") {
                     value = "<span style='color:blue;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "attachments" && data && data.workflow_state == "With Office Manager") {
                     value = "<span style='color:blue;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "name" && data) {
                     value = "<span style='color:black;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "transaction_number" && data && data.workflow_state == "Entering Data ...") {
                     value = "<span style='color:black;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "workflow_state" && data && data.workflow_state == "Entering Data ...") {
                     value = "<span style='color:black;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "transaction_owner_name" && data && data.workflow_state == "Entering Data ...") {
                     value = "<span style='color:black;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "transaction_name" && data && data.workflow_state == "Entering Data ...") {
                     value = "<span style='color:black;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "transaction_type" && data && data.workflow_state == "Entering Data ...") {
                     value = "<span style='color:black;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "start_date" && data && data.workflow_state == "Entering Data ...") {
                     value = "<span style='color:black;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "end_date" && data && data.workflow_state == "Entering Data ...") {
                     value = "<span style='color:black;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "current_situation" && data && data.workflow_state == "Entering Data ...") {
                     value = "<span style='color:black;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "remarks" && data && data.workflow_state == "Entering Data ...") {
                     value = "<span style='color:black;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "attachments_no" && data && data.workflow_state == "Entering Data ...") {
                     value = "<span style='color:black;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "attachments" && data && data.workflow_state == "Entering Data ...") {
                     value = "<span style='color:black;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "transaction_number" && data && data.workflow_state == "Pending") {
                     value = "<span style='color:red;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "workflow_state" && data && data.workflow_state == "Pending") {
                     value = "<span style='color:red;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "transaction_owner_name" && data && data.workflow_state == "Pending") {
                     value = "<span style='color:red;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "transaction_name" && data && data.workflow_state == "Pending") {
                     value = "<span style='color:red;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "transaction_type" && data && data.workflow_state == "Pending") {
                     value = "<span style='color:red;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "start_date" && data && data.workflow_state == "Pending") {
                     value = "<span style='color:red;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "end_date" && data && data.workflow_state == "Pending") {
                     value = "<span style='color:red;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "current_situation" && data && data.workflow_state == "Pending") {
                     value = "<span style='color:red;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "remarks" && data && data.workflow_state == "Pending") {
                     value = "<span style='color:red;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "attachments_no" && data && data.workflow_state == "Pending") {
                     value = "<span style='color:red;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "attachments" && data && data.workflow_state == "Pending") {
                     value = "<span style='color:red;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "transaction_number" && data && data.workflow_state == "Modification Requested") {
                     value = "<span style='color:purple;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "workflow_state" && data && data.workflow_state == "Modification Requested") {
                     value = "<span style='color:purple;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "transaction_owner_name" && data && data.workflow_state == "Modification Requested") {
                     value = "<span style='color:purple;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "transaction_name" && data && data.workflow_state == "Modification Requested") {
                     value = "<span style='color:purple;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "transaction_type" && data && data.workflow_state == "Modification Requested") {
                     value = "<span style='color:purple;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "start_date" && data && data.workflow_state == "Modification Requested") {
                     value = "<span style='color:purple;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "end_date" && data && data.workflow_state == "Modification Requested") {
                     value = "<span style='color:purple;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "current_situation" && data && data.workflow_state == "Modification Requested") {
                     value = "<span style='color:purple;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "remarks" && data && data.workflow_state == "Modification Requested") {
                     value = "<span style='color:purple;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "attachments_no" && data && data.workflow_state == "Modification Requested") {
                     value = "<span style='color:purple;font-weight: bold;'>" + value + "</span>";
                }
                if (column.fieldname == "attachments" && data && data.workflow_state == "Modification Requested") {
                     value = "<span style='color:purple;font-weight: bold;'>" + value + "</span>";
                }








                return value;
            }

}


