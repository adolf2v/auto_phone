import time

from Basic.Base import Base
import Page


class Login_Page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)
        self.login_page_title = "com.ctrip.jr:id/atom_uc_tv_title"
        self.login_page_sub_title = "com.ctrip.jr:id/atom_uc_tv_sub_title"
        self.login_page_mobile_txt = "com.ctrip.jr:id/atom_uc_input_text_view"
        self.login_page_agree_protocol_chbox = "com.ctrip.jr:id/atom_uc_login_protocol_check"
        self.login_page_login_btn = "com.ctrip.jr:id/atom_uc_view_act_button"
        self.login_page_three_protocol_txt = "com.ctrip.jr:id/atom_uc_login_protocol_text"
        self.login_page_union_login_link = "com.ctrip.jr:id/atom_uc_login_more_function"

    def click_agree_protocol(self):
        self.click_element(self.login_page_agree_protocol_chbox)

    def input_mobile(self, mobile):
        self.input_text(self.login_page_mobile_txt, mobile)

    def click_login_btn(self):
        self.click_element(self.login_page_login_btn)
