import json

from src.API import API
from src.work_vacancies import WorkVacancies

head_h = API("https://api.hh.ru/vacancies", "api_head_h", {"text": "", "page": 0, "per_page": 100}, [])

head_h.load_vacancies("Python")

with open("data/test.json", "w", encoding="utf-8") as f:
    json.dump(head_h.result, f, indent=4, ensure_ascii=False)


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


number_vac = 0
for x in head_h.result:
    name = x["name"]
    salary = x["salary"]
    city = x["area"]["name"]
    published_at = get_date(x["published_at"])
    experience = x["experience"]["name"]
    alternate_url = x["alternate_url"]
    number_vac += 1
    vacancies = WorkVacancies(name, salary, city, published_at, experience, alternate_url)
    if type(vacancies.salary) is str:
        continue
    elif vacancies.experience != "Нет опыта":
        continue
    else:
        print(WorkVacancies.all_obj[WorkVacancies.id])
        print(repr(WorkVacancies.all_obj[WorkVacancies.id]))
print(f"{number_vac}\n\n\n")

print(WorkVacancies.all_obj[18] > WorkVacancies.all_obj[39])
