import csv
from src.types.settings import settings


def get_bet_data() -> list[dict]:
    with open(settings.BASE_DIR / "bets.csv", 'r') as file:
        csvreader = csv.reader(file)
        data = []
        for row in [*csvreader][1:]:
            data.append(
                {
                    "bet_id": row[0],
                    "player_id": row[1],
                    "accept_time": row[2] if row[2] else None,
                    "create_time": row[3] if row[3] else None,
                    "settlement_time": row[4] if row[4] else None,
                    "result": row[5],
                    "amount": float(row[6]) if row[6] else None,
                    "payout": float(row[7]) if row[7] else None,
                    "profit": float(row[8]) if row[8] else None,
                    "bet_type": row[9],
                    "bet_size": row[10],
                    "accepted_bet_odd": row[11],
                    "item_result": row[12],
                    "event_stage": row[13],
                    "accepted_odd": row[14],
                    "item_amount": row[15] if row[15] else None,
                    "item_payout": row[16] if row[16] else None,
                    "item_profit": row[17] if row[17] else None,
                    "event_id": row[18],
                    "is_free_bet": row[19],
                    "settlement_status": row[20]
                }
            )
        return data


def get_events_data() -> list[dict]:
    with open(settings.BASE_DIR / "events.csv", 'r') as file:
        csvreader = csv.reader(file)
        data = []
        for row in [*csvreader][1:]:
            data.append(
                {
                    "event_id": row[0],
                    "sport": row[1],
                    "category": row[2],
                    "event": row[3]
                }
            )
        return data
