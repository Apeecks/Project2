import logging
import os
from typing import Any

import requests
from dotenv import load_dotenv

from src.Abstract import AbstractAPI
from src.auxiliary_func import add_vacancies_sort_file_json

logger = logging.getLogger("API")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/API.log")
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


class API(AbstractAPI):
    def __init__(self, url: str, api_key_name: str, params: dict, result: list):
        super().__init__(url, api_key_name, params)
        self.__url = url
        self.__api_key_name = api_key_name
        self.__params = params
        self.result = result

    def _connect_api(self) -> Any:
        """
        Подключение к api
        """
        load_dotenv()
        api_key = os.getenv(self.api_key_name)
        headers = {"apikey": api_key}
        result_json = requests.get(self.url, headers=headers, params=self.params)
        if result_json.status_code == 200:
            return result_json.json()["items"]
        else:
            return f"Ошибка. Status_code: {result_json.status_code}"

    def load_data_vacancies(self, keyword: str, filename: str = "data/vacancies.json") -> Any:
        """
        Получение вакансий hh.ru
        """
        logger.info("Вакансии загружаются")
        self.params["text"] = keyword
        result_json = self._connect_api()
        while self.params.get("page") != 1:
            logger.info(f"Загружается страница: {self.params['page'] + 1}")
            if type(result_json) is str:
                return result_json
            else:
                self.result.extend(result_json)
                self.params["page"] += 1
        logger.info("Вакансии загрузились")
        result = add_vacancies_sort_file_json(self.result, filename)
        return result
