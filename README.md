# Инструкция по запуску проекта Shop
## 1. Установка зависимостей
```bash
pip install django
pip install pillow
```
или 

```bash
pip install django pillow
```

## 2. Применение миграций

```bash
python manage.py migrate
```

## 3. Создание суперпользователя 

```bash
python manage.py createsuperuser
```
Далее введите информацию:
username
email
password

## 4. Запуск сервера

```bash
python manage.py runserver
```

## 5. Доступ к приложению

Главная страница доступна по адресу: http://localhost:8000/
Админ-панель доступна по адресу: http://localhost:8000/admin/

## 6. Добавление товаров 

Необходимо перейти в админ-панель по адресу: http://localhost:8000/admin/
Найдите модель Product
Нажмите "Add PRODUCT"
Заполните название, описание, цену и изображение (опциально)
Сохраните результат