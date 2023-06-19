# 姓名：郭宏亮
# 时间：2023/5/23 20:49
from time import sleep

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

from src.clock.base_page import BasePage


class AlarmPage(BasePage):
    # 添加闹铃按钮
    _add_alarm = dict(by=AppiumBy.ACCESSIBILITY_ID, value="Add alarm")
    # 点击键盘按钮
    _click_keyboard = dict(by=AppiumBy.ACCESSIBILITY_ID, value="Switch to text input mode for the time input.")
    # 输入时间_小时(12小时制)
    _input_time_hour = dict(by=AppiumBy.ID, value="android:id/input_hour")
    # 输入时间_分
    _input_time_minute = dict(by=AppiumBy.ID, value="android:id/input_minute")
    # 上下午切换
    _am_pm = dict(by=AppiumBy.ID, value="android:id/am_pm_spinner")
    # 点击ok按钮
    _ok = dict(by=AppiumBy.ID, value="android:id/button1")
    # 打开按钮
    _open_close_alarm = dict(by=AppiumBy.ID, value="com.android.deskclock:id/onoff")
    # 定义闹钟的个数
    _count = 2
    # 下拉箭头
    _drop = dict(by=AppiumBy.ID, value="com.android.deskclock:id/arrow")
    # 删除按钮
    _delete = dict(by=AppiumBy.ID, value="com.android.deskclock:id/delete")

    def __init__(self, driver):
        super().__init__(driver)

    def add_alarm(self, time_str):
        self.click(**self._add_alarm)
        self.click(**self._click_keyboard)
        self.send_keys(**self._input_time_hour, text=time_str[0])
        self.send_keys(**self._input_time_minute, text=time_str[1])
        self.click(**self._ok)
        self._count += 1
        print("闹钟个数count：", self._count)
        return self

    def open_alarm(self):
        # 列表个数==闹铃个数
        if self._count != 0:
            WebDriverWait(self.driver, 3).until(lambda x: len(x.find_elements(**self._open_close_alarm)) == self._count)
            lst = self.find_elements(**self._open_close_alarm)
            for ele in lst:
                if ele.__getattribute__("text") == "OFF":
                    ele.click()
        return self

    def delete_alarm(self):
        sleep(0.5)
        page_source = self.driver.page_source
        lst = self.find_elements(**self._drop)
        for ele in lst:
            text = ele.__getattribute__("content-desc")
            if ele.__getattribute__("content-desc") == "Expand alarm":
                ele.click()
            self.click(**self._delete)
        return self


if __name__ == '__main__':
    s = ("08", "23", "PM")
    print("s:", type(s))
    print(s[0])
    print(s[1])
    for i in ["zhangsan", "lisi"]:
        print(i)
