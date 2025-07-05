import json
from json import JSONDecodeError
from typing import Any

from src.Abstract import AbstractUtils


class Utils(AbstractUtils):

    def __init__(self, filename: str = "filename.txt"):
        self.__filename = filename

    def json_dump(self, info: list) -> Any:
        """
        Сохранение вакансий в json файл, без дубликата
        """
        try:
            existing_data = self.json_load()
        except FileNotFoundError:
            existing_data = []

        new_data = [item for item in info if item not in existing_data]
        existing_data.extend(new_data)

        with open(self.__filename, "w", encoding="utf-8") as f:
            json.dump(existing_data, f, indent=4, ensure_ascii=False)

    def json_load(self) -> Any:
        """
        Возвращает данные из файла
        """
        try:
            with open(self.__filename, encoding="utf-8") as f:
                result = json.load(f)
                return result
        except JSONDecodeError:
            return []

    def json_remove(self) -> Any:
        with open(self.__filename, "w"):
            pass
