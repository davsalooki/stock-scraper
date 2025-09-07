from enum import Enum
from typing import Literal, Self
from pydantic import BaseModel, model_validator

from .config import TICKER_LIST

class StockBase(BaseModel):
    exchange_code: str
    ticker_symbol: str

    def __str__(self) -> str:
        return f"{self.exchange_code}:{self.ticker_symbol}"

    @model_validator(mode="after")
    def is_a_stock(self) -> Self:
        if f"{self.exchange_code}:{self.ticker_symbol}" not in TICKER_LIST:
            raise ValueError("Invalid stock identifier")
        return self
    
class StockIdentifier(StockBase):
    pass

class ReadStock(StockBase):
    name: str

class StockFinancials(BaseModel):
    stats: dict[str, str | int | float]
    earnings_roe_chart: str

class Stock(StockBase):
    name: str
    financials: StockFinancials
