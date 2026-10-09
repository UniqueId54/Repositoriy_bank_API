import pytest

from SRC.main.api.db.engine import SessionLocal, engine


@pytest.fixture(scope="function")
def db_session():
    connection = engine.connect()
    transaction = connection.begin()
    session = SessionLocal(bind=connection)
    try:
        yield session

    finally:  # строго в таком порядке! типо стэка: первый зашел - последним вышел
        session.close()
        transaction.rollback()
        connection.close()
