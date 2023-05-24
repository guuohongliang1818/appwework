# 姓名：郭宏亮
# 时间：2023/5/23 21:01
from src.clock.main_page import MainPage


class TestStopwatchPage:

    def setup_class(self):
        self.main_page = MainPage()

    def test_to_stopwatch_page(self):
        self.main_page.to_stopwatch_page()

    def teardown_class(self):
        self.main_page.close()
