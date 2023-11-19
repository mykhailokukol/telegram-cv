from os import getenv
from dotenv import find_dotenv, load_dotenv
from pathlib import Path


load_dotenv(find_dotenv())


class Settings:
    TG_TOKEN = getenv("TELEGRAM_BOT_TOKEN")
    BASE_DIR = Path(__file__).resolve().parent.parent


settings = Settings()
