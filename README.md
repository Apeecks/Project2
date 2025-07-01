# Проект hh.ru
Проект подключается к hh.ru, получает вакансии и умеет работать с ними.

## Установка:
### 1. Копируем проект:
```
git clone https://github.com/Apeecks/Project2.git
```
### 2. Устанавливаем зависимости:
```
poetry install
```
## Тестирование
Проект покрыт тестами. Для их запуска выполните команду:
```commandline
pytest
```
```commandline
pytest --cov
```
## Описание и примеры работы функций:

### Class API(AbstractAPI)
#### __connect_api - подключается к любому api (по идее, должен), если реализовать доп методы.
#### load_data_vacancies - метод, который работает с hh.ru
### Class WorkVacancies
Работает с вакансиями
### Модуль auxiliary_func 
Вспомогательные функции
#### Функция для работы с пользователем: user_interaction
### Class Utils(AbstractUtils)
Методы для работы с файлами.