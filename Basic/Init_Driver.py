from appium import webdriver


def init_driver():
    # 服务端启动参数
    desired_caps = {}
    ##	⼿机系统信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '11.0'
    ##设备号
    desired_caps['deviceName'] = '19021'
    ##包名
    desired_caps['appPackage'] = 'com.android.contacts'
    ##启动名
    desired_caps['appActivity'] = '.activities.PeopleActivity'

    desired_caps['noReset'] = True
    ##允许输⼊中⽂
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    ##⼿机驱动对象
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    driver.implicitly_wait(60)
    return driver
