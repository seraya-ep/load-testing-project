# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем requirements.txt в контейнер
COPY app/requirements.txt /app/

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Копируем весь код приложения в контейнер
COPY app /app/

# Открываем порт 5000 для приложения
EXPOSE 5000

# Запуск приложения
CMD ["python", "app.py"]