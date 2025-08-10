from dotenv import load_dotenv
from playwright.sync_api import sync_playwright, Page
import os

from src.scraper import run_scraper

load_dotenv()

PAGE_URL = "https://www2.commsec.com.au/quotes/financials?stockCode=UNI&exchangeCode=ASX"

def main():
    print("Hello from stock-scraper!")
    run_scraper()

if __name__ == "__main__":
    main()
