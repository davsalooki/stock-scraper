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

    # Obtain mod_token cookie for financials access
    page.goto(CONFIG["urls"]["financials"])

    cookies = context.cookies()
    mod_token = next((cookie for cookie in cookies if cookie['name'] == 'ModToken'), None)

    if not mod_token:
        raise Exception("ModToken cookie not found.")

    # Find portion usable in the URL
    mod_token = mod_token.split("-")[0]
    
    print(f"ModToken: {mod_token['value']}")

    page.wait_for_timeout(100000)
    # context.request.get()


def yoink_info(page: Page) -> None:
    """Extract financial data from the page."""
    pass

def run_scraper() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        login(context, page)
        print(type(context.cookies()))
        browser.close()