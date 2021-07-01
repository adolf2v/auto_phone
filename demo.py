import os
import time
import unittest
from appium import webdriver


class SimpleAndroidTests(unittest.TestCase):
    def setUp(self):
        capabilities = {'platformName': 'Android', 'platformVersion': '11.0', 'deviceName': 'Android Emulator',
                        'appPackage': 'com.android.contacts', 'appActivity': '.activities.PeopleActivity',
                        'unicodeKeyboard': True, 'resetKeyboard': True}
        # Android平台测试
        # 测试手机版本为5.0
        # 系统手机中的联系人app的包名
        # 系统手机中的联系人app的主入口activity
        # desired_caps['app'] = os.path.abspath(cwd + '/YCMath_Android_V2.7.0_guanghetv.apk')
        # desired_caps['appPackage'] = 'com.yangcong345.android.phone'
        # desired_caps['appActivity'] = 'com.yangcong345.android.phone.presentation.activity.SplashActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)
        self.driver.implicitly_wait(60)

    def tearDown(self):
        # end the session
        self.driver.quit()

    def test_contract(self):
        try:
            # com.android.contacts:id/floating_action_button为通过uiautomatorviewer截取联系人界面获取到的
            element = self.driver.find_element_by_id('com.android.contacts:id/floating_action_button')
            # 如果找到该id所指定控件，则进行点击操作
            self.assertIsNone(element)
            element.click()
        except:
            print("exit")


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(
        unittest.defaultTestLoader.loadTestsFromTestCase(SimpleAndroidTests)
    )
    unittest.TextTestRunner(verbosity=2).run(suite)
    # timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    # filename = os.path.abspath(os.getcwd() + '/result') + "/result_" + timestr + ".html"
    # print(filename)
    # fp = open(filename, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(
    #     stream=fp,
    #     title='测试结果',
    #     description='测试报告'
    # )
    # runner.run(suite)
    # fp.close()  # 测试报告关闭
