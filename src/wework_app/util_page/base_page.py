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
            # self.driver.implicitly_wait(40)

    def close(self):
        self.driver.quit()

    def back(self):
        self.driver.back()

    def click(self, by, value):
        try:
            self.driver.find_element(by, value).click()
            allure.attach(body=self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
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
        if "package='com.android.systemui' class='android.widget.Button'" in self.driver.page_source:
            # 拒绝电话
            self.click(by=AppiumBy.ACCESSIBILITY_ID, value="Decline")
        if "" in self.driver.page_source:
            pass
