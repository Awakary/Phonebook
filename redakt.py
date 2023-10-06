import json
from print_functions import print_phone


def redakt_note(s: list):        # фунция по редактированию записи
    while True:
        h = {}
        a = input('Введите пожалуйста ФИО буквами через пробел: ')       # валидация
        if a.replace(' ', '').isalpha() and a.count(' ') == 2:
            d = [i.capitalize() for i in a.split()]
            h = {'surname': d[0], 'name': d[1], 'patronymic': d[2]}

        flag = True         # переменная сменит значение на False, когда нужная запись будет найдена

        for i in range(len(s)):
            if list(h.values()) == list(s[i].values())[:3]:
                flag = False
                print(print_phone(s[i]))

                q = input('''Выберите, что хотите отредактировать:
                             организацию - ввведите 1
                             рабочий телефон -  введите 2 
                             мобильный телефон - введите 3
                             ''')

                if q == '1':
                    s[i]['work'] = input('Введите новую организацию: ')

                if q == '2':
                    s[i]['work_number'] = input('Введите новый рабочий телефон в формате XX-XX-XX: ')

                if q == '3':
                    s[i]['personal_number'] = input('Введите новый мобильный телефон в формате 89XXXXXXXXX: ')

        if flag:
            print(
                'Нет такого человека в справочнике')  # если flag не изменился- такой записи не было найдено
        else:
            break
    with open('Phonebook.json', 'w', encoding='utf8') as file:  # запись справочника в файл
        json.dump(s, file, indent=4, ensure_ascii=False)
    print('Запись отредактирована')
