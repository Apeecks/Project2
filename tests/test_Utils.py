import json

from src.Utils import Utils


def test_utils():
    info = 'Hello, world!'
    Utils.json_load_file(info)

    with open('data/vacancies.json', encoding='utf-8') as f:
        file = json.load(f)
        assert file == 'Hello, world!'

