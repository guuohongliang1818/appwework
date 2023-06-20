# 姓名：郭宏亮
# 时间：2023/5/23 21:01
import pytest

from src.clock.main_page import MainPage


class TestAlarmPage:

    def setup_class(self):
        self.main_page = MainPage()

    @pytest.mark.parametrize("time_str", [("8", "15"), ("9", "15"), ("10", "15"), ("11", "15")])
    def test_to_alarm_page(self, time_str):
        self.main_page.to_alarm_page().add_alarm(time_str)

    def test_delete_alarm(self):
        self.main_page.to_alarm_page().delete_alarm()

    def teardown_class(self):
        self.main_page.close()
