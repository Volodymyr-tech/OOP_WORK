from src.class_vacancies import Vacancies


def sort_vacancies_by_salary(vacancies: list[Vacancies]) -> list[Vacancies]:
    """
    Функция для сортировки вакансий по зарплате
    """
    by_salary = sorted(vacancies, key=lambda x: x.salary, reverse=True)
    return by_salary
