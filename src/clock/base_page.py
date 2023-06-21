# 姓名：郭宏亮
# 时间：2023/5/22 22:14
import allure
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.remote.webdriver import WebDriver


def retry(func):
    def inner(*args, **kwargs):
        # 找到当前的对象
        po = args[0]
        func_info = f"{func.__name__}({args},{kwargs})"
        try:
            r = func(*args, **kwargs)
            print(f"{r}={func_info}")
            allure.attach(name=func_info,
                          body=po.driver.get_screenshot_as_png(),
                          attachment_type=allure.attachment_type.PNG)
            return r
        except:
            allure.attach(name=func_info,
                          body=po.driver.get_screenshot_as_png(),
                          attachment_type=allure.attachment_type.PNG)
            po.handle_exception()
            inner(*args, **kwargs)

    return inner


class BasePage:

    def __init__(self, driver=None, caps=None):
        if driver is not None:
            self.driver: WebDriver = driver
        else:
            if caps is None:
                caps = {}
            caps["platformName"] = "android"
            caps["settings[waitForIdleTimeout]"] = 0
            caps["settings[enableMultiWindows]"] = True
            caps["appium:ensureWebviewsHavePages"] = True
            caps["appium:nativeWebScreenshot"] = True
            caps["appium:newCommandTimeout"] = 3600
            caps["appium:connectHardwareKeyboard"] = True
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            self.driver.implicitly_wait(5)

    def close(self):
        self.driver.quit()

    @retry
    def back(self):
        self.driver.back()

    @retry
    def click(self, by, value):
        """
        自动截图
        :return:
        """
        self.driver.find_element(by, value).click()

    @retry
    def send_keys(self, by, value, text):
        temp = self.driver.find_element(by, value)
        temp.clear()
        temp.send_keys(text)

    @retry
    def find_elements(self, by, value):
        return self.driver.find_elements(by, value)

    @retry
    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def handle_exception(self):
        if 'package="com.android.systemui" class="android.widget.Button" text="DECLINE" content-desc="Decline"' in self.driver.page_source:
            self.click(by=AppiumBy.ACCESSIBILITY_ID, value="Decline")
        # 用户调查，广告，调查，升级
        elif 'package="com.android.dialer" class="android.widget.TextView" text="Swipe down to reject" resource-id="com.android.dialer:id/incoming_swipe_to_reject_text"' in self.driver.page_source:
            size = self.driver.get_window_size()
            width = size["width"]
            height = size["height"]
            self.driver.swipe(width * 0.5, height * 0.3, width * 0.5, height * 0.7)
        # 回到桌面
        elif 'package="com.android.systemui" class="android.widget.FrameLayout" text="" resource-id="com.android.systemui:id/navigation_bar_frame"' in self.driver.page_source:
            package = "com.android.deskclock"
            activity = "com.android.deskclock.DeskClock"
            self.driver.start_activity(app_package=package, app_activity=activity)
