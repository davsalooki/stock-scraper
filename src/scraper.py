""" Scraper for CommSec financial data """

import os
from playwright.sync_api import sync_playwright, Page
from dotenv import load_dotenv

load_dotenv()

PAGE_URL = "https://www2.commsec.com.au/quotes/financials?stockCode=UNI&exchangeCode=ASX"

def login(page: Page) -> None:
    CLIENT_ID = os.getenv("CLIENT_ID")
    PASSWORD = os.getenv("PASSWORD")

    page.goto("https://www2.commsec.com.au/secure/login")

    # Fill in login form
    page.get_by_role("textbox", name="Client ID").fill(CLIENT_ID)
    page.get_by_role("textbox", name="Password").fill(PASSWORD)
    page.get_by_role("button", name="Login", exact=True).click()

def run_scraper() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        login(page)
        browser.close()