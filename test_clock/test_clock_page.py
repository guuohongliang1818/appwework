# 姓名：郭宏亮
# 时间：2023/5/23 20:40
import pytest

from src.clock.main_page import MainPage


class TestClockPage:

    def setup_class(self):
        self.main_page = MainPage()

    def teardown_class(self):
        self.main_page.close()

    @pytest.mark.parametrize("city", ["Beijing"])
    def test_to_clock_page(self, city):
        self.main_page.to_clock_page().add_city(city).cancel_city(city)
