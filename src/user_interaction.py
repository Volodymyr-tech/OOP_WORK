from src.class_json_saver import JsonSaver
from src.class_api import HH
from src.class_vacancies import Vacancies

class UserInteraction:
    def __init__(self):
        self.api = HH()  # Инициализируем класс для работы с API
        self.saver = JsonSaver()  # Инициализируем класс для сохранения данных

    def search_vacancies(self):
        """Запрашиваем ключевое слово у пользователя и ищем вакансии"""
        keyword = input("Введите ключевое слово для поиска вакансий: ")
        self.api.load_vacancies(keyword)
        vacancies = self.api.get_vacancies  # Получаем список вакансий
        vacancy_objects = Vacancies.get_list_vacancies(vacancies)  # Преобразуем в объекты класса Vacancies
        self.saver.add_vacancy(vacancy_objects)  # Сохраняем вакансии
        print(f"Найдено и сохранено {len(vacancy_objects)} вакансий.")

    def show_vacancies(self):
        """Показываем вакансии по фильтру"""
        keyword = input("Введите ключевое слово для фильтра вакансий: ")
        result = self.saver.get_info(keyword)
        print(result)

    def delete_vacancy(self):
        """Удаляем вакансию по URL"""
        url = input("Введите URL вакансии, которую нужно удалить: ")
        self.saver.delete_info(url)
        print("Вакансия удалена.")
