# Тестовое задание
___
## Функционал и Выполненные доп.задания

#### Сайт доступен для тестирования - ......

+ Было выполнено основное задание 
+ Были сделаны все дополнительные задания

+ При запуске проекта, суперюзер создается автоматически
+ Дополнительно был написан docker-compose файл

```bash
git clone git@github.com:contiinue/test-task.git && cd test_task
```

#### Необходимо создать .env файл и добавить переменные окружения + вставить свои ключи от STRIPE
```
# Postgresql environments
POSTGRES_USER=postgres_user
POSTGRES_PASSWORD=postgres_password
POSTGRES_DB=postgres_db

# Django superuser
DJANGO_SUPERUSER_PASSWORD=test_password
DJANGO_SUPERUSER_EMAIL=root@root.com
DJANGO_SUPERUSER_USERNAME=root

# Django
DJANGO_SECRET_KEY='some_secret_key'

# Stripe
STRIPE_PUBLIC_KEY=
STRIPE_SECRET_KEY=
```

#### Запускаем проект
```
docker compose up --build 
```
