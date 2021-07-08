import time

from Basic.Base import Base
import Page


class Login_Page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)
        self.apply_button = "autoTestId-CASH_IOUS_PLUS"
        self.login_mobile_txt = "com.ctrip.jr:id/atom_uc_input_text_view"
        self.agree_protocol_chbox = "com.ctrip.jr:id/atom_uc_login_protocol_check"

    def click_apply_button(self):
        self.click_element(self.apply_button)

    def click_agree_protocol(self):
        self.click_element(self.agree_protocol_chbox)

    def input_mobile(self):
        self.input_text(self.login_mobile_txt, "18612965323")
