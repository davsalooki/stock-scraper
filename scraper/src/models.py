from typing import Self
from pydantic import BaseModel, model_validator

from .config import TICKER_LIST


class StockInfo(BaseModel):
    financials: dict[str, str | int | float]
    earnings_roe_chart: str


class Ticker(BaseModel):
    exchange_code: str
    stock_code: str

    def __repr__(self):
        return f"{self.exchange_code}:{self.stock_code}"

    @model_validator(mode="after")
    def is_a_stock(self) -> Self:
        if f"{self.exchange_code}:{self.stock_code}" not in TICKER_LIST:
            raise ValueError("Invalid stock code")
        return self


class Stock(BaseModel):
    ticker: Ticker
    info: StockInfo
