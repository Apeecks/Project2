from typing import Any

from src.work_vacancies import WorkVacancies


def test_work_vac(
    capsys: Any,
    obj1_work_vacancies: WorkVacancies,
    obj2_work_vacancies: WorkVacancies,
    obj3_work_vacancies: WorkVacancies,
) -> Any:
    print(obj3_work_vacancies)
    c = capsys.readouterr()
    assert c.out == "Разработчик, Сочи, от 3 до 5, Зарплата не указанна\n"

    print(repr(obj3_work_vacancies))
    c = capsys.readouterr()
    assert c.out == "WorkVacancies(Разработчик, Зарплата не указанна, Сочи, 02.02.2000, от 3 до 5, url)\n"

    assert WorkVacancies.salary_range(50) == [obj1_work_vacancies]
    assert WorkVacancies.city_sort("Москва") == [obj1_work_vacancies]
    assert WorkVacancies.experience_not() == [obj1_work_vacancies, obj2_work_vacancies]
