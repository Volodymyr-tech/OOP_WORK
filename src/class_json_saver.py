import os.path

from config import DATA_DIR
from src.abstract_file_methods import FileMethods
from src.class_vacancies import Vacancies
import json

class JsonSaver(FileMethods):
    '''Класс для сохранения и обработки информации о вакансиях в JSON-файл.'''

    def __init__(self, filename='vacancies.json'):
        '''Список для хранения экземпляров класса Vacancy'''
        self.vacancies = []

    def add_vacancy(self, vacancy: Vacancies):
        """Добавляем вакансию в список"""
        if len(self.vacancies) != 0:
            for vac in self.vacancies:
                if vac.url == vacancy.url:
                    print("Вакансия с таким URL уже существует.")
                    return  # Прекращаем выполнение метода, если дубликат найден

        self.vacancies.append(vacancy)

    def save_vacancy(self):
        """Сохраняем список вакансий в JSON файл"""
        json_file = os.path.join(DATA_DIR, 'vacancies.json')  # путь к файлу
        data = [{
            "name": vac.name,
            "url": vac.url,
            "salary": vac.salary,
            "requirement": vac.requirement
        } for vac in self.vacancies]  # преобразуем все объекты Vacancy в список словарей

        with open(json_file, 'w', encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def get_info(self):
        pass


    def delete_info(self):
        pass



if __name__ == '__main__':
    manager = JsonSaver()
    vacancy_list = Vacancies.get_list_vacancies()
    for vac in vacancy_list:
        manager.add_vacancy(vac)
    manager.save_vacancy()
# saver.add_vacancy(emp)
# saver.add_vacancy(emp2)
# saver.add_vacancy(emp3)

# print(saver.vacancies)