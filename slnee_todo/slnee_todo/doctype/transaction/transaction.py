# Copyright (c) 2021, erpcloud.systems and contributors
# For license information, please see license.txt
from __future__ import unicode_literals
import frappe
from frappe import _
from six import iteritems
from email_reply_parser import EmailReplyParser
from frappe.utils import (flt, getdate, get_url, now,
	nowtime, get_time, today, get_datetime, add_days)
from erpnext.controllers.queries import get_filters_cond
from frappe.desk.reportview import get_match_cond
from erpnext.hr.doctype.daily_work_summary.daily_work_summary import get_users_email
from erpnext.hr.doctype.holiday_list.holiday_list import is_holiday
from frappe.model.document import Document
from erpnext.education.doctype.student_attendance.student_attendance import get_holiday_list
from datetime import datetime, timedelta
from datetime import date
import operator
import json
import re, datetime, math, time
from urllib.parse import quote, urljoin
from frappe.desk.utils import slug
from frappe.utils import add_to_date, now, nowdate
from frappe.model.document import Document


class Transaction(Document):
	@frappe.whitelist()
	def on_submit(self):
		self.update_end_date()

	@frappe.whitelist()
	def update_end_date(self):
		frappe.db.commit()
		if self.workflow_state == "Done":
			frappe.db.sql("""update `tabTransaction` set end_date = %s where name=%s """, (nowdate(), self.name))
			self.reload()

pass



@frappe.whitelist()
def update_transaction_status():
	transactions = frappe.db.sql(""" select name, estimated_duration, start_date from `tabTransaction` where docstatus != 2 and workflow_state != 'Done' """, as_dict=1)

	for x in transactions:
		y = int(x.estimated_duration)
		z = int(2 * x.estimated_duration)

		if getdate(nowdate()) > getdate(add_to_date(x.start_date, days=y)) and getdate(nowdate()) < getdate(add_to_date(x.start_date, days=z)):
			#update = ("""update `tabTransaction` set status = 'Late' where name=%s """, x.name)
			frappe.db.set_value('Transaction', x.name, 'status', 'Late', update_modified=False)
			#return update

		elif getdate(add_to_date(x.start_date, days=z)) < getdate(nowdate()):
			#update = ("""update `tabTransaction` set status = 'Too Late' where name=%s """, x.name)
			#return update
			frappe.db.set_value('Transaction', x.name, 'status', 'Too Late', update_modified=False)




	"""
	x = (2 * self.estimated_duration)

	if getdate(nowdate()) > getdate(add_to_date(self.start_date, days=self.estimated_duration)) and getdate(nowdate()) < getdate(add_to_date(self.start_date, days=x)):
		self.status = 'Late'
	elif getdate(add_to_date(self.start_date, days=x)) < getdate(nowdate()):
		self.status = 'Too Late'
	else:
		self.status = 'Active'
	"""
