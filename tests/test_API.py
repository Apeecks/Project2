from typing import Any
from unittest.mock import patch

from src.API import API


@patch("requests.get")
def test_load_vacancies(mock_get: Any) -> Any:
    head_h = API("https://test.ru", "API_KEY", {"text": "", "page": 0}, [])
    mock_get.return_value.json.return_value = {"items": [{"test": "test"}, {"test": "test"}]}
    head_h.load_vacancies("test")
    assert head_h.result == [{"test": "test"}, {"test": "test"}]
