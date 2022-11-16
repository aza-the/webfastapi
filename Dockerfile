# syntax=docker/dockerfile:1

FROM python:3.10

WORKDIR /app

COPY . .

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "3000"]