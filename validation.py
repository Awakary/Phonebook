import re


def validation_field(field_number: int) -> dict:

    """функция считывания и проверки всех введенных полей для одной записи """

    data: dict = {}
    fields: list = ['surname', 'name', 'patronymic']
    fields_for_input: list = ['фамилию', 'имя', 'отчество']
    if field_number in (1, 2, 3, 7):
        count: int = 3 if field_number == 7 else 1
        for index in range(count):
            while True:
                if count == 3:
                    word: str = input(f'Введите пожалуйста {fields_for_input[index]}:  ')
                else:
                    word: str = input(f'Введите пожалуйста {fields_for_input[field_number - 1]}:  ')
                if word.isalpha():
                    data[fields[index]] = word.capitalize()
                    break
                else:
                    print('Введите пожалуйста буквами ')
    if field_number in (4, 7):
        data['work'] = input('Введите пожалуйста организацию: ').capitalize()
    if field_number in (5, 7):
        while True:
            phone: str = input(f'''Введите пожалуйста рабочий номер телефона в'''
                               f'''формате ХХ-ХХ-ХХ: (при отсутствии - введите нет)   ''')
            if re.fullmatch('(\d{2}-){2}\d{2}', phone) or phone == 'нет':
                data['work_number'] = phone
                break
            else:
                print('Неверный формат номера')
    if field_number in (6, 7):
        while True:
            mobile_phone: str = input(f'''Введите пожалуйста личный номер телефона в'''
                                      f'''формате 89ХХХХХХХХХ: (при отсутствии  - введите нет)   ''')
            if re.fullmatch('89\d{9}', mobile_phone) or mobile_phone == 'нет':
                data['personal_number'] = mobile_phone
                break
            else:
                print('Неверный формат номера')
    return data


def validation_int(number: str) -> int:

    """функция проверки введенных чисел и перевод в int"""

    while True:
        try:
            number: int = int(number)
            break
        except ValueError:
            number: str = input('Ввведите пожалуйста число ')
    return number
