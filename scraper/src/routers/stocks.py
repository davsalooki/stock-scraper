from fastapi import APIRouter

from ..scraper import run_scraper

from ..dependencies import ConnectionDep
from ..models import StockInfo, Ticker

from ..config import TICKER_LIST

router = APIRouter()


@router.get("/stocks")
def get_all_stocks() -> list[Ticker]:
    res = []
    for row in TICKER_LIST:
        row = row.split(":")
        dict_row = {"exchange_code": row[0], "stock_code": row[1]}
        res.append(Ticker.model_validate(dict_row))
    return res


@router.get("/stocks/{ticker}")
def get_stock_financials(ticker: str, connection: ConnectionDep) -> StockInfo:
    ticker = Ticker.model_validate(ticker)
    with connection:
        stock_info = connection.execute(
            "SELECT financial_data FROM stocks WHERE ticker = ?", ticker
        ).fetchone()

        stock_info = StockInfo.model_validate_json(stock_info)
    connection.close()
    return stock_info


@router.put("/stocks/{ticker}")
def update_stock(ticker: str, connection: ConnectionDep) -> None:
    ticker = Ticker.model_validate(ticker)
    stock_info = run_scraper(ticker)
    with connection:
        connection.execute(
            "UPDATE stocks SET financial_data = ? WHERE ticker = ?",
            (stock_info.model_dump_json(), ticker),
        )
    connection.close()
