import random as r
import json


if __name__ == "__main__":
    fields = dict()
    fields['names'] = ['Александр', 'Борис', 'Вадим', 'Станислав', 'Терентий']
    fields['surnames'] = ['Иванов', 'Смирнов', 'Кузнецов', 'Соколов', 'Морозов']
    fields['patronymic'] = ['Александрович', 'Анатольевич', 'Валерьевич', 'Иванович', 'Петрович']
    fields['work'] = ['Веритас', 'Гелион', 'Лесные жители', 'Цитрус', 'Чай и булочки']
    phonebook = [dict([('surname', r.choice(fields['surnames'])),  # создание 100 записей справочника
                       ('name', r.choice(fields['names'])),
                       ('patronymic', r.choice(fields['patronymic'])),
                       ('work', r.choice(fields['work'])),
                       ('work_number', ''.join([str(r.randint(11, 99)) + '-' for _ in '123']).rstrip('-')),
                       ('personal_number', '89' + ''.join([str(r.randint(0, 9)) for _ in range(9)]))]) for _ in
                 range(100)]

    phonebook.sort(key=lambda note: tuple(note.values()))          # сортировка справочника

    with open('Phonebook.json', 'w', encoding='utf8') as file:     # запись справочника в файл
        json.dump(phonebook, file, indent=4, ensure_ascii=False)
