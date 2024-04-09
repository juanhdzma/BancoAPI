FROM python:3.12

WORKDIR /app

COPY env/prod.env .env
COPY . /app

RUN pip install -r requirements.txt

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]