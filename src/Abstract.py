from abc import ABC, abstractmethod
from typing import Any


class AbstractAPI(ABC):
    """
    Абстрактный класс для работы с API
    """

    def __init__(self, url: str, api_key_name: str, params: dict):
        self.url = url
        self.api_key_name = api_key_name
        self.params = params

    @abstractmethod
    def load_data_vacancies(self, keyword: str, filename: str) -> Any:
        """
        Метод получения данных Api
        """
        pass


class AbstractUtils(ABC):
    """
    Абстрактный класс для работы с файлами
    """

    @staticmethod
    @abstractmethod
    def json_dump(info: list, filename: str) -> Any:
        """
        Загрузка данных в json файл
        """
        pass

    @staticmethod
    @abstractmethod
    def json_load(filename: str) -> Any:
        """
        Загрузка данных из json файла
        """
        pass

    @staticmethod
    @abstractmethod
    def json_remove(filename: str) -> Any:
        """
        Удаление данных из файла
        """
        pass
