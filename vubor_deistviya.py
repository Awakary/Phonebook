import json


def vubor():
    while True:
        command = input('''Доступные команды справочника: 
                           Вывести весь справочник постранично -  1
                           Вывести нужную страницу справочника  - 2
                           Добавить запись -  3
                           Редактировать запись -  4
                           Найти запись(и) -  5
                           Введите цифру: ''')

        if command in ('1', '2', '3', '4', '5'):
            break
        else:
            print('Введена некорректная команда')
    return int(command)


def pechat(spravocnik: list):  # функция на вывод постранично справочника
    if command == 1:
        for i in range(10):
            a = spravocnik[i * 10: i * 10 + 10]  # переменная для отбора 10 записей на каждой странице
            for e, v in enumerate(a, i * 10 + 1):
                print(
                    f'''{e} {v['surname']} {v['name']} {v['otchestvo']}, организация: {v['rabota']}, раб.тел.: {v['work_number']}, 1моб.тел.: {v['personal_number']}''')
            print(f'Cтраницa {i + 1}')  # печать номера страницы

            while True:
                vopros = input('Вывести следующую страницу? Да - введите 1, Нет - введите 2 ')  # перелистывание страниц
                if vopros in ('1', '2'):
                    break
                else:
                    print('Некорректный ввод')
            if vopros == '1':
                continue
            else:
                break

    if command == 2:
        page = input('Введите номер страницы (от 1 до 100) ')  # вывод нужной страницы по номеру
        nomer = int(page) * 10  # определение нужных записей для введенного номера страницы
        for e, v in enumerate(spravocnik[nomer - 10: nomer], nomer - 9):
            print(
                f'''{e} {v['surname']} {v['name']} {v['otchestvo']}, организация: {v['rabota']}, раб.тел.: {v['work_number']}, моб.тел.: {v['personal_number']}''')
        print(f'Cтраницa {page}')


def add_zapis(s: list):  # функция добавления записи со всеми проверками на правильность введенных данных
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
            d['otchestvo'] = a.capitalize()
            break
        else:
            print('Отчество должно состоять только из букв')

    d['rabota'] = input('Введите пожалуйста организацию: ').capitalize()

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

    s.append(d)  # добавление записи в список справочника
    s = sorted(s, key=lambda x: tuple(x.values()))  # сортировка всего справочника

    with open('Spravochnik.json', 'w', encoding='utf8') as file:  # запись справочника в файл
        json.dump(s, file, indent=4, ensure_ascii=False)
    print('Запись добавлена')


def redakt(s: list):  # фунция по редактированию записи
    while True:
        h = {}
        a = input(
            'Введите пожалуйста ФИО буквами через пробел: ')  # при некорректно введенных данных появится сообщение, что нет записи, поэтому не стала добавлять проверки
        if a.replace(' ', '').isalpha() and a.count(' ') == 2:
            d = [i.capitalize() for i in a.split()]
            h = {'surname': d[0], 'name': d[1], 'otchestvo': d[2]}

        flag = True  # переменная сменит значение на False, когда нужная запись будет найдена

        for i in range(len(s)):
            if list(h.values()) == list(s[i].values())[:3]:
                flag = False
                print(
                    f'''{s[i]['surname']} {s[i]['name']} {s[i]['otchestvo']}, организация: {s[i]['rabota']}, раб.тел.: {s[i]['work_number']}, моб.тел.: {s[i]['personal_number']}''')

                q = input('''Выберите, что хотите отредактировать:
                             организацию - ввведите 1
                             рабочий телефон -  введите 2 
                             мобильный телефон - введите 3
                             ''')

                if q == '1':
                    s[i]['rabota'] = input('Введите новую организацию: ')

                if q == '2':
                    s[i]['work_number'] = input('Введите новый рабочий телефон в формате XX-XX-XX: ')

                if q == '3':
                    s[i]['personal_number'] = input('Введите новый мобильный телефон в формате 89XXXXXXXXX: ')

        if flag:
            print(
                'Нет такого человека в справочнике')  # если значение переменной не сменилось, значит такой записи не было найдено
        else:
            break
    with open('Spravochnik.json', 'w', encoding='utf8') as file:  # запись справочника в файл
        json.dump(s, file, indent=4, ensure_ascii=False)
    print('Запись отредактирована')


def poisk(spr: list):  # фунция поиска записей по справочнику
    f = input('''Поиск записей
              По односу критерию - введите 1 
              По нескольким критериям - введите 2  
              ''')
    flag = True
    if f == '1':  # запуск поиска по одному критерию
        a = input('Введите один критерий (фамилию, имя или др.) ')
        for i in spr:
            if a.capitalize() in i.values():  # поиск введенного параметра в значениях словарей
                print(
                    f'''{i['surname']} {i['name']} {i['otchestvo']}, организация: {i['rabota']}, раб.тел.: {i['work_number']}, моб.тел.: {i['personal_number']}''')
                flag = False

    if f == '2':  # запуск поиска по нескольким критериям
        a = input('Введите несколько критериев через пробел(фамилия, имя и др.) ')
        a = a.split()
        for i in spr:
            d = []
            for j in a:
                d.append(j.capitalize() in i.values())
            if all(d):  # поиск введенных параметров в значениях словарей(all проверяет соотвествие всем введенным параметрам)
                print(
                    f'''{i['surname']} {i['name']} {i['otchestvo']}, организация: {i['rabota']}, раб.тел.: {i['work_number']}, моб.тел.: {i['personal_number']}''')
                flag = False
    if flag:
        print('Нет записей, соответствующих данному критерию')


# основная программа

while True:
    with open('Spravochnik.json', encoding='utf-8') as file:  # загрузка справочника
        spr = json.load(file)

    command = vubor()  # пользоватеь выбирает команду
    if command in (1, 2):  # запуск соответствующей функции по команде
        pechat(spr)
    elif command == 3:
        add_zapis(spr)
    elif command == 4:
        redakt(spr)
    elif command == 5:
        poisk(spr)
    answer = input('''Закрыть справочник? Да - 1, Продолжить работу со справочником - 2 ''')
    if answer == '1':
        print('Справочник закрыт')
        break
    else:
        continue
