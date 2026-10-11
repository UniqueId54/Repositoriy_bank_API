from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from SRC.main.api.configs.config import Config

engine = create_engine(Config.fetch('dataBaseURL'), echo=False)  # echo - лог SQL запросов, engine - движок подключения
SessionLocal = sessionmaker(bind=engine) # сессия фабрик - с её помощью идет работа с БД
