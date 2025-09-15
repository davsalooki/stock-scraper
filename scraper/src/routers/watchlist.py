from fastapi import APIRouter, status

from ..dependencies import ConnectionDep, StockIdentifierDep
from ..models import StockIdentifier, StockOverview
from ..scraper import run_scraper

router = APIRouter()


@router.get("/watchlist")
def get_watchlist(connection: ConnectionDep) -> list[StockOverview]:
    with connection:
        result = connection.execute(
            """
            SELECT s.exchange_code, s.ticker_symbol, s.name, s.last
            FROM stocks s
            JOIN watchlist_items w ON s.exchange_code = w.exchange_code AND s.ticker_symbol = w.ticker_symbol
            WHERE w.watchlist_id = ?
        """,
            (1,),
        )
        stock_summary_list = []
        for row in result.fetchall():
            stock_summary = StockOverview(**dict(row))
            stock_summary_list.append(stock_summary)
        return stock_summary_list


@router.post("/watchlist", status_code=status.HTTP_201_CREATED)
def add_to_watchlist(
    connection: ConnectionDep, stock_identifier: StockIdentifier
) -> None:
    stock = run_scraper(stock_identifier)
    with connection:
        connection.execute(
            "INSERT INTO watchlist_items (watchlist_id, exchange_code, ticker_symbol) VALUES (?, ?, ?)",
            (1, stock.exchange_code, stock.ticker_symbol),
        )

        connection.execute(
            "REPLACE INTO stocks (exchange_code, ticker_symbol, name, financials, last) VALUES (?, ?, ?, ?, ?)",
            (
                stock.exchange_code,
                stock.ticker_symbol,
                stock.name,
                stock.financials.model_dump_json(),
                stock.last
            ),
        )
    connection.close()


@router.delete(
    "/watchlist/stocks/{exchange_code}/{ticker_symbol}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def remove_from_watchlist(
    connection: ConnectionDep, stock_identifier: StockIdentifierDep
) -> None:
    with connection:
        connection.execute(
            "DELETE FROM watchlist_items WHERE watchlist_id = ? AND exchange_code = ? AND ticker_symbol = ?",
            (1, stock_identifier.exchange_code, stock_identifier.ticker_symbol),
        )
    connection.close()
