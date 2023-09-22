FROM ubuntu:latest
LABEL authors="user"

ENTRYPOINT ["top", "-b"]

# Используйте образ Python 3.9 в качестве базового образа
FROM python:3.9

# Установите переменную окружения PYTHONUNBUFFERED для предотвращения буферизации вывода Python
ENV PYTHONUNBUFFERED 1

# Создайте и установите рабочий каталог внутри контейнера
RUN mkdir /app
WORKDIR /app

# Скопируйте зависимости проекта (requirements.txt) в контейнер и установите их
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Установите Gunicorn
RUN pip install gunicorn

# Скопируйте все файлы вашего проекта в контейнер
COPY . /app/

# Запустите команду для запуска вашего приложения с Gunicorn
CMD ["gunicorn", "courses.wsgi:application", "--bind", "0.0.0.0:8000"]
