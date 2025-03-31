import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

API_TOKEN = os.getenv("API_TOKEN")

DB_DIR = os.getenv("DB_PATH")
DB_PATH = os.path.join(DB_DIR, "app.db")

DOWNLOADS_DIR = os.getenv("DOWNLOADS_DIR")

os.makedirs(os.path.dirname(DB_DIR), exist_ok=True)
os.makedirs(DOWNLOADS_DIR, exist_ok=True)

if not os.path.exists(DB_PATH):
    open(DB_PATH, "a").close()
