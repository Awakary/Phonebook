import json
from print_functions import print_pages
from add import add_note
from redakt import redakt_note
from search import search_note


def choose_operation():
    while True:
        oper = input('''Доступные команды справочника: 
                           Вывести весь справочник постранично -  1
                           Вывести нужную страницу справочника  - 2
                           Добавить запись -  3
                           Редактировать запись -  4
                           Найти запись(и) -  5
                           Введите цифру: ''')

        if oper in '12345':
            break
        else:
            print('Введена некорректная команда')
    return int(oper)


def main():
    while True:
        with open('Phonebook.json', encoding='utf-8') as file:  # загрузка справочника
            spr = json.load(file)

        operation = choose_operation()            # пользователь выбирает команду
        if operation in (1, 2):                   # запуск соответствующей функции по команде
            print_pages(spr, operation)
        elif operation == 3:
            add_note(spr)
        elif operation == 4:
            redakt_note(spr)
        elif operation == 5:
            search_note(spr)
        answer = input('''Закрыть справочник? Да - 1, Продолжить работу со справочником - 2 ''')
        if answer == '1':
            print('Справочник закрыт')
            break
        else:
            continue


if __name__ == "__main__":
    main()
