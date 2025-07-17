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
    def _connect_api(self) -> Any:
        pass

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

    @abstractmethod
    def json_dump(self, info: list) -> Any:
        """
        Загрузка данных в json файл
        """
        pass

    @abstractmethod
    def json_load(self) -> Any:
        """
        Загрузка данных из json файла
        """
        pass

    @abstractmethod
    def json_remove(self) -> Any:
        """
        Удаление данных из файла
        """
        pass
