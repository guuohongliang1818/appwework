# 姓名：郭宏亮
# 时间：2023/5/23 20:50
from appium.webdriver.common.appiumby import AppiumBy

from src.clock.base_page import BasePage


class ClockPage(BasePage):
    # 跳转添加城市页面的按钮
    _add_city = dict(by=AppiumBy.ACCESSIBILITY_ID, value="Cities")
    # 搜索按钮
    _search_button = dict(by=AppiumBy.ID, value="com.android.deskclock:id/search_button")
    # 输入文本信息
    _input_text = dict(by=AppiumBy.ID, value="com.android.deskclock:id/search_src_text")
    # 返回按钮
    _back = dict(by=AppiumBy.ACCESSIBILITY_ID, value="Navigate up")

    def __init__(self, driver):
        super().__init__(driver)

    def add_city(self, city):
        self.click(**self._add_city_button)
        self.click(**self._search_button)
        self.send_keys(**self._input_text, text=city)
        self.click(by=AppiumBy.XPATH, value="//android.widget.CheckBox[@content-desc='" + city + "']")
        self.click(**self._back)
        return self

    def cancel_city(self, city):
        self.click(**self._add_city_button)
        self.click(**self._search_button)
        if 'class="android.widget.TextView" text="Selected Cities"' in self.driver.page_source:
            self.click(by=AppiumBy.XPATH, value="//android.widget.CheckBox[@content-desc='" + city + "']")
        self.click(**self._back)
        return self
