# Плохой Dockerfile: намеренно содержит bad practices для лабораторной работы
FROM python:latest

WORKDIR /app

# Bad practice: копируется весь контекст, включая потенциально лишние файлы
COPY . /app

# Bad practice: установка лишних пакетов, отсутствие очистки apt cache, лишний слой
RUN apt-get update && apt-get install -y curl vim iputils-ping net-tools

# Bad practice: секреты нельзя хранить внутри Dockerfile
ENV SECRET_KEY=very_secret_password_123
ENV APP_PORT=8000
ENV APP_NAME="Bad Clouds Container"

# Bad practice: контейнер работает от root-пользователя
USER root

EXPOSE 8000

# Bad practice: shell-form CMD хуже управляет сигналами завершения процесса
CMD python app.py
