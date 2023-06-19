# 姓名：郭宏亮
# 时间：2023/5/22 22:14
import allure
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
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
            self.driver.implicitly_wait(5)

    def close(self):
        self.driver.quit()

    def back(self):
        self.driver.back()

    def click(self, by, value):
        """
        自动截图
        :return:
        """
        try:
            self.driver.find_element(by, value).click()
            allure.attach(body=self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
            return
        except:
            self.click(by, value)
            allure.attach(body=self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)

    def send_keys(self, by, value, text):
        self.driver.find_element(by, value).send_keys(text)

    def find_elements(self, by, value):
        return self.driver.find_elements(by, value)

    def handle_exception(self):
        if "" in self.driver.page_source:
            pass
