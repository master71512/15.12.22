import user_interface as ui
import student_action

def user_role():
    role = ui.user_ident()
    if role == 2:
        student_action.show_scores()

user_role()