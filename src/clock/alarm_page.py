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
        # 打开闹铃
        content_str = time_str[0] + ":" + time_str[1] + " " + "AM"
        ele = self.find_element(by=AppiumBy.XPATH,
                                value="//android.view.ViewGroup"
                                      "[contains(@content-desc,'" + content_str + "')]/android.widget.Switch")
        if ele.get_attribute("text") == "OFF":
            ele.click()
        print("添加闹铃成功")
        return self

    def delete_alarm(self):
        lst = self.find_elements(**self._drop)
        for ele in lst:
            sleep(0.3)
            if ele.get_attribute("content-desc") == "Expand alarm":
                ele.click()
            sleep(0.3)
            self.click(**self._delete)
        return self


if __name__ == '__main__':
    s = ("08", "23", "PM")
    print("s:", type(s))
    print(s[0])
    print(s[1])
    for i in ["zhangsan", "lisi"]:
        print(i)
