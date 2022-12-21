import user_interface as ui
import student_action
import teacher_action

def user_role():
    role = ui.user_ident()
    if role == 2:
        student_action.show_scores()
    if role == 1:
        teacher_action.choose_action()