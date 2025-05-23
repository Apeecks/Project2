from typing import Any

import pytest

from src.work_vacancies import WorkVacancies


@pytest.fixture(autouse=True)
def clear_class_work() -> Any:
    WorkVacancies.list_vacancies.clear()
    try:
        yield
    finally:
        WorkVacancies.list_vacancies.clear()


@pytest.fixture
def test_requests_json_hh() -> dict:
    return {
        "items": [
            {
                "name": "test1_name",
                "salary": {"from": 10000, "to": 20000},
                "area": {"name": "test1_city"},
                "published_at": "2000-02-02",
                "experience": {"name": "test1_experience"},
                "alternate_url": "test1_alternate_url",
            }
        ]
    }


@pytest.fixture
def test_result_load_data_vacancies() -> list:
    return [
        {
            "name": "test1_name",
            "salary": {"from": 10000, "to": 20000},
            "city": "test1_city",
            "published_at": "02.02.2000",
            "experience": "test1_experience",
            "alternate_url": "test1_alternate_url",
        }
    ]


@pytest.fixture
def obj1_work_vacancies() -> WorkVacancies:
    return WorkVacancies("Разработчик", {"from": 100, "to": 200}, "Москва", "02.02.2000", "Нет опыта", "url")


@pytest.fixture
def obj2_work_vacancies() -> WorkVacancies:
    return WorkVacancies("Разработчик", {"from": 1, "to": 2}, "СПб", "02.02.2000", "Нет опыта", "url")


@pytest.fixture
def obj3_work_vacancies() -> WorkVacancies:
    return WorkVacancies("Разработчик", "Зарплата не указанна", "Сочи", "02.02.2000", "от 3 до 5", "url")


@pytest.fixture
def add_obj_test() -> list:
    return [
        {
            "name": "QA Engineer",
            "salary": "Зарплата не указанна",
            "city": "Алматы",
            "published_at": "20.05.2025",
            "experience": "От 1 года до 3 лет",
            "alternate_url": "url",
        },
        {
            "name": "Python Developer",
            "salary": "Зарплата не указанна",
            "city": "Брест",
            "published_at": "13.05.2025",
            "experience": "No",
            "alternate_url": "url",
        },
    ]


# @pytest.fixture
# def test_data_user() -> list:
#     return [
#     {
#         "name": "test1",
#         "salary": {'from': 1, 'to': 2},
#         "city": "Алматы",
#         "published_at": "20.05.2025",
#         "experience": "От 1 года до 3 лет",
#         "alternate_url": "url"
#     },
#     {
#         "name": "test2",
#         "salary": "Зарплата не указанна",
#         "city": "Москва",
#         "published_at": "13.05.2025",
#         "experience": "No",
#         "alternate_url": "url"
#     },
#     {
#         "name": "test3",
#         "salary": {'from': 100, 'to': 200},
#         "city": "Екатеринбург",
#         "published_at": "13.05.2025",
#         "experience": "No",
#         "alternate_url": "url"
#     }]
