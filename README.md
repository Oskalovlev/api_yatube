# API для соц. сети YaTube

### Ссылка на соц. сеть: https://github.com/Oskalovlev/hw05_final

## Технологии:
* Python - 3.7
* Django - 3.2
* Django REST Framework - 3.12.4
* Pillow - 9.3.0
##### P.S. Остальной стек в requirements.txt

### Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/Oskalovlev/api_yatube.git
```
```
cd api_yatube
```

### Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

### Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

### Миграции и запуск:
```
python manage.py migrate
```
```
python manage.py runserver
```

### Автор 
#### Оскалов Лев
