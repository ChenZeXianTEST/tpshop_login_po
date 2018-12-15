from selenium import webdriver


def get_driver():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1")
    driver.maximize_window()
    return driver

