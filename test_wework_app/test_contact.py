# 姓名：郭宏亮
# 时间：2023/5/28 9:38
import datetime

import pytest

from src.wework_app.home_page import HomePage


class TestContact:

    def setup_class(self):
        self.home_page = HomePage()

    def teardown_class(self):
        pass

    def test_to_add_person_m1(self):
        pass

    @pytest.mark.parametrize("name", ["张三"])
    @pytest.mark.parametrize("phone", ["138"])
    def test_to_add_person_m2(self, name, phone):
        phone = phone + datetime.datetime.now().strftime("%d%H%M%S")
        self.home_page.to_contact() \
            .to_manage_page() \
            .to_add_person_page() \
            .to_write(name, phone) \
            .back_manage_page() \
            .cancel_manage()
