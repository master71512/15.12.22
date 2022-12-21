import user_interface as ui
import student_action

def user_role():
    role = ui.user_ident()
    if role == 2:
        student_action.find_name()

user_role()