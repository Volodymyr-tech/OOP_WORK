from src.class_api import HH

class Vacancies():
    '''Класс для работы с вакансиями получеными с хедхантера'''
    def __init__(self, name, url, salary, requirement):
        self.name = name
        self.url = url
        self.salary = salary
        self.requirement = requirement
        # if self.url is None:
        #     raise ValueError(f"URL не может быть None для вакансии: {self.name}")
        # print(f'Создан объект вакансии: {self.name} с URL: {self.url}')


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
        return (f'{self.name}, link:{self.url}\n'
                f'Salary:{self.salary},{self.requirement}')

    def __eq__(self, other):
        if isinstance(other, Vacancies):
            return self.url == other.url  # Сравниваем объекты только по URL
        return False

    def __hash__(self):
        return hash(self.url)

    # @staticmethod
    # def validation(salary):
    #     if salary is None:
    #         return

        # validated_vacancy = []
        # for vac in vacancies_list:
        #     if vac.salary == "Зарплата не указана":
        #         continue  # Пропустить вакансию, если зарплата не указана
        #     validated_vacancy.append(vac)
        # return validated_vacancy

    # def compare(self):
    #     pass


# if __name__ == '__main__':
#     data = Vacancies("Python Developer", "<https://hh.ru/vacancy/123456>", None, "Требования: опыт работы от 3 лет...")
#     print(repr(data))
#     obj_list = data.get_list_vacancies()
#     print(obj_list)

