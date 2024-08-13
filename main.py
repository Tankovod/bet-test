from sqlalchemy import text
from src.settings import logger
from src.database.base import postgres_uow
from datetime import datetime

datetime(hour=12, minute=0, day=14, month=3, year=2022)


def main():
    postgres_uow.create_tables()
    postgres_uow.migrate_data()
    data = postgres_uow.conn.execute(text(
        """
        SELECT player_id FROM bets b
        JOIN
            events e ON b.event_id = e.event_id
        WHERE
            b.create_time > '2022-03-14 12:00:00' AND
            b.settlement_time < '2022-03-15 12:00:00' AND
            b.event_stage = 'Prematch' AND 
            b.bet_size >= 10 AND
            b.bet_type <> 'System' AND
            b.is_free_bet is false AND
            b.result not IN ('Cashout', 'Return') AND
            b.accepted_bet_odd >= 1.5 AND
            e.sport = 'E-Sports' 
        """
    ))
    logger.info(f"Количество полученных результатов: {len([*data])}")


if __name__ == "__main__":
    main()
