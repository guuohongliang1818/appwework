# 姓名：郭宏亮
# 时间：2023/5/28 9:38
import datetime

import pytest

from src.wework_app.home_page import HomePage


class TestContact:

    def setup_class(self):
        self.contact_page = HomePage().to_contact()

    def teardown_class(self):
        pass

    @pytest.mark.parametrize("name", ["张三", "李四", "王五", "赵六", "钱七", "孙八"])
    @pytest.mark.parametrize("phone", ["138"])
    def test_to_add_person_m1(self, name, phone):
        phone = phone + datetime.datetime.now().strftime("%d%H%M%S")
        self.contact_page.to_add_person_page().to_write(name, phone).back_contact_page()

    @pytest.mark.parametrize("name", ["张三", "李四", "王五"])
    @pytest.mark.parametrize("phone", ["138"])
    def test_to_add_person_m2(self, name, phone):
        phone = phone + datetime.datetime.now().strftime("%d%H%M%S")
        self.contact_page \
            .to_manage_page() \
            .to_add_person_page() \
            .to_write(name, phone) \
            .back_manage_page() \
            .cancel_manage()

    def test_delete_person(self):
        # 进入管理页面，删除员工信息，最后取消管理页面，进入通讯录页面
        self.contact_page.to_manage_page().delete_person()
