import os
from typing import Any
from unittest.mock import patch

from src.API import API


@patch("requests.get")
def test_load_data_vacancies(mock_get: Any, test_requests_json_hh: dict, test_result_load_data_vacancies: list) -> Any:
    test = API("https://test.com", "api_head_h", {"text": "test", "page": 0, "per_page": 1}, [])
    mock_get.return_value.json.return_value = test_requests_json_hh

    response = mock_get.return_value
    response.status_code = 200

    with open("data/test.json", "w"):
        pass

    assert test.load_data_vacancies("test", "data/test.json") == test_result_load_data_vacancies

    os.remove("data/test.json")
