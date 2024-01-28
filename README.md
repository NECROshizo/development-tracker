# Модуль: Трекер развития для Яндекса

## **Описание проекта**
Карьерный трекер – веб-сервис для аналитики пути студента в трудоустройстве с элементами соц.сети. Благодаря сервису студент может вести свой дневник, отмечая отклики на вакансии и соответствующие этапы прохождения. Также ему доступны партнерские вакансии и парсер вакансий, который собирает все релевантные предложения на рынке.

## Технологии:
- Python 3.10
- Django 4.1
- Django REST Framework 3.14
- PostgreSQL
- Djoser
- Nginx
- Qunicorn 20.1
- Docker
- Node.js 20 (LTS)

## Как запустить проект локально:

1. Клонирование проекта с GitHub на локальный компьютер
```
git clone git@github.com:development-tracker-practicum/development-tracker.git
```
2. В директории проекта перейдите в директорию infra/.
3. Создайте файл .env в директории infra/ и заполните его. Переменные для работы проекта перечислены в файле .env.example, находящемся в директории infra/.
3. Запустите в терминале контейнеры Docker внутри папки infra:
```
docker compose up
```
4. Выполните миграции в другом терминале:
```
docker compose exec backend python manage.py migrate
```
5. Создайте администратора:
```
docker compose exec backend python manage.py createsuperuser
```
6. Соберите статику backend:
```
docker compose exec backend python manage.py collectstatic
docker compose exec backend cp -r /app/static/. /static/
```
7. Перейдите на сайт:
```
https://localhost:8000/
```

### Авторы проекта:

Backend:
- [Anton Krasin](https://github.com/KrasinAD)
- [Peter Oganin](https://github.com/NECROshizo)

Frontend:
- [Sergey Gromov](https://github.com/LoONeyXx)
- [Pavel](https://github.com/rakleed)
