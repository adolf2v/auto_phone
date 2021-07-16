import time

from Basic.Base import Base
import Page


class First_Page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)
        self.apply_button = "autoTestId-CASH_IOUS_PLUS"

    def click_apply_button(self):
        self.click_element(self.apply_button)
