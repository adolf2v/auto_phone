import unittest

import pytest

from Page.login_page import Login_Page
from Page.first_page import First_Page
from Page.sms_page import Sms_Page
from Basic.Init_Driver import init_driver, init_ios_driver
import time
import allure


@allure.feature('测试登录功能')
class TestLogin:
    def setup(self):
        self.driver = init_driver()
        self.lp = Login_Page(self.driver)
        self.fp = First_Page(self.driver)
        self.sp = Sms_Page(self.driver)

    @allure.feature("test_login")
    def test_login(self):
        time.sleep(5)
        self.fp.click_apply_button()
        print(self.driver.page_source)
        self.lp.click_agree_protocol()
        self.lp.input_mobile(mobile="18612965323")
        self.lp.click_login_btn()
        time.sleep(1)
        self.sp.input_sms_code(sms="123456")
        assert not self.sp.get_phone_text()
        print('第四步')

    def teardown(self):
        self.driver.quit()


if __name__ == '__main__':
    # pytest.main(["-s", "test_search_page.py"])
    # allure generate result -o report --clean
    # console: pytest --reruns=1 --reruns-delay=2 --alluredir result
    pytest.main(["--reruns", "0", "--reruns-delay", "2", "--alluredir", "result"])
