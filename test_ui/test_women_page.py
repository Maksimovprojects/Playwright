from playwright.sync_api import Playwright, sync_playwright, expect
from pom.shop_women_elements import ShopWomen


def woman_section(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    shop_women = ShopWomen(page)

    expect(shop_women.celebrating_beauty_header).to_be_visible()
    expect(shop_women.celebrating_beauty_body).to_be_visible()


with sync_playwright() as playwright:
    woman_section(playwright)  # running the test

# Q  Empty suite
