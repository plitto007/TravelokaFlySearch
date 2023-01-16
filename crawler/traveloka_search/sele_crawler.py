import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def create_driver():
    """
    Create selenium driver
    """
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--no-sandbox")
    options.add_argument('--headless')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-dev-shm-usage")  # overcome limited  resource   problems
    options.add_argument(
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36")
    driver = webdriver.Chrome(options=options)
    return driver


def open_selenium(url="https://traveloka.com"):
    """
    Open selenium and return the cookie object
    :param url:
    :return:
    """
    driver = create_driver()
    try:
        driver.get(url)
        time.sleep(5)
        all_cookies = driver.get_cookies()
        cookies_dict = {}
        for cookie in all_cookies:
            cookies_dict[cookie['name']] = cookie['value']
        print('==========COOKIE==============')
        print(cookies_dict)
        driver.quit()
        return cookies_dict
    except Exception as e:
        driver.quit()
        return {}
