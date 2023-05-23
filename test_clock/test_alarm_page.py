# 姓名：郭宏亮
# 时间：2023/5/23 21:01
from src.clock.main_page import MainPage


class TestAlarmPage:

    def setup_class(self):
        self.main_page = MainPage()

    def test_to_alarm_page(self):
        self.main_page.to_alarm_page().say()
