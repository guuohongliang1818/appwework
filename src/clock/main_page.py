# 姓名：郭宏亮
# 时间：2023/5/22 21:18
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
        return AlarmPage(self.driver)

    def to_clock_page(self):
        return ClockPage(self.driver)

    def to_timer_page(self):
        return TimerPage(self.driver)

    def to_stopwatch_page(self):
        return StopwatchPage(self.driver)
