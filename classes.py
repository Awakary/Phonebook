import json
from validation import validation_int


class PhoneNote(object):

    """класс для записи в телефонном справочнике"""

    name: str
    surname: str
    patronymic: str
    work: str
    work_number: str
    personal_number: str

    def __init__(self, data: dict):

        """метод инициализации экземпляра класса PhoneNote и определения его атрибутов"""

        self.name = data['name']
        self.surname = data['surname']
        self.patronymic = data['patronymic']
        self.work = data['work']
        self.work_number = data['work_number']
        self.personal_number = data['personal_number']

    @staticmethod
    def search_note(all_notes: list) -> list | None:

        """метод поиска записи в справочнике по одному или нескольким критериям"""

        count_parameters: int = validation_int(input('''Поиск записей : По одному критерию - введите 1 
                По нескольким критериям - введите 2  '''))
        if count_parameters == 1:
            parameters: list[str] = [input(f'''Введите значение критерия для поиска (фамилия, имя и др.) ''')]
        else:
            parameters: list[str] = input(f'''Введите значения нескольких критериев для поиска '''
                                          f'''через запятую (фамилия, имя и др.) ''').split(',')
        flag: bool = False
        result: list = []
        for note in all_notes:
            if len(parameters) == 0:
                print('Не введены параметры поиска')
                return
            elif len(parameters) == 1:
                if any([parameter.strip().capitalize() in note.__dict__.values() for parameter in parameters]):
                    result.append(note)
                    flag = True
            else:
                if all(parameter.strip().capitalize() in note.__dict__.values() for parameter in parameters):
                    result.append(note)
                    flag = True

        if not flag:
            print('Нет записей, соответствующих данному критерию')
            return

        if result:
            for index, note in enumerate(result, 1):
                note.print_note(index=index)
        return result

    @staticmethod
    def writing_sorted_phonebook(all_notes: list) -> None:

        """метод сортировки записей и записи их в файл справочника"""

        all_notes: list = sorted(all_notes, key=lambda note: note)
        all_notes: list = [note.__dict__ for note in all_notes]
        with open('Phonebook.json', 'w', encoding='utf8') as file:  # запись справочника в файл
            json.dump(all_notes, file, indent=4, ensure_ascii=False)

    def print_note(self, index: int = None) -> None:

        """метод печати одной записи справочника"""

        print(f'''{index} {self.surname} {self.name} {self.patronymic}, организация: {self.work}, '''
              f'''раб.тел.: {self.work_number}, моб.тел.: {self.personal_number}''')

    def __lt__(self, other) -> bool:
        return self.surname < other.surname


class Page:

    """класс для одной страницы справочника"""

    page_number: int
    limit_notes: list

    def __init__(self, all_notes: list, page_number: int):

        """метод инициализации экземпляра класса Page и определения его атрибутов"""

        self.page_number = page_number
        if self.page_number * 10 <= len(all_notes):
            self.limit_notes = all_notes[(page_number - 1) * 10: page_number * 10]
        else:
            self.limit_notes = all_notes[(page_number - 1) * 10:]

    def print_notes_from_page(self) -> None:

        """метод печати всех записей со страницы"""

        for index, note in enumerate(self.limit_notes, 1):
            note.print_note(index=index)
        print(f'Cтраницa {self.page_number}')
