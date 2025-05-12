FROM python:3.9-slim

WORKDIR /app

COPY ./django /app

RUN pip install --no-cache-dir -r /app/requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
