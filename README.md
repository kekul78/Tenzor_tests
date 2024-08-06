# Tenzor testing 

## 1. Описание <a id=1></a>
Тесты написанные для проверки трёх сценариев. Автотесты реализованы на Python 3 и Selenium Webdriver. В качестве тестового framework используется pytest. Реализован паттерн PageObject. Настроено логирование автотестов.

Cтруктура репозитория:
```
Dev
 └── Tenzor_testis
     ├── pages
     │   ├── base_app.py          <- Файл с базовыми методами для работы с WebDriver
     │   └── pages.py             <- Файл с локаторами для веб страницы
     ├── tests
     │   ├── config.py            <- Файл с вспомогательными конфигурациями
     │   └── test_routes.py       <- Файл с тестами по трём сценариям
     ├── .gitignore
     ├── chromedriver_options.py  <- Файл с опциями для работы WebDriver
     ├── conftest.py              <- Файл с микстурами
     ├── pytest.ini               <- Файл с настройками pytest
     ├── README.md
     └── requirements.txt
```
---
## 2. Команды для локального запуска <a id=4></a>

Перед запуском необходимо склонировать проект:
```bash
git clone git@github.com:kekul78/Tenzor_tests.git

```

Cоздать и активировать виртуальное окружение:
```bash
Linux: python3 -m venv venv
Windows: python -m venv venv
```
```bash
Linux: source venv/bin/activate
Windows: source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:
```bash
python3 -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```

Запустить автотесты:
```bash
pytest
```
---
## Стек технологий

* Python 3.11.3,
* Pytest 8.3.2,
* Selenium 4.23.1

Автор: 
* [Канцулин Данил](https://github.com/kekul78)
