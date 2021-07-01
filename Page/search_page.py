import time

from Basic.Base import Base
import Page


class Search_Page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def input_search_text(self):
        self.click_element(Page.search_button)
