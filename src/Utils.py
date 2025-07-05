import json
from json import JSONDecodeError
from typing import Any

from src.Abstract import AbstractUtils


class Utils(AbstractUtils):

    @staticmethod
    def json_dump(info: list, filename: str) -> Any:
        """
        Сохранение вакансий в json файл, без дубликата
        """
        if filename == "data/vacancies.json":
            list_json_file = Utils.json_load(filename)

            new_sort_list = [x for x in info if x not in list_json_file]

            with open(filename, "w", encoding="utf-8") as f:
                list_json_file.extend(new_sort_list)
                json.dump(list_json_file, f, indent=4, ensure_ascii=False)

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(info, f, indent=4, ensure_ascii=False)

    @staticmethod
    def json_load(filename: str) -> Any:
        """
        Возвращает данные из файла
        """
        try:
            with open(filename, encoding="utf-8") as f:
                result = json.load(f)
                return result
        except JSONDecodeError:
            return []

    @staticmethod
    def json_remove(filename: str) -> Any:
        with open(filename, "w"):
            pass
