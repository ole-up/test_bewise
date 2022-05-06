# Тестовое задание BEWISE.AI
***
## Подготовка к сборке
Для запуска проекта необходим docker и docker-compose, процесс установки описан в официальной документации
[Install Docker Engine](https://docs.docker.com/engine/install/) и [Install Docker Compose](https://docs.docker.com/compose/install/).
Рекомендуемые версии Docker - 20.10.14, Docker Compose - 2.3.3.
## Сборка и запуск контейнеров
1. Скопируйте папку docker на сервер или свой компьютер
2. Настройте данные подключения к серверу баз данных (БД). 
- переименуйте файл docker/_env в .env и укажите в нем имя пользователя БД и пароль (POSTGRES_USER и POSTGRES_PASSWORD), 
 при необходимости можно изменить имя сервер БД (POSTGRES_SERVER), порт (POSTGRES_PORT) 
 и название самой базы данных (POSTGRES_DB)
- эти же параметры необходимо изменить в docker/docker-compose.yml
- в файле wait-for-postgres.sh так же нужно указать в 7 строке пользователя БД (параметр -U ), 
 его пароль (PGPASSWORD), имя БД (параметр -d)
Скрипт wait-for-postgres.sh необходим, согласно официальной документации Docker для устранения 
 проблемы одновременного запуска контейнера проекта и контейнера БД, т.к. серверу БД требуется 
 время для запуска [Control startup and shutdown order in Compose](https://docs.docker.com/compose/startup-order/)
3. Для сборки и запуска в папке docker выполните команду `sudo docker-compose up --build`. 
Выполнится сборка и запуск контейнеров
## Описание API и пример запроса
При успешном старте проекта описание API (swagger) доступно по адресу  [http://<адрес сервера>:8000](http://<адрес сервера>:8000), 
например [http://localhost:8000](http://localhost:8000). На этой странице есть пример запроса и возможность выполнить запрос к API.
