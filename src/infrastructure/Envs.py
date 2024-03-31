from dotenv import load_dotenv
import os

os.environ.clear()
load_dotenv('.env')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_NAME = os.getenv('DB_NAME')
ENV = os.getenv('ENV')