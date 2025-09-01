"""Scraper for CommSec financial data"""

import os
from playwright.sync_api import sync_playwright, Page, BrowserContext
from dotenv import load_dotenv

from .config import CONFIG
from .models import StockInfo, Ticker

load_dotenv()


def login(context: BrowserContext, page: Page) -> None:
    CLIENT_ID = os.getenv("CLIENT_ID")
    PASSWORD = os.getenv("PASSWORD")
    LOGIN_URL = CONFIG["urls"]["login"]

    page.goto(LOGIN_URL)

    # Fill in login form
    page.get_by_role("textbox", name="Client ID").fill(CLIENT_ID)
    page.get_by_role("textbox", name="Password").fill(PASSWORD)

    # Non-unique button name, so use exact match
    page.get_by_role("button", name="Login", exact=True).click()


def get_mod_token(context: BrowserContext, page: Page) -> str:
    """Get the ModToken cookie from the browser context.

    This cookie is required in the URL when requesting financial data.
    """
    page.goto(CONFIG["urls"]["financials"])

    cookies = context.cookies()
    mod_token = next(
        (cookie for cookie in cookies if cookie["name"] == "ModToken"), None
    )

    if not mod_token:
        raise Exception("ModToken cookie not found.")

    # Find portion usable in the company financial's URL
    return mod_token["value"].split("-")[0]


def yoink_info(
    context: BrowserContext, page: Page, mod_token: str, ticker: Ticker
) -> StockInfo:
    """Fetch financial data using the API."""
    api_request_context = context.request
    response = api_request_context.get(
        CONFIG["urls"]["stock_info"],
        params={
            "access_token": mod_token,
            "exchangeCode": ticker.exchange_code,
            "symbol": ticker.stock_code,
        },
    )

    response_json = response.json()

    # Return the most recent data, first in the List
    return_data = StockInfo(
        financials=response_json["data"]["financials"][0],
        earnings_roe_chart=response_json["data"]["financialChartSrc"],
    )

    return return_data


def run_scraper(ticker: Ticker) -> StockInfo:
    """Scrapes stock financial info from CommSec."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()

        login(context, page)

        mod_token = get_mod_token(context, page)
        data = yoink_info(context, page, mod_token, ticker)

        browser.close()

    return data
