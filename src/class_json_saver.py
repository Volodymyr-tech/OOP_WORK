import os.path
import json

from config import DATA_DIR
from src.abstract_file_methods import FileMethods
from src.class_vacancies import Vacancies


class JsonSaver(FileMethods):
    '''Класс для сохранения и обработки информации о вакансиях в JSON-файл.'''

    def __init__(self, filename='vacancies.json'):
        self.filename = filename

    def add_vacancy(self, *args):
        '''Добавляем одну или несколько вакансий, если их нет в файле'''

        existing_vacancies = self.__open_file() # Получаем множество существующих вакансий

        new_vacancies = set() #Получаем множество

        for arg in args: # Обрабатываем каждый переданный аргумент
            if isinstance(arg, list):
                new_vacancies.update(arg)  # Добавляем все элементы списка в множество
            else:
                new_vacancies.add(arg)

        updated_vacancies = existing_vacancies.union(new_vacancies)# Объединяем новые и существующие вакансии с помощью union

        self.__save_vacancy(updated_vacancies) # преобразует вакансии в формат списка словарей.
        self.__write_to_file(updated_vacancies) # Пишем данные в файл

    def __save_vacancy(self, vacancies):
        """Преобразуем вакансии в список словарей для сохранения в JSON"""
        data = [{
            "name": vac.name,
            "url": vac.url,
            "salary": vac.salary,
            "requirement": vac.requirement
        } for vac in vacancies]
        return data


    def __write_to_file(self, vacancies):
        """Сохраняем список вакансий в JSON файл"""
        data = self.__save_vacancy(vacancies)   #Вызываем метод для получения списка словарей вакансий
        json_file = os.path.join(DATA_DIR, self.filename)
        with open(json_file, 'w', encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


    def __open_file(self):
        """Открываем файл JSON и возвращаем множество вакансий"""
        json_file = os.path.join(DATA_DIR, self.filename)

        # Если файл не существует, возвращаем пустое множество
        if not os.path.exists(json_file):
            return set()

        if os.path.getsize(json_file) == 0:
            return set()

        with open(json_file, 'r', encoding="utf-8") as file:
            vacancies_in_file = json.load(file)

        vacancies_set = {
            Vacancies(
                vac.get("name"),
                vac.get("url"),
                vac.get("salary"),
                vac.get("requirement")
            ) for vac in vacancies_in_file
        }

        return vacancies_set # Преобразуем данные в множество объектов класса Vacancies


    def get_info(self, filter):
        existing_vacancies = self.__open_file() # Получаем множество существующих вакансий
        for vacancy in existing_vacancies:
            name = vacancy.name
            if filter in name:
                return name  # Вакансии с ключевым словом по имени


    def delete_info(self, filter):
        existing_vacancies = self.__open_file()
        existing_vacancies.remove(filter)
        self.__save_vacancy(existing_vacancies)  # преобразует вакансии в формат списка словарей.
        self.__write_to_file(existing_vacancies)



# Пример использования
emp1 = Vacancies("Python Developer", "https://hh.ru/vacancy/123456", "100 000-150 000 руб.",
                 "Требования: опыт работы от 3 лет...")
emp2 = Vacancies("Java Developer", "https://hh.ru/vacancy/654123", "200 000-150 000 руб.",
                 "Требования: опыт работы от 12 лет...")
emp3 = Vacancies("C++ Developer", "https://hh.ru/vacancy/987654", "250 000 руб.",
                 "Требования: опыт работы от 10 лет...")
emp4 = Vacancies("C++ Developer", "https://hh.ru/vacancy/987654", "250 000 руб.",
                 "Требования: опыт работы от 10 лет...")
emp5 = Vacancies("GOGO Developer", "https://hh.ru/vacancy/9823423454", "250 000 руб.",
                 "Требования: опыт работы от 10 лет...")
emp6 = Vacancies("Python Developer", "https://hh.ru/vacancy/000000", "100 000-150 000 руб.",
                 "Требования: опыт работы от 3 лет...")
# Создаем экземпляр класса JsonSaver
saver = JsonSaver()
listado = [emp1, emp2, emp3, emp4, emp5, emp6]
saver.add_vacancy(listado)
saver.delete_info(emp2)




