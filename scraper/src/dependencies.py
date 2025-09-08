import sqlite3
from typing import Annotated

from fastapi import HTTPException, status
from fastapi.params import Depends
from pydantic import ValidationError

from src.models import StockIdentifier


def get_connection():
    connection = sqlite3.connect("./db/stock-scraper.db")
    connection.row_factory = sqlite3.Row
    return connection

def stock_identifier(exchange_code: str, ticker_symbol: str) -> StockIdentifier:
    try:
        stock_id = StockIdentifier(exchange_code=exchange_code.upper(), ticker_symbol=ticker_symbol.upper())
    except ValidationError as e:
        print("Validation error:", e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid stock identifier")
    return stock_id


ConnectionDep = Annotated[sqlite3.Connection, Depends(get_connection)]
StockIdentifierDep = Annotated[StockIdentifier, Depends(stock_identifier)]
