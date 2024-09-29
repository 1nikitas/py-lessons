import json
from pathlib import Path

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    postgresql_url: PostgresDsn
    debug: bool = False
    api_prefix: str = ''

    @classmethod
    def load_settings(cls, path_to_configs: Path) -> 'Settings':


        with open(path_to_configs, 'r') as file:
            unparsed_settings = json.load(file)
        config = cls.model_validate(unparsed_settings)

        return config

settings = Settings.load_settings(Path('./local_config.json'))