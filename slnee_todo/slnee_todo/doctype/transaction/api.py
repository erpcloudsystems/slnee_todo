from __future__ import unicode_literals
import frappe
from frappe import auth
import datetime
import json, ast




current_date = datetime.datetime.today().strftime('%Y-%m-%d')
current_user = frappe.session.user


@frappe.whitelist(allow_guest=True)
def login(usr, pwd):
    try:
        login_manager = frappe.auth.LoginManager()
        login_manager.authenticate(user=usr, pwd=pwd)
        login_manager.post_login()

    except frappe.exceptions.AuthenticationError:
        frappe.clear_messages()
        frappe.local.response["message"] = {
            "success_key": true,
            "message": "اسم المستخدم او كلمة المرور غير صحيحة !"
        }

        return

    api_generate = generate_keys(frappe.session.user)
    user = frappe.get_doc('User', frappe.session.user)


    frappe.response["message"] = {
        "success_key": True,
        "message": "Authentication Success",
        "sid": frappe.session.sid,
        "api_key": user.api_key,
        "api_secret": api_generate,
        "email": user.email,
        "user_type": user.role_profile_name
    }

    return


def generate_keys(user):
    user_details = frappe.get_doc('User', user)
    api_secret = frappe.generate_hash(length=15)

    if not user_details.api_key:
        api_key = frappe.generate_hash(length=15)
        user_details.api_key = api_key

    user_details.api_secret = api_secret
    user_details.save()
    return api_secret

# ------------------------------------------------------------------------------------

@frappe.whitelist()
def add_transaction(transaction_name, start_date, priority,transaction_owner_name,estimated_duration,description,transaction_type,add_voice,employee,general_remarks,final_description):


    transaction = frappe.get_doc({"doctype":"Transaction",
      "transaction_name": transaction_name,
      "transaction_owner_name": transaction_owner_name,
      "start_date": start_date,
      "estimated_duration": estimated_duration,
      "priority": priority,
      "description": description,
      "transaction_type": transaction_type,
      "add_voice": add_voice,
      "employee": employee,
      "general_remarks": general_remarks,
      "final_description": final_description

    })


    transaction.insert()
    transaction_id = transaction.name
    frappe.db.commit()

    if(transaction):
        message = frappe.response["message"] = {
            "success_key": True,
            "message": "تمت اضافة المعاملة بنجاح !",
            "transaction_id": transaction_id
        }
        return message
    else:return "حدث خطأ ولم نتمكن من اضافة المعاملة . برجاء المحاولة مرة اخري!"


# ------------------------------------------------------------------------------------
@frappe.whitelist()
def attachments(transaction_id, file, attachment_name):
    attachment = frappe.get_doc({"doctype":"Attachments Table",
      "parenttype": "Transaction",
      "parentfield": "attachments_table",
      "parent": transaction_id,
      "attachment": file,
      "attachment_name ": attachment_name
    })

    attachment.insert()
    frappe.db.commit()

    if(attachment):
        return attachment
    else:
        return "Error encountered!"

# ------------------------------------------------------------------------------------

@frappe.whitelist()
def transaction_remark(transaction_id, remark):
    remarks = frappe.get_doc({"doctype":"Remarks Table",
      "parenttype": "Transaction",
      "parentfield": "remarks_table",
      "parent": transaction_id,
      "user": current_user,
      "remark": remark,
      "remark_date": current_date
    })

    remarks.insert()
    frappe.db.commit()

    if remarks:
        message = frappe.response["message"] = {
            "success_key": True,
            "message": "تمت اضافة الملاحظة بنحاخ !"
        }
        return message
    else:
        return "حدث خطأ ولم نتمكن من اضافة الملاحظة . برجاء المحاولة مرة اخري!"

# ------------------------------------------------------------------------------------

@frappe.whitelist()
def transaction_situation(transaction_id, current_situation):
    remarks = frappe.get_doc({"doctype":"Current Situation Table",
      "parenttype": "Transaction",
      "parentfield": "current_situation",
      "parent": transaction_id,
      "input_user": current_user,
      "current_situation": current_situation,
      "input_date": current_date
    })

    remarks.insert()
    frappe.db.commit()

    if remarks:
        message = frappe.response["message"] = {
            "success_key": True,
            "message": "تم اضافة الوضع الحالي بنجاح !"
        }
        return message
    else:
        return "حدث خطأ ولم نتمكن من اضافة الوضع الحالي . برجاء المحاولة مرة اخري!"

