from contextlib import asynccontextmanager, contextmanager
from dotenv import load_dotenv
from fastapi import FastAPI

from .db_init import setup_db

from .models import Ticker
from .routers import stocks, watchlist
from .scraper import run_scraper

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_db()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(watchlist.router)
app.include_router(stocks.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


def main():
    print("Hello from stock-scraper!")
    ticker = Ticker(exchange_code="ASX", stock_code="UNI")
    x = run_scraper(ticker)
    print(x)


if __name__ == "__main__":
    main()
