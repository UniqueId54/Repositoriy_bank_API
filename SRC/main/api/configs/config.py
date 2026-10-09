from pathlib import Path
from typing import Any


class Config:
    _isinstance = None  # переменная класса
    _dictionary = {}  # пустой словарь, в который потом будет записано urls.properties

    def __new__(cls):  # создание нового объекта (cls -это и есть Config)
        if cls._isinstance is None:  # создавали ли мы Config? True
            cls._isinstance = super(Config, cls).__new__(cls)  # создай объект Config и сохр. в _isinstance

            config_path = Path(__file__).parents[
                              4] / '.venv' / 'resources' / 'urls.properties'  # путь к указанному файлу urls

            if not config_path.exists():  # если файла не существует в urls
                raise FileNotFoundError(f"Config path not found at {config_path}")  # поднятие ошибки

            with open(config_path, "r") as f:  # откр файл по пути config_path для чтения
                for line in f:  # читаем файл построчно
                    if "=" in line:  # есть есть =
                        key, value = line.split("=")  # разделить на ключ = значение
                        cls._dictionary[key] = value.strip()  # закидываем в словарь base_url и https://

        return cls._isinstance  # возврат объекта Config

    @staticmethod
    def fetch(key: str, default_value: Any = None) -> Any:  # функция которая хранит ключ значние

        return Config()._dictionary.get(key, default_value)  # возврат ключа и значения
