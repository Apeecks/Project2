from typing import Any, Union


class WorkVacancies:
    """
    Класс для работы с вакансиями
    """

    list_vacancies: list = []
    __slots__ = ("name", "salary", "city", "published_at", "experience", "alternate_url")

    def __init__(
        self, name: str, salary: Union[dict, str], city: str, published_at: str, experience: str, alternate_url: str
    ):
        self.name = name
        self.salary = salary
        self.city = city
        self.published_at = published_at
        self.experience = experience
        self.alternate_url = alternate_url

        self.__data_validation()
        WorkVacancies.list_vacancies.append(self)

    def __str__(self) -> str:
        return f"{self.name}, {self.city}, {self.experience}, {self.salary}"

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}({self.name}, {self.salary}, {self.city},"
            f" {self.published_at}, {self.experience}, {self.alternate_url})"
        )

    def __gt__(self, other: Any) -> Any:
        try:
            return self > other
        except TypeError:
            if self.salary and other.salary is str:
                return self == other
            if type(self.salary) is str:
                return other > self
            elif type(other.salary) is str:
                return self > other

    def __data_validation(self) -> Any:
        """
        Проверка данных
        """
        pass

    @staticmethod
    def salary_range(min_salary: int) -> list:
        """
        Сравнивает параметры salary
        """
        list_sort = [vac for vac in WorkVacancies.list_vacancies if type(vac.salary) is dict]
        if min_salary == 0:
            return WorkVacancies.list_vacancies
        else:
            return [vac_sort for vac_sort in list_sort if vac_sort.salary["from"] > min_salary]

    @staticmethod
    def city_sort(city: str) -> list:
        """
        Сортирует данные по городу
        """
        return [vac for vac in WorkVacancies.list_vacancies if vac.city == city]

    @staticmethod
    def experience_not() -> Any:
        """
        Сортирует данные по городу
        """
        return [vac for vac in WorkVacancies.list_vacancies if vac.experience == "Нет опыта"]
