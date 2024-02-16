from validation import *
from classes import *


if __name__ == "__main__":
    with open('Phonebook.json', encoding='utf-8') as file:  # загрузка справочника
        all_lines: list[dict] = json.load(file)
    all_notes: list[PhoneNote] = [PhoneNote(line) for line in all_lines]
    while True:
        while True:
            command: int = validation_int(input("""Доступные команды справочника:
            Вывести весь справочник постранично -  1
            Вывести нужную страницу справочника  - 2
            Добавить запись -  3
            Редактировать запись -  4
            Найти запись(и) -  5      

            Введите команду(цифра от 1 до 5)   """))

            if command in range(1, 6):
                break
            else:
                print('Введена некорректная команда')
        match command:
            case 1 | 2:  # печать справочника постранично
                if command == 1:
                    page_count: int = len(all_notes) // 10
                    for page_number in range(1, page_count + 1):
                        page: Page = Page(all_notes=all_notes, page_number=page_number)
                        page.print_notes_from_page()
                elif command == 2:
                    page_number: int = validation_int(input('Введите номер нужной страницы от 1 до 10 '))
                    page: Page = Page(all_notes=all_notes, page_number=page_number)
                    page.print_notes_from_page()

            case 3:  # добавление записи
                note: PhoneNote = PhoneNote(validation_field(field_number=7))
                all_notes.append(note)
                PhoneNote.writing_sorted_phonebook(all_notes=all_notes)
                print('Запись добавлена')

            case 4:  # редактирование записи
                print('Запуск поиска записи для редактирования')
                search_result: list = PhoneNote.search_note(all_notes=all_notes)
                if search_result:
                    if len(search_result) == 1:
                        note_for_change: PhoneNote = search_result[0]
                    else:
                        number_note_for_change: int = validation_int(input('Введите номер нужной записи '
                                                                           'для редактирования   '))
                        note_for_change: PhoneNote = search_result[number_note_for_change - 1]
                    change_field_number: int = validation_int(input(f'''Выберите поле, которое хотите отредактировать:
                    фамилию - введите 1
                    имя - введите 2
                    отчество - введите 3   
                    организацию - ввведите 4
                    рабочий телефон -  введите 5 
                    мобильный телефон - введите 6
                
                    Введите номер поля для редактирования(цифра от 1 до 6)   '''))
                    change_field_value: list = list(validation_field(field_number=change_field_number).values())[0]
                    list_attr: list = list(note_for_change.__dict__.keys())
                    setattr(note_for_change, list_attr[change_field_number - 1], change_field_value)
                    PhoneNote.writing_sorted_phonebook(all_notes=all_notes)
                    print('Запись отредактирована')

            case 5:  # поиск записей
                PhoneNote.search_note(all_notes=all_notes)

        continue_work: int = validation_int(input('''Закрыть справочник? - введите 1
Продолжить работу со справочником? - введите 2  '''))
        if continue_work == 1:
            print('Справочник закрыт')
            break
        else:
            continue
