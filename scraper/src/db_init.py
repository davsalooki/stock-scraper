import sqlite3


def setup_db():
    create_stock_command = """
    CREATE TABLE IF NOT EXISTS stocks (
        exchange_code TEXT,
        ticker_symbol TEXT,
        name TEXT,
        financials TEXT,
        PRIMARY KEY (exchange_code, ticker_symbol)
    )
    """

    create_watchlist_command = """
    CREATE TABLE IF NOT EXISTS watchlists (
        id INTEGER PRIMARY KEY AUTOINCREMENT
    )
    """

    create_watchlist_item_cmd = """
    CREATE TABLE IF NOT EXISTS watchlist_items (
        watchlist_id INTEGER,
        exchange_code TEXT,
        ticker_symbol TEXT,

        PRIMARY KEY (watchlist_id, exchange_code, ticker_symbol),
        FOREIGN KEY (watchlist_id) REFERENCES watchlists(id)
    )
    """

    # This should only be added if there are no existing watchlists
    add_watchlist_command = """
    INSERT OR IGNORE INTO watchlists (id) VALUES (1)
    """

    connection = sqlite3.connect("./db/stock-scraper.db")
    with connection:
        connection.execute(create_stock_command)
        connection.execute(create_watchlist_command)
        connection.execute(create_watchlist_item_cmd)
        connection.execute(add_watchlist_command)
    connection.close()


if __name__ == "__main__":
    setup_db()
