import sqlite3
from typing import Annotated

from fastapi.params import Depends

def get_connection():
    # Context manager for closing session and autocommitting transactions
    with sqlite3.connect("../db/stock-scraper.db") as connection:
        yield connection

SessionDep = Annotated[sqlite3.Connection, Depends(get_connection)]
