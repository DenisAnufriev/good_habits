# Good Habits

## Обзор
Good Habits API — это backend на основе Django REST Framework для управления персональными привычками. Пользователи могут создавать, отслеживать и делиться привычками с настраиваемыми параметрами, такими как периодичность, продолжительность и награды. API поддерживает аутентификацию, что позволяет безопасно управлять своими привычками, а также получать доступ к публичным привычкам, которыми делятся другие.

## Установка и настройка с Docker

### 1. Клонирование репозитория

```bash
git clone git@github.com:DenisAnufriev/good_habits.git
cd good_habits
```

### 2. Копирование файла env.example в .env
Откройте .env и замените значения переменных на свои собственные:
```bash
cp .env.example .env
```

### 2.1 Настройка переменных окружения

# .env файл
SECRET_KEY=секретный_ключ_для_Django
DEBUG=True # Установите False в продакшене
POSTGRES_USER=имя_пользователя_PostgreSQL
POSTGRES_PASSWORD=пароль_для_PostgreSQL
POSTGRES_DB=название_базы_данных
REDIS_URL=redis://redis:6379/0 # URL Redis

### 3. Сборка и запуск Docker-контейнеров
Выполните следующую команду для сборки образов Docker:
```bash
docker-compose build
```
Запустите приложение и его зависимости:
```bash
docker-compose up
```

Сервер будет доступен по адресу: http://127.0.0.1:8000

### 4. Тестирование приложения
Запустите тесты с покрытием. Эта команда выполнит тесты Django и соберет данные о покрытии кода:
```bash
docker exec -it django coverage run --source='.' manage.py test
docker exec -it django coverage report
```

### 5. Остановка и очистка Docker-контейнеров
Для остановки запущенных контейнеров используйте:
```bash
docker-compose down
```
При необходимости удалите неиспользуемые контейнеры и образы для освобождения места:
```bash
docker system prune -a
```

### 6. Документация
Полная документация API доступна по адресу: http://127.0.0.1:8000/swagger/

### 7. Инструкция если нужно выполнить миграции вручную:

# Создание миграций
docker exec -it django python manage.py makemigrations

# Применение миграций
docker exec -it django python manage.py migrate

### 8. Решение распространённых проблем

# Ошибка: "Database is not ready"
Решение: Убедитесь, что контейнер с PostgreSQL работает корректно и POSTGRES_USER, POSTGRES_DB указаны правильно.

# Ошибка: "Cannot connect to Redis"
Решение: Проверьте, запущен ли контейнер redis и совпадает ли порт 6379.