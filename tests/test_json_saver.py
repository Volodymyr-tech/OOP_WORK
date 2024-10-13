from src.class_json_saver import JsonSaver
from src.class_vacancies import Vacancies
from unittest.mock import patch


def test_json_saver_add_vacancy():
    emp1 = Vacancies("Go Developer", "https://hh.ru/vacancy/1222456", "0 -150 000 руб.",
                     "Требования: опыт работы от 2 лет...")
    emp2 = Vacancies("Java Script", "https://hh.ru/vacancy/60003", "200 000-150 000 руб.",
                     "Требования: опыт работы от 12 лет...")
    emp3 = Vacancies("Node.js Developer", "https://hh.ru/vacancy/7654", "250 000 руб.",
                     "Требования: опыт работы от 10 лет...")
    emp4 = Vacancies("Data Science", "https://hh.ru/vacancy/123654", "500 000 руб.",
                     "Требования: опыт работы от 10 лет...")
    emp5 = Vacancies(" Science", "https://hh.ru/vacancy/3654", "500 000 руб.",
                     "Требования: опыт работы от 10 лет...")
    # Создаем экземпляр класса JsonSaver
    saver = JsonSaver()
    listado = [emp1, emp2, emp3, emp4]
    saver.add_vacancy(listado)
    saver.add_vacancy(emp5)
    assert