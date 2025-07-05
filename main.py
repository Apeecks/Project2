from src.auxiliary_func import add_obj_work_vacancies, api_name, user_interaction
from src.Utils import Utils
from src.work_vacancies import WorkVacancies

# Класс API + auxiliary_func. Формирование запроса по сервису, кол-ом вакансий и слову
hh = api_name("hh.ru", 20)
hh_sort = hh.load_data_vacancies("Python")

# Создаем объекты класса WorkVacancies
add_obj_work_vacancies(hh_sort)

# Class WorkVacancies. Работа с вакансиями
for x in WorkVacancies.salary_range(100000):
    print(x)
print("\n")
for x in WorkVacancies.experience_not():
    print(x)
print("\n")
for x in WorkVacancies.city_sort("Москва"):
    print(x)
print("\n")
for x in WorkVacancies.list_vacancies:
    print(x)

Utils.json_remove("data/vacancies.json")

# Функция взаимодействия с пользователем
print("\n\n\n")
user_interaction()
