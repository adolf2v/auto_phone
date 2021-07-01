from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class Base(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, loc, timeout=1):
        print('第二步', loc)
        return WebDriverWait(self.driver, timeout).until(lambda x: x.find_element(by=By.ID, value=loc))

    def click_element(self, loc):
        self.find_element(loc).click()

    def input_text(self, loc, text):
        self.fm = self.find_element(loc)
        self.fm.clear()
        self.fm.send_keys(text)
