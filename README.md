# Бэк для проекта по рекомендации рецептов по распознанным продуктам
## Требования
Docker и Docker-Compose.
## Запуск
1) Переименовать `.env-example` в `.env`.
2) Запустить в терминале `docker-compose up --build`
## Основные инструменты, использованные в этом репозитории.
1) FastAPI - web server.
2) Torch + Torchvision - для YOLOv5.
3) Docker - контейнеризация.
4) Docker-Compose - оркестрация; возможно будет заменён на Kubernetes.
5) aiohttp - запросы к стороннему API с рецептами.
## Назначения файлов и модулей
- `.env-exampe` - пример файла с переменными окружения; нужно скопировать или переименовать в `.env` 
- `prod.env` - переменные окружения для развёртывания в продакшн; на данном этапе не используется.
- `pyproject.toml` - информация о проекте и зависимостях для пакетного менеджера poetry. 
- `requirements.txt` - те же зависимости, что и в секции `tool.poetry.dependencies`; в отдельный файл вынес для избежания проблем с зависимостями при сборке контейнера.  
- `Dockerfile` - конфигурация для контейнера Docker. 
- `docker-compose.yml` - конфигурация для Docker-Compose; пока используется только один образ для web-приложения и модели. 
- `app/main.py` - отсюда осуществляется запуск web-приложение FastAPI.
- `app/api/routes/` - маршруты API. 
- `app/api/errors/` - обработчики исключений, возникающих во время обработки запросов приложением.
- `app/core` - настройки веб приложения. 
- `app/models/schemas/` - модели для сущностей, используемых при обработке запросов. 
- `app/services/recipes_parsing/` - класс для парсинга рецептов из внешнего API (`edamam.com`). 
- `app/services/ai_model/` - корневая директория для модели.
- `app/services/ai_model/weights/` - веса модели.
- `app/services/ai_model/yolov5/` - модель.
- `app/services/ai_model/app.py` - модуль для работы с моделью.
- `app/services/foodstuff_recognition.py` - модуль сервиса, объединяющего парсер с моделью и возвращающего списки распознанных объектов и рецептов.