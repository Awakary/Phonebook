import json


def add_note(s: list):    # функция добавления записи со всеми проверками на правильность введенных данных
    d = {}
    while True:
        a = input('Введите пожалуйста фамилию: ')
        if a.isalpha():
            d['surname'] = a.capitalize()
            break
        else:
            print('Фамилия должна состоять только из букв')
    while True:
        a = input('Введите пожалуйста имя: ')
        if a.isalpha():
            d['name'] = a.capitalize()
            break
        else:
            print('Имя должно состоять только из букв')
    while True:
        a = input('Введите пожалуйста отчество: ')
        if a.isalpha():
            d['patronymic'] = a.capitalize()
            break
        else:
            print('Отчество должно состоять только из букв')

    d['work'] = input('Введите пожалуйста организацию: ').capitalize()

    while True:
        a = input('Введите пожалуйста рабочий номер телефона в формате ХХ-ХХ-ХХ: ')
        if a.find('-') == 2 and a.rfind('-') == 5 and a.replace('-', '').isdigit() and len(a) == 8:
            d['work_number'] = a
            break
        else:
            print('Неверный формат номера')
    while True:
        a = input('Введите пожалуйста личный номер телефона в формате 89ХХХХХХХХХ: ')
        if a[:2] == '89' and a.isdigit() and len(a) == 11:
            d['personal_number'] = a
            break
        else:
            print('Неверный формат номера')

    s.append(d)                                          # добавление записи в список справочника
    s = sorted(s, key=lambda x: tuple(x.values()))       # сортировка всего справочника

    with open('Phonebook.json', 'w', encoding='utf8') as file:       # запись справочника в файл
        json.dump(s, file, indent=4, ensure_ascii=False)
    print('Запись добавлена')
