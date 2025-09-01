import sqlite3


def create_tables():
    create_stock_command = """
    CREATE TABLE IF NOT EXISTS stocks (
        ticker TEXT PRIMARY KEY,
        financial_data TEXT
    )
    """

    create_watchlist_command = """
    CREATE TABLE IF NOT EXISTS watchlists (
        id INTEGER PRIMARY KEY AUTOINCREMENT
    )
    """

    create_watchlist_item_cmd = """
    CREATE TABLE IF NOT EXISTS watchlist_items (
        watchlist_id INTEGER NOT NULL,
        ticker TEXT NOT NULL,
        PRIMARY KEY (watchlist_id, ticker),
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
    create_tables()
