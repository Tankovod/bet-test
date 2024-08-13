

def raw_create_bets_table() -> str:
    return """
            CREATE TABLE if not exists bets (
            bet_id UUID NOT NULL,
            player_id UUID NOT NULL,
            accept_time TIMESTAMP NULL,
            create_time TIMESTAMP NULL,
            settlement_time TIMESTAMP NULL,
            result VARCHAR(255) NOT NULL,
            amount DECIMAL(10, 2) NULL,
            payout DECIMAL(10, 2) NULL,
            profit DECIMAL(10, 2) NULL,
            bet_type VARCHAR(255) NOT NULL,
            bet_size DECIMAL(10, 2) NOT NULL,
            accepted_bet_odd DECIMAL(10, 2) NULL,
            item_result VARCHAR(255) NOT NULL,
            event_stage VARCHAR(255) NOT NULL,
            accepted_odd DECIMAL(10, 2) NULL,
            item_amount DECIMAL(10, 2) NULL,
            item_payout DECIMAL(10, 2) NULL,
            item_profit DECIMAL(10, 2) NULL,
            event_id UUID NOT NULL,
            is_free_bet BOOLEAN NOT NULL,
            settlement_status VARCHAR(255) NOT NULL,
            FOREIGN KEY (event_id) REFERENCES events(event_id)
            );
            """


def raw_create_events_table() -> str:
    return """
            CREATE TABLE if not exists events (
            event_id UUID PRIMARY KEY,
            sport VARCHAR(255) NOT NULL,
            category VARCHAR(255) NOT NULL,
            event VARCHAR(255) NOT NULL
            );
            """


def raw_insert_bets_table() -> str:
    return """
    INSERT INTO bets (
    bet_id,
    player_id,
    accept_time,
    create_time,
    settlement_time,
    result,
    amount,
    payout,
    profit,
    bet_type,
    bet_size,
    accepted_bet_odd,
    item_result,
    event_stage,
    accepted_odd,
    item_amount,
    item_payout,
    item_profit,
    event_id,
    is_free_bet,
    settlement_status
    )
    VALUES (
    :bet_id,
    :player_id,
    :accept_time,
    :create_time,
    :settlement_time,
    :result,
    :amount,
    :payout,
    :profit,
    :bet_type,
    :bet_size,
    :accepted_bet_odd,
    :item_result,
    :event_stage,
    :accepted_odd,
    :item_amount,
    :item_payout,
    :item_profit,
    :event_id,
    :is_free_bet,
    :settlement_status
    )
    """


def raw_insert_events_table() -> str:
    return """
    INSERT INTO events (
    event_id,
    sport,
    category,
    event
    )
    VALUES (
    :event_id,
    :sport,
    :category,
    :event
    )
    """
