from sqlalchemy import create_engine
from src.database.data_migration import get_bet_data, get_events_data
from src.settings import logger
from src.database.raw_sql import raw_create_events_table, raw_create_bets_table, raw_insert_bets_table, \
    raw_insert_events_table
from src.types.settings import settings
from sqlalchemy.sql import text


class PostgresUoW:
    def __init__(self, user: str, password: str, database: str, host: str, port: int = None):
        self.user = user
        self.password = password
        self.database = database
        self.host = host
        self.port = port

        if self.port:
            self.url = f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
        else:
            self.url = f"postgresql://{self.user}:{self.password}@{self.host}/{self.database}"

        self.engine = create_engine(url=self.url)
        self.conn = self.engine.connect()

    def create_tables(self) -> None:
        """Создание таблиц в базе данных"""

        logger.info("Создание таблиц в базе данных ...")
        self.conn.execute(text(raw_create_events_table()))
        self.conn.execute(text(raw_create_bets_table()))
        self.conn.commit()

    def migrate_data(self) -> None:
        """Миграция данных"""

        logger.info("Миграция данных ...")
        self.conn.execute(text(raw_insert_events_table()), get_events_data())
        self.conn.execute(text(raw_insert_bets_table()), get_bet_data())
        self.conn.commit()


postgres_uow = PostgresUoW(
    password=settings.POSTGRES_PASSWORD,
    user=settings.POSTGRES_USER,
    database=settings.POSTGRES_DB,
    host=settings.POSTGRES_HOST
)
