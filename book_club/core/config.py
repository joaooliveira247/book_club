from dotenv import load_dotenv, dotenv_values
from pathlib import Path


class Settings:
    db_url: str
    TABLE_NAME: str | None
    BOOK_BASE_URL = "https://books.toscrape.com/"
    DB_USER: str | None
    DB_PASS: str | None
    DB_HOST: str | None
    DB_NAME: str | None
    BASE_DIR = Path(__file__).parent.parent.parent

    def __init__(self) -> None:
        env = load_dotenv()
        if not env:
            raise Exception(".env not found")
        env = dotenv_values()
        try:
            self.DB_USER = env["DB_USER"]
            self.DB_PASS = env["DB_PASS"]
            self.DB_NAME = env["DB_NAME"]
            self.DB_HOST = env["DB_HOST"]
            self.DB_PORT = env["DB_PORT"]
            self.TABLE_NAME = env["DB_TABLE_NAME"]
        except KeyError:
            raise KeyError("Try set .env values")
        self.db_url = (
            f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASS}@"
            f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

    def __repr__(self) -> str:
        self.__dict__.__str__()


settings = Settings()
