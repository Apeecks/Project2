import os
from typing import Any
from unittest.mock import patch

from src.auxiliary_func import add_obj_work_vacancies, user_interaction
from src.work_vacancies import WorkVacancies


def test_add_obj(capsys: Any, add_obj_test: Any) -> Any:
    add_obj_work_vacancies(add_obj_test)

    print(WorkVacancies.list_vacancies)
    c = capsys.readouterr()
    assert c.out == (
        "[WorkVacancies(QA Engineer, Зарплата не указанна, Алматы, 20.05.2025, От 1 года до 3 лет, url), "
        "WorkVacancies(Python Developer, Зарплата не указанна, Брест, 13.05.2025, No, url)]\n"
    )


@patch("src.API.API._connect_api")
@patch("builtins.input")
def test_user_interaction(mock_input: Any, mock_connect_api: Any, capsys: Any) -> Any:
    mock_input.side_effect = ["test", "список", "hh.ru", "3", "test", "y", "50", "Москва"]

    mock_connect_api.return_value = [
        {
            "name": "test1",
            "salary": {"from": 1, "to": 2},
            "area": {"name": "Алматы"},
            "published_at": "2000-02-02",
            "experience": {"name": "От 1 года до 3 лет"},
            "alternate_url": "url",
        },
        {
            "name": "test2",
            "salary": None,
            "area": {"name": "Москва"},
            "published_at": "2000-02-02",
            "experience": {"name": "No"},
            "alternate_url": "url",
        },
        {
            "name": "test3",
            "salary": {"from": 100, "to": 200},
            "area": {"name": "Екб"},
            "published_at": "2000-02-02",
            "experience": {"name": "No"},
            "alternate_url": "url",
        },
    ]
    user_interaction()
    c = capsys.readouterr()
    assert c.out == (
        "['hh.ru']\n"
        "\nФайл успешно создан со всеми вакансиями\n\n"
        "[WorkVacancies(test3, {'from': 100, 'to': 200}, Екб, 02.02.2000, No, url)]\n"
        "[WorkVacancies(test2, Зарплата не указанна, Москва, 02.02.2000, No, url)]\n"
    )

    # Тесты Utils
    from src.auxiliary_func import add_vacancies_sort_file_json
    from src.Utils import Utils

    # Utils.json_dump создается в test_user_interaction

    utils_filename = Utils("data/test.json")
    result = utils_filename.json_load()
    print(result)
    c = capsys.readouterr()
    assert c.out == f"{add_vacancies_sort_file_json(mock_connect_api.return_value, 'data/test.json')}\n"

    result = utils_filename.json_remove()
    print(result)
    c = capsys.readouterr()
    assert c.out == "None\n"

    os.remove("data/test.json")
