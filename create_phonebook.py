import random as r
import json


def create_phonebook():
    names = ['Александр', 'Алексей', 'Борис', 'Вадим', 'Станислав', 'Терентий', 'Тимофей', 'Федор', 'Яков']
    names.sort()
    surnames = ['Иванов', 'Смирнов', 'Кузнецов', 'Попов', 'Васильев', 'Михайлов', 'Петров', 'Соколов', 'Морозов']
    surnames.sort()
    patronymic = ['Александрович', 'Анатольевич', 'Валерьевич', 'Иванович', 'Петрович']
    patronymic.sort()
    work = ['Веритас', 'Гелион', 'Едим вкусно', 'Лесные жители', 'Пчела и мед', 'Цитрус', 'Чай и булочки']
    work.sort()

    phonebook = [dict([('surname', r.choice(surnames)), ('name', r.choice(names)), ('patronymic', r.choice(patronymic)),
                       ('work', r.choice(work)),
                       ('work_number', ''.join([str(r.randint(11, 99)) + '-' for _ in '123']).rstrip('-')),
                       ('personal_number', '89' + ''.join([str(r.randint(0, 9)) for _ in range(9)]))]) for _ in
                 range(100)]
    # рандомное наполнение справочника на 100 записей из списков

    phonebook = sorted(phonebook, key=lambda x: tuple(x.values()))  # сортировка справочника

    with open('Phonebook.json', 'w', encoding='utf8') as file:  # запись справочника в файл
        json.dump(phonebook, file, indent=4, ensure_ascii=False)
