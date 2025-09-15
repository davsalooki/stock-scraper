from fastapi import APIRouter

from ..scraper import run_scraper

from ..dependencies import ConnectionDep, StockIdentifierDep
from ..models import StockFinancials, StockSummary

from ..config import STOCK_ID_TO_NAME

router = APIRouter()


@router.get("/stocks")
def get_all_stocks() -> list[StockSummary]:
    res = []
    for stock_id, name in STOCK_ID_TO_NAME.items():
        dict_row = {
            "exchange_code": stock_id.split(":")[0],
            "ticker_symbol": stock_id.split(":")[1],
            "name": name,
        }
        res.append(StockSummary.model_validate(dict_row))
    return res


@router.get("/stocks/{exchange_code}/{ticker_symbol}/financials")
def get_stock_financials(
    connection: ConnectionDep, stock_identifier: StockIdentifierDep
) -> StockFinancials:
    with connection:
        row = connection.execute(
            "SELECT financials FROM stocks WHERE exchange_code = ? AND ticker_symbol = ?",
            (stock_identifier.exchange_code, stock_identifier.ticker_symbol),
        ).fetchone()

        financials = StockFinancials.model_validate_json(row["financials"])
    connection.close()
    return financials


@router.post("/stocks/{exchange_code}/{ticker_symbol}/update", status_code=204)
def update_stock(
    connection: ConnectionDep, stock_identifier: StockIdentifierDep
) -> None:
    stock = run_scraper(stock_identifier)
    with connection:
        connection.execute(
            "UPDATE stocks SET financials = ? WHERE exchange_code = ? AND ticker_symbol = ?",
            (
                stock.financials.model_dump_json(),
                stock_identifier.exchange_code,
                stock_identifier.ticker_symbol,
            ),
        )

        connection.execute(
            "UPDATE stocks SET last = ? WHERE exchange_code = ? AND ticker_symbol = ?",
            (
                stock.last,
                stock_identifier.exchange_code,
                stock_identifier.ticker_symbol,
            ),
        )
    connection.close()
