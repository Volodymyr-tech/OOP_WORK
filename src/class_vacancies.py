from src.class_api import HH

class Vacancies():
    '''Класс для работы с вакансиями получеными с хедхантера'''
    def __init__(self, name, url, salary, requirement):
        self.__name = name
        self.__url = url
        self.__salary = salary if salary else 0
        self.__requirement = requirement

    @classmethod
    def get_list_vacancies(cls):
        '''Класс-метод для создания списка объектов класса Vacancy'''
        vacancies = HH()
        vacancies.load_vacancies('Python')
        vacancies = vacancies.get_vacancies

        vacancies_list = [
            cls(
                name=vac.get("name", "Нет названия"),
                url=vac.get("alternate_url", "Нет URL"),
                salary=(
            f'Зарплата от '
            f'{vac["salary"].get("from") if vac["salary"].get("from") is not None else 0} до '
            f'{vac["salary"].get("to", "Зарплата не указана") if vac["salary"].get("to") is not None else "'Верхний предел не указан'"} '
            f'{vac["salary"].get("currency", "Валюта не указана")}'
            if vac["salary"] is not None else "Зарплата не указана"
            ),
                requirement=vac.get('snippet', {}).get('requirement', "нет описания")
            ) for vac in vacancies
        ]

        return vacancies_list


    def __repr__(self):
        return (f'{self.__name}, link:{self.__url}\n'
                f'Salary:{self.__salary},{self.__requirement}')


    # def validation(self, vacancies_list):
    #     validated_vacancy = []
    #     for vac in vacancies_list:
    #         if vac.salary == "Зарплата не указана":
    #             continue  # Пропустить вакансию, если зарплата не указана
    #         validated_vacancy.append(vac)
    #     return validated_vacancy

    # def compare(self):
    #     pass


if __name__ == '__main__':
    data = Vacancies("Python Developer", "<https://hh.ru/vacancy/123456>", None, "Требования: опыт работы от 3 лет...")
    print(repr(data))
    obj_list = data.get_list_vacancies()
    print(obj_list)

