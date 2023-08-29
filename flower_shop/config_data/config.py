from dataclasses import dataclass
from pathlib import Path
from environs import Env


@dataclass
class TgBot:
    token: str
    #admin_ids: list[int]


@dataclass
class Config:
    tg_bot: TgBot


def load_config(env_path: Path | None = None) -> Config:
    '''Loading configurations using environment variables from an .env file,
    the path to which should be specified as an argument to the function.
    If the path to the .env is not specified, the function will look for the
    file in the entry point directory.
    Returns an instance of the Config class with the data already filled in.
    '''

    env:Env = Env()
    env.read_env(env_path)

    return Config(tg_bot=TgBot(token=env('TG_BOT_TOKEN')))
