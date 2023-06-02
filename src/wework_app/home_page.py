# 姓名：郭宏亮
# 时间：2023/5/26 22:39
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from src.wework_app.contact.contact_page import ContactPage
from src.wework_app.util_page.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver=None):
        # com.tencent.wework/com.tencent.wework.launch.LaunchSplashActivity
        caps = {}
        caps["noReset"] = True
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        super().__init__(driver, caps)

    def to_message(self):
        self.click(by=AppiumBy.XPATH, value="//*[@text='消息']")
        return self

    def to_email(self):
        pass

    def to_document(self):
        pass

    def to_workbench(self):
        pass

    def to_contact(self):
        self.click(by=AppiumBy.XPATH, value="//*[@text='通讯录']")
        return ContactPage(self.driver)
