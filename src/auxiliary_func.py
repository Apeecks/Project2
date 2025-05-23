from typing import Any

from src.Utils import Utils
from src.work_vacancies import WorkVacancies


def api_name(name_api: str, per_page: int) -> Any:
    from src.API import API

    if name_api == "hh.ru":
        return API("https://api.hh.ru/vacancies", "api_head_h", {"text": "", "page": 0, "per_page": per_page}, [])


def get_date(data: str) -> str:
    """Изменение формата даты"""
    if data == "":
        raise ValueError("Неверный формат")
    elif data[4] != "-":
        raise ValueError("Неверный формат")
    elif data[7] != "-":
        raise ValueError("Неверный формат")

    data_t = [data[8:10], data[5:7], data[0:4]]

    return ".".join(data_t)


def add_vacancies_sort_file_json(list_dict_vacancies: list, filename: str) -> list:
    """
    Отбирает данные из json ответа hh.ru
    """
    list_dict_sort = []
    for x in list_dict_vacancies:
        if x["salary"] is not None:
            dict_vacancies = {
                "name": x["name"],
                "salary": {"from": x["salary"]["from"], "to": x["salary"]["to"]},
                "city": x["area"]["name"],
                "published_at": get_date(x["published_at"]),
                "experience": x["experience"]["name"],
                "alternate_url": x["alternate_url"],
            }
            list_dict_sort.append(dict_vacancies)
        else:
            dict_vacancies = {
                "name": x["name"],
                "salary": "Зарплата не указанна",
                "city": x["area"]["name"],
                "published_at": get_date(x["published_at"]),
                "experience": x["experience"]["name"],
                "alternate_url": x["alternate_url"],
            }
            list_dict_sort.append(dict_vacancies)
    Utils.json_dump(list_dict_sort, filename)
    return list_dict_sort


def add_obj_work_vacancies(list_dict_vacancies: list) -> Any:
    """
    Отбирает данные из json ответа hh.ru
    """
    for x in list_dict_vacancies:
        name = x["name"]
        if type(x["salary"]) is dict:
            salary = {"from": x["salary"]["from"], "to": x["salary"]["to"]}
        else:
            salary = x["salary"]
        city = x["city"]
        published_at = x["published_at"]
        experience = x["experience"]
        alternate_url = x["alternate_url"]
        WorkVacancies(name, salary, city, published_at, experience, alternate_url)


def user_interaction() -> Any:
    filename_user = input(
        "В какой файл хотите сохранить данные? Файл по умолчанию vacancies,\n"
        " нажмите Enter, для сохранения в него: "
    )
    if filename_user != "":
        filename_user = f"data/{filename_user}.json"
        with open(filename_user, "w"):
            pass
    else:
        filename_user = "data/vacancies.json"

    list_api_serves = ["hh.ru"]
    while True:
        platforms = input('Какой сервис хотите использовать?\nДля получения списка сервисов напишите: "список": ')
        if platforms == "список":
            print(list_api_serves)
        elif platforms == "hh.ru":
            break
        else:
            print("Такого сервиса нет, попробуйте повторить ввод\n")

    while True:
        per_page = int(input("Введите количество вакансий для вывода в топ N: "))
        if type(per_page) is int:
            hh = api_name(platforms, per_page)
            break
        else:
            print("Вы ввели не числовое значение")

    keyword = input("Введите ключевое слово для фильтрации вакансий: ").lower()
    hh_load = hh.load_data_vacancies(keyword, filename_user)

    print("\nФайл успешно создан со всеми вакансиями\n")

    sort_data = input("Хотите отсортировать и вывести данные по зарплате? y/n: ")
    if sort_data == "y":
        add_obj_work_vacancies(hh_load)
        salary_range = int(input("Введите минимальную з\\п или, если хотите посмотреть все вакансии, введите 0: "))
        sort_list_user = WorkVacancies.salary_range(salary_range)
        print(sort_list_user)

    city_sort = input('Введите город, если не хотите сортировать по городу нажмите "n": ')
    if city_sort != "n":
        sort_list_user = WorkVacancies.city_sort(city_sort)
        print(sort_list_user)
