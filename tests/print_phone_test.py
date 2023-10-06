import unittest
from Phonebook.print_functions import print_phone


class PrintPhoneTestCase(unittest.TestCase):
    """Тесты для функции print_phone"""

    def test_print_phone(self):
        """Параметры вида  {"surname": "Алексеев", "name": "Александр", "patronymic": "Анатольевич",
           "work": "Гелион", "work_number": "23-87-25", "personal_number": "89766913916"}, 1 работают правильно?"""
        a = print_phone({"surname": "Алексеев", "name": "Александр", "patronymic": "Анатольевич", "work": "Гелион", "work_number": "23-87-25", "personal_number": "89766913916"}, 1)
        self.assertEqual(print(a), print('1 Алексеев Александр Анатольевич, организация: Гелион, раб.тел.: 23-87-25, моб.тел.: 89766913916'))

if __name__ == '__main__':
    unittest.main()
