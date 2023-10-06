from print_functions import print_phone


def search_note(spr: list):  # фунция поиска записей по справочнику
    f = input('''Поиск записей
              По одному критерию - введите 1 
              По нескольким критериям - введите 2  
              ''')
    flag = True
    if f == '1':  # запуск поиска по одному критерию
        a = input('Введите один критерий (фамилию, имя или др.) ')
        for i in spr:
            if a.capitalize() in i.values():  # поиск введенного параметра в значениях словарей
                print(print_phone(i))
                flag = False

    if f == '2':  # запуск поиска по нескольким критериям
        a = input('Введите несколько критериев через пробел(фамилия, имя и др.) ')
        a = a.split()
        for i in spr:
            d = []
            for j in a:
                d.append(j.capitalize() in i.values())
            if all(d):  # поиск введенных параметров в значениях словарей
                print(print_phone(i))
                flag = False
    if flag:
        print('Нет записей, соответствующих данному критерию')
