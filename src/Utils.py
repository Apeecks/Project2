from src.Abstract import AbstractUtils
import json

class Utils(AbstractUtils):


    @staticmethod
    def json_load_file(info):
        with open("data/vacancies.json", "w", encoding="utf-8") as f:
            json.dump(info, f, indent=4, ensure_ascii=False)