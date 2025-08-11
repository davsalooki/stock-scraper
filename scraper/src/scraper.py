""" Scraper for CommSec financial data """

import os
from playwright.sync_api import sync_playwright, Page, BrowserContext
from dotenv import load_dotenv

from config import CONFIG

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
    # Obtain mod_token cookie for financials access
    page.goto(CONFIG["urls"]["financials"])

    cookies = context.cookies()
    mod_token = next((cookie for cookie in cookies if cookie['name'] == 'ModToken'), None)

    if not mod_token:
        raise Exception("ModToken cookie not found.")

    # Find portion usable in the company financial's URL
    return mod_token['value'].split("-")[0]


def yoink_info(context: BrowserContext, page: Page, mod_token: str, symbol: str) -> list[dict]:
    """Fetch financial data using the API."""
    api_request_context = context.request
    response = api_request_context.get(CONFIG["urls"]["stock_info"], params={
        "symbol": symbol,
        "access_token": mod_token
    })

    data = response.json()["data"]["financials"]
    return data

def run_scraper() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        login(context, page)
        mod_token = get_mod_token(context, page)

        stocks = ["UNI", "COL"]
        for stock in stocks:
            print(f"Fetching data for stock: {stock}")
            stock_data = yoink_info(context, page, mod_token, stock)
            print(f"Data for {stock}: {stock_data}")
            print("-" * 40)

        browser.close()