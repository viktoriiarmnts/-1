import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
DB_NAME = os.getenv('DB_NAME') # Наприклад: fitness.db

if not BOT_TOKEN:
    raise ValueError("Токен не знайдено! Перевір файл .env")