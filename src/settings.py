import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    ENV_FILE: str = '.env'
    DB_DRIVER: str = 'sqlite+aiosqlite'
    BOT_API_TOKEN: str = ''

    BASE_DIR: str = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')
    )
    model_config = SettingsConfigDict(env_file=f"{BASE_DIR}/.env")

    @property
    def db_url(self):
        return (f'{self.DB_DRIVER}:///scraping.sqlite')
