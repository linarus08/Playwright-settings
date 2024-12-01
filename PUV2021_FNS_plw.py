import re
import time
import keyboard

from playwright.sync_api import Playwright, sync_playwright, expect


def go_application(browser, page, id_application):
    """ По ID войти в обращение """
    application_url = f"http://puv.egisso.ru/applications/assignment/{id_application}"
    page.goto(application_url)


def click_check_statistic(page):
    """ Переключить 'Статистика запросов сведений' """
    page.locator('nz-switch').click()


def tabl_processing(page):
    """ Из таблицы получить список запросов в ФНС """
    class_name = 'ant-tabs-content-holder'
    page.wait_for_selector("//*[@class='ant-tabs-content-holder']//tbody")
    table = page.locator("//*[@class='ant-tabs-content-holder']//tbody")
    time.sleep(3)

    all_rows = table.all_text_contents()
    print(all_rows)
    # page.wait_for_selector("xpath=//td[contains(text(), 'ФНС')]")
    # row_locator = page.locator("xpath=//td[contains(text(), 'ФНС')]")
    # print(row_locator.count())
    # for rw in row_locator.all():
    #     print(rw.text_content())


def run(playwright: Playwright) -> None:
    path = r'C:\Users\Linar\AppData\Local\Chromium\User Data'
    browser = playwright.chromium.launch_persistent_context(user_data_dir=path, headless=False,
                                                            ignore_default_args=['--enable-automation'],
                                                            args=['--start-maximised'], no_viewport=True)
    page = browser.new_page()
    page.goto("http://puv.egisso.ru/sign-in")
    browser.pages[0].close()

    id_application = '3ae8e72f-2718-42ee-9b9a-e8158f8ea7d4'
    go_application(browser, page, id_application)
    click_check_statistic(page)
    tabl_processing(page)

    # ---------------------
    keyboard.wait('Esc')
    browser.close()
    print('Завершение работы.')


with sync_playwright() as playwright:
    run(playwright)
