# selenium_utils.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pickle
import time

def setup_driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def load_session_cookies(driver, cookie_file, profile_url):
    driver.get("https://www.linkedin.com/")
    time.sleep(2)
    cookies = pickle.load(open(cookie_file, "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get(profile_url)
    print("Successfully loaded session cookies and accessed profile!")
