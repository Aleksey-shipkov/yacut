# YaCut

Это проект создающий короткие ссылки на веб-ресурcы.
Проект создан с применением фреймворка Flask и SQLAlchemy.
Доступ осуществляется через веб-сайт или посредством API.
Спецификация API находится в файле openapi.yml

## Как установить программу

Клонировать репозиторий и перейти в него в командной строке:

```
git clone 
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Запустить программу:

```
flask run
```
