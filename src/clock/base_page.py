# 姓名：郭宏亮
# 时间：2023/5/22 22:14
from appium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:

    def __init__(self, driver=None, caps=None):
        if driver is not None:
            self.driver: WebDriver = driver
        else:
            if caps is None:
                caps = {}
            caps["platformName"] = "android"
            caps["settings[waitForIdleTimeout]"] = 0
            caps["appium:ensureWebviewsHavePages"] = True
            caps["appium:nativeWebScreenshot"] = True
            caps["appium:newCommandTimeout"] = 3600
            caps["appium:connectHardwareKeyboard"] = True
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            self.driver.implicitly_wait(20)

    def close(self):
        self.driver.quit()

    def back(self):
        pass

    def click(self):
        """
        自动截图
        :return:
        """
        pass

    def send_keys(self):
        pass
