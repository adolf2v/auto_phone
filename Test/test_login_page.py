import unittest

import pytest

from Page.login_page import Login_Page
from Basic.Init_Driver import init_driver
import time
import allure


@allure.feature('测试登录功能')
class TestLogin:
    def setup(self):
        self.driver = init_driver()
        self.lp = Login_Page(self.driver)

    @allure.feature("test_login")
    def test_login(self):
        time.sleep(5)
        self.lp.click_apply_button()
        self.lp.click_agree_protocol()
        self.lp.input_mobile()
        time.sleep(1)
        print('第四步')

    def teardown(self):
        self.driver.quit()


if __name__ == '__main__':
    # pytest.main(["-s", "test_search_page.py"])
    # allure generate result -o report --clean
    # console: pytest --reruns=1 --reruns-delay=2 --alluredir result
    pytest.main(["--reruns", "1", "--reruns-delay", "2", "--alluredir", "result"])
