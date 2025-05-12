FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install -r /app/requirements.txt && \
    mkdir -p /app/logs && chmod -R 777 /app/logs

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
