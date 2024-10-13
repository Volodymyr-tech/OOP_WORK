import requests

from src.abstract_api import Parser


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 1}
        self.__vacancies = []

    def __api_conection(self):
        """Метод для проверки подключения API"""
        response = requests.get(self.__url)
        if response.status_code == 200:
            return "Подключение стабильно"
        else:
            raise ConnectionError(f"Ошибка {response.status_code}")

    def load_vacancies(self, keyword):
        """Метод получения Json ответа от апи HH"""
        print(self.__api_conection())
        self.__params["text"] = keyword
        while self.__params.get("page") != 20:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            vacancies = response.json()["items"]
            self.__vacancies.extend(vacancies)
            self.__params["page"] += 1

    @property
    def get_vacancies(self):
        """Геттер который возвращает список словарей с информацией о вакансиях"""
        return self.__vacancies
