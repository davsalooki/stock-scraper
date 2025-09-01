import sqlite3
from typing import Annotated

from fastapi.params import Depends


def get_connection():
    return sqlite3.connect("./db/stock-scraper.db")


ConnectionDep = Annotated[sqlite3.Connection, Depends(get_connection)]
