import sqlite3


def create_tables():
    create_stock_command = """
    CREATE TABLE IF NOT EXISTS stocks (
        ticker TEXT PRIMARY KEY,
        financial_data TEXT
    )
    """

    create_watchlist_command = """
    CREATE TABLE IF NOT EXISTS watchlist (
        id INTEGER PRIMARY KEY AUTOINCREMENT
    )
    """

    create_watchlist_item_cmd = """
    CREATE TABLE IF NOT EXISTS watchlist_item (
        watchlist_id INTEGER NOT NULL,
        ticker TEXT NOT NULL,
        PRIMARY KEY (watchlist_id, ticker),
        FOREIGN KEY (watchlist_id) REFERENCES watchlists(id)
    )
    """

    connection = sqlite3.connect("./db/test.db")
    with connection:
        connection.execute(create_stock_command)
        connection.execute(create_watchlist_command)
        connection.execute(create_watchlist_item_cmd)
    connection.close()

if __name__ == "__main__":
    create_tables()
