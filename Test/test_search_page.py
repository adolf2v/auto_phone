import pytest

from Page.search_page import Search_Page
from Basic.Init_Driver import init_driver
import time
import allure

class TestBase:
    def setup(self):
        self.driver = init_driver()
    @allure.feature("aaa")
    def test_aaa(self):
        time.sleep(2)
        sp = Search_Page(self.driver)
        time.sleep(1)
        sp.input_search_text()
        print('第四步')

    # self.driver.quit()


if __name__ == '__main__':
    # pytest.main(["-s", "test_search_page.py"])
    # allure generate result -o report --clean
    # console: pytest --reruns=1 --reruns-delay=2 --alluredir result
    pytest.main(["--reruns", "1", "--reruns-delay", "2", "--alluredir", "result"])
