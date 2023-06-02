# 姓名：郭宏亮
# 时间：2023/5/22 22:14
from time import sleep

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

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def find_elements(self, by, value):
        return self.driver.find_elements(by, value)

    def click(self, by, value):
        try:
            self.driver.find_element(by, value).click()
            allure.attach(body=self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
            return
        except:
            allure.attach(body=self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
            self.exception_handle()
            self.click(by, value)

    # 异常处理

    def send_keys(self, by, value, text):
        self.driver.find_element(by, value).send_keys(text)
        allure.attach(body=self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)

    def exception_handle(self):
        # 判断是否有电话打进来
        page = self.driver.page_source
        if 'package="com.android.systemui" class="android.widget.Button"' in self.driver.page_source:
            # 拒绝电话
            self.click(by=AppiumBy.ACCESSIBILITY_ID, value="Decline")
        elif 'package="com.tencent.wework" class="android.widget.TextView" text="编辑成员"' in self.driver.page_source:
            size = self.driver.get_window_size()
            width = size["width"]
            height = size["height"]
            self.driver.swipe(width * 0.5, height * 0.9, width * 0.5, height * 0.1)