# ------------------------------------------------------------------------------------

# You can replace [*] with the fields you need from your database table
# Replace [critetia_field] with the appropriate field from your table
# Please let me know what you meant by [page number]

@frappe.whitelist()
def list_transaction(transaction_number,transaction_owner_name,start_date,current_situation, priorityy ,posting_date,transaction_name,description,transaction_type,employee,employee_name,final_description,general_remarks):
    conditions=''
    if employee:
        conditions += "and `tabTransaction`.employee like {employee}".format(employee=employee)
    if transaction_number:
        conditions += "and `tabTransaction`.name like '%{transaction_number}%'".format(transaction_number=transaction_number)
    if transaction_owner_name:
        conditions += "and `tabTransaction`.transaction_owner_name like {transaction_owner_name}".format(transaction_owner_name=transaction_owner_name)
    if start_date:
        conditions += "and `tabTransaction`.start_date like {start_date}".format(start_date=start_date)
    if current_situation:
        conditions += "and `tabTransaction`.current_situation like {current_situation}".format(current_situation=current_situation)
    if priorityy:
        conditions += "and `tabTransaction`.priority like '%{priority}%'".format(priority=priorityy)
    if posting_date:
        conditions += "and `tabTransaction`.posting_date = {posting_date}".format(posting_date=posting_date)
    if transaction_name:
        conditions += "and `tabTransaction`.transaction_name like '%{transaction_name}%'".format(transaction_name=transaction_name)
    if description:
        conditions += "and `tabTransaction`.description like '%{description}%'".format(description=description)
    if transaction_type:
        conditions += "and `tabTransaction`.transaction_type like '%{transaction_type}%'".format(transaction_type=transaction_type)
    if employee_name:
        conditions += "and `tabTransaction`.employee_name like '%{employee_name}%'".format(employee_name=employee_name)
    if final_description:
        conditions += "and `tabTransaction`.final_description like '%{final_description}%'".format(final_description=final_description)
    if general_remarks:
        conditions += "and `tabTransaction`.general_remarks like '%{general_remarks}%'".format(general_remarks=general_remarks)

    all_transaction = frappe.db.sql("""SELECT * FROM `tabTransaction` where docstatus !=2 {conditions}""".format(conditions=conditions), as_dict=1)

    if (all_transaction):
        return all_transaction
    else:
        return "لا توجد معاملات برجاء البحث مرة اخرى"

@frappe.whitelist()
def priority_options():
    get_proirity = frappe.db.sql(""" select name,value from `tabTransaction Priority` """, as_dict=True)

    if get_proirity:
        return get_proirity
    else:
        return "لا توجد خيارات متاحة !"

@frappe.whitelist()
def transaction_type_options():
    get_transaction_type = frappe.db.sql(""" select name,value from `tabTransaction Type`""",as_dict=True)

    if get_transaction_type:
        return get_transaction_type
    else:
        return "لا توجد انواع متاحة !"


@frappe.whitelist()
def list_employee():
    all_employee = frappe.db.sql("""SELECT name,employee_name,department FROM `tabEmployee` where status ='Active'""",as_dict=True)

    if all_employee:
        return all_employee
    else:
        return "لا يوجد موظفين !"

@frappe.whitelist()
def list_remarks(transaction_id):
    all_remarks = frappe.db.sql("""SELECT * FROM `tabRemarks Table` where parent =%s""",transaction_id,as_dict=True)
    if all_remarks:
        return all_remarks
    else:
        return "لا توجد ملاحظات على المعاملة !"

@frappe.whitelist()
def list_situation(transaction_id):
    all_situation = frappe.db.sql("""SELECT * FROM `tabCurrent Situation Table` where parent =%s""",transaction_id,as_dict=True)
    if all_situation:
        return all_situation
    else:
        return "لم يتم تسجيل اي موقف يخص المعاملة !"

@frappe.whitelist()
def list_attachments(transaction_id):
    all_attachments = frappe.db.sql("""SELECT * FROM `tabFile` where attached_to_name =%s""",transaction_id,as_dict=True)

    if all_attachments:
        return all_attachments
    else:
        return "لا يوجد مرفقات على المعامله !"