# 姓名：郭宏亮
# 时间：2023/5/23 20:49
from src.clock.base_page import BasePage


class AlarmPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def say(self):
        print("=======")
