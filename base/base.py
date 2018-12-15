from selenium.webdriver.support.wait import WebDriverWait


class Base():

    def __init__(self, driver):
        self.driver = driver

    def base_find_element(self, loc, timeout=10, poll=0.5):
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))

    def base_click_element(self, loc):
        self.base_find_element(loc).click()

    def base_input(self, loc, test):
        ele = self.base_find_element(loc)
        ele.clear()
        ele.send_keys(test)
