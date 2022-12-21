from openpyxl import load_workbook

def user_ident():
    role = int(input('Если Вы учитель - введите 1, если ученик - введите 2, для выхода введите 0\n'))
    while role < 0 or role > 2:
        role = int(input("Пожалуйста, укажите, кто Вы, введите 1, 2 или 0\n"))
    return role

def name_enter():
    name = input('Для продолжения введите фамилию ученика\n') 
    return name

def teacher_greeting():
    action = int(input("Для добавления ученика введите 1, для добавления оценки ученику введите 2, для выхода введите 0\n"))
    while action < 0 or action > 2:
        action = int(input("Пожалуйста, выберите действие: 1, 2 или 0\n"))
    return action

def discipline_enter():
    discipline = input('Введите название учебной дисциплины для добавления оценки\n')
    return discipline

def wrong_discipline():
    ans = int(input('Такой дисциплины нет в списке. Добавить - введите 1, повторить ввод - введите 2, выйти - введите 0\n'))
    while ans < 0 or ans > 2:
        ans = int(input("Пожалуйста, выберите действие: 1, 2 или 0\n"))
    return ans

def score_enter():
    score = int(input("Введите оценку от 2 до 5\n"))
    while score < 2 or score > 5:
        score = int(input("Оценка может быть только числом от 2 до 5, повторите ввод\n"))
        print('Оценка добавлена!')
    return score

def goodbye():
    print('Работа программы завершена, до свидания!')

def wrong_name():
    name = input("Такой фамилии нет в списке. Возможно, Вы ошиблись, или фамилию еще не добавили в список.\n\
    Введите фамилию еще раз или введите 0 для выхода\n")
    return name

def find_name():
    wb = load_workbook('test.xlsx')
    name = name_enter()
    students = wb.get_sheet_names()
    while name not in students:
        name = wrong_name()
        if name == '0':
            break
    return name
