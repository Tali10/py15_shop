'''
pip install -r requirements.txt
pip freeze
django-admin startproject main - создает папку main/main
django-admin startproject main . - создает папку main
./manage.py startapp python15 - создаем приложение
./manage.py runserver - запуск сервера
./manage.py runserver 5000 - можно выставить порт самому
 ./manage.py makemigrations - создает миграцию
./manage.py migrate - применяем миграцию
./manage.py createsuperuser - создаем суперюзера
CREATE DATABASE python15; - создаем базу данных
CREATE USER python15 with password 'python15'; - создаем пользователя
GRANT ALL PRIVILEGES on DATABASE "python15" to python15; - задаем ему права

'''


'''
main
    asgi.py - управление потоками (синхронное, рассинхронное)
    settings.py
        DEBUG - если True, то видим ошибки. Если False, то не видим
        ROOT_URLCONF = 'main.urls' - все url будут хранится по этому пути main/url
    urls.py - храним ссылки нашего сайта
manage.py - все настройки при миграции хранятся тут

'''