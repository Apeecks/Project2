import logging
import os
from typing import Any

import requests
from dotenv import load_dotenv

from src.Abstract import AbstractAPI

logger = logging.getLogger("API")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/API.log")
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


class API(AbstractAPI):

    def __init__(self, url: str, api_key_name: str, params: dict, result: list):
        super().__init__(url, api_key_name, params)
        self.result = result

    def load_vacancies(self, keyword: str) -> Any:
        logger.info("Вакансии загружаются")
        self.params["text"] = keyword
        load_dotenv()
        api_key = os.getenv(self.api_key_name)
        headers = {"apikey": api_key}
        while self.params.get("page") != 1:
            logger.info(f"Загружается страница: {self.params['page'] + 1}")
            result_json = requests.get(self.url, headers=headers, params=self.params).json()["items"]
            self.result.extend(result_json)
            self.params["page"] += 1
        logger.info("Вакансии загрузились")
