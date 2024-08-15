import re
import time
import keyboard

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    path = r'C:\Users\Linar\AppData\Local\Chromium\User Data'
    browser = playwright.chromium.launch_persistent_context(user_data_dir=path, headless=False,
                                                            ignore_default_args=['--enable-automation'],
                                                            args=['--start-maximised'], no_viewport=True, slow_mo=1000)
    page = browser.new_page()
    page.goto("http://puv.egisso.ru/dashboard")
    browser.pages[0].close()



    keyboard.wait('Esc')
    # ---------------------
    browser.close()
    print('Завершение работы.')


with sync_playwright() as playwright:
    run(playwright)
