import frappe

@frappe.whitelist(allow_guest=True)
def login(username, password):
	login_manager = LoginManager()
	login_manager.authenticate(username,password)
	login_manager.post_login()

	if frappe.response['message'] == 'Logged In':
		user = frappe.db.get_value("User", {"user": login_manager.user}, "name")

		if user:return user
        else:
	        return "No user Found."

# ------------------------------------------------------------------------------------

# Add all the fields for which data you capture from the frontend app
@frappe.whitelist()
def add_task(token, subject):
    task = frappe.get_doc({"doctype":"Task",
      "subject": subject
    })

    task.insert()
    frappe.db.commit()

    if(task):
        return True
    else:
        return "We encountered an error!"


# ------------------------------------------------------------------------------------

# [tabTask Docs] should be replaced with the table which contains the task files 
# [file_name] should be replaced with the name of the field receiving the files
@frappe.whitelist()
def upload_attachment(task_id, attachment):
    upload_files = frappe.db.sql(f"""UPDATE `tabTask Docs` SET file_name={attachment} WHERE name='{task_id}';""")
    frappe.db.commit()

    if(upload_files):
        return True
    else:
        return False

# ------------------------------------------------------------------------------------

# Other than the [title], please add all the other field names you need to send from the frontend app
@frappe.whitelist()
def task_note(token, task_id, title):
    task_note = frappe.db.sql(f"""UPDATE `tabNote` SET title={title} WHERE name='{task_id}';""")
    frappe.db.commit()

    if(task_note):
        return True
    else:
        return False

# ------------------------------------------------------------------------------------

# You can replace [*] with the fields you need from your database table
# Replace [critetia_field] with the appropriate field from your table
# Please let me know what you meant by [page number]
@frappe.whitelist()
def list_tasks(criteria, token):
    tasks = frappe.db.sql(f"""SELECT * FROM `tabTasks` WHERE critetia_field={criteria};""", as_dict=True)

    if(tasks):
        return tasks
    else:
        return "No Tasks found!"