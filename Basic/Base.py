from selenium.webdriver.support.wait import WebDriverWait
from Basic.Init_Driver import init_driver


class Base(object):
    def __init__(self, driver):
        self.driver = driver

    # 查找元素
    def find_element(self, loc):
        if "autoTestId" in loc:
            return self.driver.find_element_by_accessibility_id(loc)
        else:
            return self.driver.find_element_by_id(loc)

    # 点击元素
    def click_element(self, loc):
        self.find_element(loc).click()

    # 输入指定的text
    def input_text(self, loc, text):
        self.fm = self.find_element(loc)
        self.fm.clear()
        self.fm.send_keys(text)
