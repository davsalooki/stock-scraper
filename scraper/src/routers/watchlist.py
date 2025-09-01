from fastapi import APIRouter, status

from ..dependencies import ConnectionDep
from ..models import Ticker
from ..scraper import run_scraper

router = APIRouter()


@router.get("/watchlist")
def get_watchlist(connection: ConnectionDep) -> list[Ticker]:
    with connection:
        result = connection.execute(
            "SELECT * FROM watchlist_items WHERE watchlist_id = ?", (1,)
        )
        ticker_list = []
        for row in result.fetchall():
            ticker = Ticker.model_validate(row)
            ticker_list.append(ticker)
        return ticker_list


@router.post("/watchlist", status_code=status.HTTP_201_CREATED)
def add_to_watchlist(ticker: Ticker, connection: ConnectionDep) -> None:
    stock_info = run_scraper(ticker)
    with connection:
        connection.execute(
            "INSERT INTO watchlist_items (watchlist_id, ticker) VALUES (?, ?)",
            (1, ticker),
        )

        connection.execute(
            "INSERT INTO stocks (ticker, financial_data) VALUES (?, ?)",
            (ticker, stock_info.model_dump_json()),
        )
    connection.close()


@router.delete("/watchlist", status_code=status.HTTP_204_NO_CONTENT)
def remove_from_watchlist(ticker: Ticker, connection: ConnectionDep) -> None:
    with connection:
        connection.execute(
            "DELETE FROM watchlist_items WHERE watchlist_id = ? AND ticker = ?",
            (1, ticker),
        )
    connection.close()
