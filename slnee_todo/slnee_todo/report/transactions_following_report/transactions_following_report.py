# Copyright (c) 2013, erpcloud.systems and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _


def execute(filters=None):
	columns, data = [], []
	columns = get_columns()
	data = get_data(filters, columns)
	return columns, data

def get_columns():
	return [
		{
			"label": _("Transaction"),
			"fieldname": "name",
			"fieldtype": "Link",
			"options": "Transaction",
			"width": 120
		},
		{
			"label": _("Transaction No."),
			"fieldname": "transaction_number",
			"fieldtype": "Data",
			"width": 125
		},
		{
			"label": _("Transaction State"),
			"fieldname": _("workflow_state"),
			"fieldtype": "Data",
			"width": 140
		},
		{
			"label": _("Transaction Owner Name"),
			"fieldname": "transaction_owner_name",
			"fieldtype": "Data",
			"width": 180
		},
		{
			"label": _("Transaction Name"),
			"fieldname": "transaction_name",
			"fieldtype": "Data",
			"width": 200
		},
		{
			"label": _("Transaction Type"),
			"fieldname": "transaction_type",
			"fieldtype": "Data",
			"width": 200
		},
		{
			"label": _("Start Date"),
			"fieldname": "start_date",
			"fieldtype": "Date",
			"width": 120
		},
		{
			"label": _("End Date"),
			"fieldname": "end_date",
			"fieldtype": "Date",
			"width": 120
		},
		{
			"label": _("Current Situation"),
			"fieldname": "current_situation",
			"fieldtype": "Data",
			"width": 300
		},
		{
			"label": _("Remarks"),
			"fieldname": "remarks",
			"fieldtype": "Data",
			"width": 300
		},
		{
			"label": _("No. Of Attachments"),
			"fieldname": "attachments_no",
			"fieldtype": "Data",
			"width": 150
		},
		{
			"label": _("Attached Files"),
			"fieldname": "attachments",
			"fieldtype": "Data",
			"width": 300
		}
	]

def get_data(filters, columns):
	item_price_qty_data = []
	item_price_qty_data = get_item_price_qty_data(filters)
	return item_price_qty_data

def get_item_price_qty_data(filters):
	conditions = ""
	if filters.get("from_date"):
		conditions += " and `tabTransaction`.posting_date>=%(from_date)s"
	if filters.get("to_date"):
		conditions += " and `tabTransaction`.posting_date<=%(to_date)s"
	item_results = frappe.db.sql("""
				SELECT
						`tabTransaction`.name as name  ,
						`tabTransaction`.transaction_number as transaction_number,
						`tabTransaction`.workflow_state as workflow_state,
						`tabTransaction`.transaction_owner_name as transaction_owner_name,
						`tabTransaction`.transaction_name as transaction_name,
						`tabTransaction`.transaction_type as transaction_type,
						`tabTransaction`.start_date as start_date,
						`tabTransaction`.end_date as end_date,
		
						(SELECT `tabCurrent Situation Table`.current_situation 
						FROM `tabCurrent Situation Table`
						WHERE `tabCurrent Situation Table`.parent = `tabTransaction`.name
						ORDER BY idx DESC LIMIT 1) as current_situation,
		
						(SELECT GROUP_CONCAT('<li>',`tabRemarks Table`.remark order by idx separator '</li>')
						FROM `tabRemarks Table`
						WHERE `tabRemarks Table`.parent = `tabTransaction`.name) as remarks,
		
						(SELECT count(file_name)
						FROM `tabFile`
						WHERE `tabFile`.attached_to_name = `tabTransaction`.name) as attachments_no,
						
						(SELECT GROUP_CONCAT('<li>',`tabFile`.file_name order by idx separator '<li>')
						FROM `tabFile`
						WHERE `tabFile`.attached_to_name = `tabTransaction`.name) as attachments

				FROM
				`tabTransaction`
				
				WHERE
				`tabTransaction`.docstatus != 2
				{conditions}
					
				ORDER BY `tabTransaction`.name desc
				

				""".format(conditions=conditions), filters, as_dict=1)

	# price_list_names = list(set([item.price_list_name for item in item_results]))

	# buying_price_map = get_price_map(price_list_names, buying=1)
	# selling_price_map = get_price_map(price_list_names, selling=1)

	result = []
	if item_results:
		for item_dict in item_results:
			data = {
				'name': item_dict.name,
				'transaction_number': item_dict.transaction_number,
				'workflow_state': item_dict.workflow_state,
				'transaction_owner_name': item_dict.transaction_owner_name,
				'transaction_name': item_dict.transaction_name,
				'transaction_type': item_dict.transaction_type,
				'start_date': item_dict.start_date,
				'end_date': item_dict.end_date,
				'current_situation': item_dict.current_situation,
				'remarks': item_dict.remarks,
				'attachments_no': item_dict.attachments_no,
				'attachments': item_dict.attachments,
			}
			result.append(data)

	return result

def get_price_map(price_list_names, buying=0, selling=0):
	price_map = {}

	if not price_list_names:
		return price_map

	rate_key = "Buying Rate" if buying else "Selling Rate"
	price_list_key = "Buying Price List" if buying else "Selling Price List"

	filters = {"name": ("in", price_list_names)}
	if buying:
		filters["buying"] = 1
	else:
		filters["selling"] = 1

	pricing_details = frappe.get_all("Item Price",
									 fields=["name", "price_list", "price_list_rate"], filters=filters)

	for d in pricing_details:
		name = d["name"]
		price_map[name] = {
			price_list_key: d["price_list"],
			rate_key: d["price_list_rate"]
		}

	return price_map
