
def print_phone(note, number=''):
    print(f'''{number} {note['surname']} {note['name']} {note['patronymic']}, организация: {note['work']},''', end='')
    return f''' раб.тел.: {note['work_number']}, моб.тел.: {note['personal_number']}'''


def print_pages(phonebook: list, pages):                      # функция на вывод постранично справочника
    if pages == 1:
        for i in range(10):
            first_note = phonebook[i * 10: i * 10 + 10]       # переменная для отбора 10 записей на каждой странице
            for e, v in enumerate(first_note, i * 10 + 1):
                print(print_phone(v, e))
            print(f'Cтраницa {i + 1}')                        # печать номера страницы

            while True:
                question = input('Вывести следующую страницу? Да - введите 1, Нет - введите 2 ')  # перелистывание
                if question in '12':
                    break
                else:
                    print('Некорректный ввод')
            if question == '1':
                continue
            else:
                break

    if pages == 2:
        page = input('Введите номер страницы (от 1 до 100) ')  # вывод нужной страницы по номеру
        page_number = int(page) * 10                      # определение нужных записей для введенного номера страницы
        for e, v in enumerate(phonebook[page_number - 10: page_number], page_number - 9):
            print(print_phone(v, e))
        print(f'Cтраницa {page}')
