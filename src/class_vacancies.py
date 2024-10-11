from src.class_api import HH

class Vacancies():
    '''Класс для работы с вакансиями получеными с хедхантера'''
    def __init__(self, name, url, salary, requirement):
        self.name = name
        self.url = url
        self.salary = salary
        self.requirement = requirement

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
                    f'Зарплата от {vac.get("salary", {}).get("from", 0)} до {vac.get("salary", {}).get("to", 0)} {vac.get("salary", {}).get("currency", "")}'
                    if vac.get("salary") else "Зарплата не указана"
                ),
                requirement=vac.get('snippet', {}).get('requirement', "нет описания")
            ) for vac in vacancies
        ]

        return vacancies_list  #список словарей с вакансиями на вход для создания объекта Vacancy


    def __repr__(self):
        return (f'{self.name}, link:{self.url}\n'
                f'Salary:{self.salary},{self.requirement}')


    # def validation(self):
    #     vacancies = HH().get_vacancies
    #     for vac in vacancies:
    #         if vac.get("salary") is True:



    def compare(self):
        pass


if __name__ == '__main__':
    data = Vacancies
    data.get_list_vacancies()
    print(data)