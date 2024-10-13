from src.class_api import HH
import re


class Vacancies():
    '''Класс для работы с вакансиями получеными с хедхантера'''
    __slots__ = ('name', 'url', 'salary', 'requirement')

    def __init__(self, name, url, salary, requirement):

        self.name = name
        self.url = url
        self.salary = salary
        self.requirement = requirement


    @classmethod
    def get_list_vacancies(cls, vacancies):
        '''Класс-метод для создания списка объектов класса Vacancy'''

        vacancies_list = [
            cls(
                name=vac.get("name", "Нет названия"),
                url=vac.get("alternate_url", "Нет URL"),
                salary=(
            f'Зарплата от '
            f'{vac["salary"].get("from") if vac["salary"].get("from") is not None else 0} до '
            f'{vac["salary"].get("to") if vac["salary"].get("to") is not None else "'Верхний предел не указан'"} '
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


    def _extract_numbers(self):
        """Извлекает все числа из строки"""

        numbers = re.findall(r'\d+', self.salary) # Получаем список зп

        # Преобразуем найденные строки в числа
        numbers = [int(num) for num in numbers]

        if len(numbers) == 1:
            return numbers[0], 0  # Если найдено одно число, считаем это минимальной зарплатой
        else:
            return numbers[0], numbers[-1]


    def _average_salary(self):
        salary = self._extract_numbers()
        if 0 in salary:
            average_salary = sum(salary)
            return average_salary
        else:
            average_salary = sum(salary)
            return average_salary / len(salary)

    def __le__(self, other):
        if not isinstance(other, Vacancies):
            raise TypeError("Операнд справа должен иметь тип Vacancy")
        else:
            return self._average_salary() <= other._average_salary()


    def __gt__(self, other):
        if not isinstance(other, Vacancies):
            raise TypeError("Операнд справа должен иметь тип Vacancy")
        else:
            return self._average_salary() > other._average_salary()


    def __ge__(self, other):
        if not isinstance(other, Vacancies):
            raise TypeError("Операнд справа должен иметь тип Vacancy")
        else:
            return self._average_salary() >= other._average_salary()