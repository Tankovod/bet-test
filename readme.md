# Поиск ставок в БД по определенным условиям

## Как это работает?

В базе данных PostgreSQL docker контейнера создаются таблицы и добавляются начальные данные. Далее выполняется запрос на выборку ставок по определенным критериям вида:

```SQL
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
```

## Порядок установки:

- Добававить файлы с данными bets.csv, events.csv в корень проекта.
- Переименовать файл .env.example в .env и подставить в него свои значения.
- Запуск проекта командой ```docker compose up```.