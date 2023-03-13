# **Yatube_API**
___ 

### *Технологии*
- Python 3.7
- Django
- djangorestframework
- SQLite

___

## *Описание проекта*

Проект Yatube_API - API сервис для проекта [Yatube](https://github.com/Sergio7523/hw05_final)

Функционал проекта Yatube доступен через API, аутентификация пользователей осуществляется через JWT-токены.

После установки проекта полная документация к проекту доступна по адресу /redoc/
___
## Установка

Cоздать и активировать виртуальное окружение:
```sh
python -m venv env

source venv/scripts/activate
```

Установить зависимости из файла requirements.txt:
```sh
pip install -r requirements.txt
```
Выполнить миграции:
```sh
python manage.py migrate
```
Запустить проект:
```sh
python manage.py runserver
```
** Для установки на Linux и MacOs использовать команды python3 и source env/bin/activate
___
