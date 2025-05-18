from abc import ABC, abstractmethod
from typing import Any


class AbstractAPI(ABC):

    def __init__(self, url: str, api_key_name: str, params: dict):
        self.url = url
        self.api_key_name = api_key_name
        self.params = params

    @abstractmethod
    def load_vacancies(self, keyword: str) -> Any:
        pass


class AbstractUtils(ABC):

    @staticmethod
    @abstractmethod
    def json_load_file(info):
        pass
