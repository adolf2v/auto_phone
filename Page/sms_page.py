import time

from Basic.Base import Base
import Page


class Sms_Page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)
        self.sms_page_txt = "com.ctrip.jr:id/atom_uc_sms_vcode_input"
        self.sms_page_phone = "com.ctrip.jr:id/atom_uc_sms_vcode_verify_phone_tv"

    def input_sms_code(self, sms="000000"):
        self.input_text(self.sms_page_txt, sms)

    def get_phone_text(self, txt="****"):
        return txt in self.get_text(loc=self.sms_page_phone, value="text")
