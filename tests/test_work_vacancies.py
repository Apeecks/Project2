from typing import Any

from src.work_vacancies import WorkVacancies


def test_work_vacancies(capsys: Any) -> Any:
    obj = WorkVacancies("test_name1", {"from": 1}, "test_city", "test_data", "test", "test_url")
    assert obj.id == 1

    obj2 = WorkVacancies("test_name2", {"from": 2}, "test_city", "test_data", "test", "test_url")
    obj3 = WorkVacancies("test_name3", None, "test_city", "test_data", "test", "test_url")
    assert obj3.id == 3

    print(obj3)
    c = capsys.readouterr()
    assert c.out == "3: test_name3, Зарплата не указана, test_data\n"

    print(repr(obj3))
    c = capsys.readouterr()
    assert c.out == "WorkVacancies(test_name3, Зарплата не указана, test_city, test_data, test, test_url)\n"

    print(obj2 > obj)
    c = capsys.readouterr()
    assert c.out == "3: test_name2, 2, test_data зп больше\n"

    print(obj2 > obj3)
    c = capsys.readouterr()
    assert c.out == "Нечего сравнивать :)\n"
