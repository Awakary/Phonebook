import random as r
import json

names = ['Александр', 'Алексей', 'Борис', 'Вадим',
         'Валентин', 'Дмитрий', 'Евгений', 'Евдоким', 'Егор', 'Игорь',
         'Илья', 'Кирилл', 'Максим', 'Марк', 'Назар', 'Никита', 'Николай', 'Олег',
         'Павел', 'Петр', 'Руслан', 'Степан', 'Станислав', 'Терентий', 'Тимофей', 'Федор', 'Яков']

names.sort

surnames = ['Иванов', 'Смирнов', 'Кузнецов', 'Попов', 'Васильев', 'Михайлов', 'Петров', 'Соколов', 'Морозов',
            'Волков', 'Алексеев', 'Лебедев', 'Семенов', 'Егоров']
surnames.sort

otchestvo = ['Александрович', 'Анатольевич', 'Андреевич', 'Антонович', 'Борисович', 'Валентинович', 'Валерьевич',
             'Иванович', 'Петрович']
otchestvo.sort

rabota = ['Веритас', 'Гелион', 'Едим вкусно', 'Лесные жители', 'Пчела и мед', 'Цитрус', 'Чай и булочки']

rabota.sort

s = [dict([('surname', r.choice(surnames)), ('name', r.choice(names)), ('otchestvo', r.choice(otchestvo)),
           # рандомное наполнение справочника на 1000 записей из списков
           ('rabota', r.choice(rabota)),
           ('work_number', ''.join([str(r.randint(11, 99)) + '-' for i in '123']).rstrip('-')),
           ('personal_number', '89' + ''.join([str(r.randint(0, 9)) for t in range(9)]))]) for m in range(1000)]

s = sorted(s, key=lambda x: tuple(x.values()))  # сортировка справочника

with open('Spravochnik.json', 'w', encoding='utf8') as file:  # запись справочника в файл
    json.dump(s, file, indent=4, ensure_ascii=False)
