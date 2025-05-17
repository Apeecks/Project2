from typing import Any, Union


class WorkVacancies:
    id = 0
    all_obj: dict = {}

    def __init__(
        self, name: str, salary: Union[dict, None], city: str, published_at: str, experience: str, alternate_url: str
    ):
        WorkVacancies.id += 1

        self.name = name
        if type(salary) is not dict:
            self.salary = "Зарплата не указана"
        else:
            self.salary = salary["from"]
        self.city = city
        self.published_at = published_at
        self.experience = experience
        self.alternate_url = alternate_url
        WorkVacancies.all_obj[WorkVacancies.id] = self

    def __str__(self) -> str:
        return f"{WorkVacancies.id}: {self.name}, {self.salary}, {self.published_at}"

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}({self.name}, {self.salary}, {self.city},"
            f" {self.published_at}, {self.experience}, {self.alternate_url})"
        )

    def __gt__(self, other: Any) -> str:
        try:
            if self.salary > other.salary:
                return f"{self} зп больше"
            else:
                return f"{other} зп больше"
        except TypeError:
            return "Нечего сравнивать :)"
