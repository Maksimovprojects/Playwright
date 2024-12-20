from playwright.sync_api import Playwright, sync_playwright, expect
from pom.home_page_elements import HomePage

def about_us_section(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.wait_for_load_state(timeout=1000)
    home_page = HomePage(page)
    expect(home_page.celebrate_header).to_be_visible()
    expect(home_page.celebrate_body).to_be_visible()
    page.screenshot(path="../screenshot.png", full_page=True)


with sync_playwright() as playwright:
    about_us_section(playwright) # running the test

#Q  Empty suite

