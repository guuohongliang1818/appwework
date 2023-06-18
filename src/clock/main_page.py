# 姓名：郭宏亮
# 时间：2023/5/22 21:18
from appium.webdriver.common.appiumby import AppiumBy

from src.clock.alarm_page import AlarmPage
from src.clock.base_page import BasePage
from src.clock.clock_page import ClockPage
from src.clock.stopwatch_page import StopwatchPage
from src.clock.timer_page import TimerPage


class MainPage(BasePage):

    def __init__(self, driver=None):
        # 在初始化main_page的时候，已经将driver初始化完毕
        caps = {}
        # 桌面点击clock按钮，进入了alarm，timer，clock，stopwatch主页，由如下四个跳转功能
        caps["appPackage"] = "com.android.deskclock"
        caps["appActivity"] = "com.android.deskclock.DeskClock"
        super().__init__(driver, caps)

    def to_alarm_page(self):
        self.driver.find_element(by=AppiumBy.XPATH,
                                 value="//androidx.appcompat.app.ActionBar.Tab[@content-desc='Alarm']"
                                       "/android.widget.TextView").click()
        return AlarmPage(self.driver)

    def to_clock_page(self):
        self.driver.find_element(by=AppiumBy.XPATH,
                                 value="//androidx.appcompat.app.ActionBar.Tab[@content-desc='Clock']"
                                       "/android.widget.TextView").click()
        return ClockPage(self.driver)

    def to_timer_page(self):
        self.driver.find_element(by=AppiumBy.XPATH,
                                 value="//androidx.appcompat.app.ActionBar.Tab[@content-desc='Timer']"
                                       "/android.widget.TextView").click()
        return TimerPage(self.driver)

    def to_stopwatch_page(self):
        self.driver.find_element(by=AppiumBy.XPATH,
                                 value="//androidx.appcompat.app.ActionBar.Tab[@content-desc='Stopwatch']"
                                       "/android.widget.TextView").click()
        return StopwatchPage(self.driver)
