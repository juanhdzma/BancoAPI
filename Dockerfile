FROM python:3.12

WORKDIR /app

COPY env/prod.env .env
COPY . /app

RUN pip install -r requirements.txt