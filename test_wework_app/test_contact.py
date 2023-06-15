# 姓名：郭宏亮
# 时间：2023/5/28 9:38
import datetime

import pytest

from src.wework_app.home_page import HomePage


class TestContact:

    def setup_class(self):
        self.home_page = HomePage()

    def setup_method(self):
        # 每次都从首页切换到通讯录，可以获取最新的成员数据
        self.contact_page = self.home_page.to_message().to_contact()

    def teardown_class(self):
        self.home_page.close()

    # 从通讯录页面添加成员
    @pytest.mark.parametrize("name", ["张三", "李四", "王五", "赵六", "钱七", "孙八", "jack", "8078656"])
    @pytest.mark.parametrize("phone", ["138"])
    def test_to_add_person_m1(self, name, phone):
        name = name + datetime.datetime.now().strftime("%d%H%M%S")
        phone = phone + datetime.datetime.now().strftime("%d%H%M%S")
        show_person_detail_page = self.contact_page \
            .to_add_person_page() \
            .to_write(name, phone) \
            .back_contact_page() \
            .to_search_person(name) \
            .to_show_person_detail()

        assert name == show_person_detail_page.get_show_person_detail().get("name")
        # 返回到通讯录页面
        show_person_detail_page.one_step_back_contact_page()

    # 从管理页面添加成员
    @pytest.mark.parametrize("name", ["张三", "李四", "王五"])
    @pytest.mark.parametrize("phone", ["138"])
    def test_to_add_person_m2(self, name, phone):
        name = name + datetime.datetime.now().strftime("%d%H%M%S")
        phone = phone + datetime.datetime.now().strftime("%d%H%M%S")
        show_person_detail_page = self.contact_page \
            .to_manage_page() \
            .to_add_person_page() \
            .to_write(name, phone) \
            .back_manage_page() \
            .cancel_manage() \
            .to_search_person(name) \
            .to_show_person_detail()
        assert name == show_person_detail_page.get_show_person_detail().get("name")
        # 返回倒通讯录页面
        show_person_detail_page.two_step_back_contact_page()

    # 从管理页面删除成员
    @pytest.mark.parametrize("count", range(1, 6))
    def test_delete_person(self, count):
        # 进入管理页面，点击员工找到删除按钮，进入删除员工页面，点击删除按钮<直接返回管理页面>，取消管理
        self.contact_page \
            .to_manage_page() \
            .to_delete_person_page() \
            .delete_person() \
            .cancel_manage()

    # 办理员工离职测试
    @pytest.mark.parametrize("count", range(1, 11))
    def test_depart(self, count):
        self.contact_page \
            .to_manage_page() \
            .to_delete_person_page() \
            .handle_depart() \
            .cancel_manage()

    # 办理取消删除员工测试
    @pytest.mark.parametrize("count", range(1, 19))
    def test_cancel_delete(self, count):
        # 进入管理页面，点击员工详情，找到删除按员工，弹出删除员工对话框，点击取消，退出详情页面，取消管理
        self.contact_page \
            .to_manage_page() \
            .to_delete_person_page() \
            .cancel_delete() \
            .cancel_manage()

    # 创建部门
    @pytest.mark.parametrize("sub_department", ["部门10", "部门11", "部门12"])
    def test_add_sub_department(self, sub_department):
        contact_page = self.contact_page \
            .to_manage_page() \
            .to_add_sub_department(sub_department) \
            .cancel_manage()
        assert sub_department == contact_page.to_search_sub_department(sub_department)
        contact_page.cancel_search()

    # 为部门10中添加员工
    @pytest.mark.parametrize("sub_department", ["部门10"])
    @pytest.mark.parametrize("name", ["张三", "李四", "王五", "赵六", "钱七", "孙八", "jack", "8078"])
    @pytest.mark.parametrize("phone", ["138"])
    def test_to_add_person_for_department(self, sub_department, name, phone):
        name = name + datetime.datetime.now().strftime("%d%H%M%S")
        phone = phone + datetime.datetime.now().strftime("%d%H%M%S")
        show_person_detail_page = self.contact_page \
            .to_manage_page() \
            .to_find_sub_department_manage(sub_department) \
            .to_add_person_page() \
            .to_write(name, phone) \
            .back_manage_page() \
            .cancel_manage() \
            .to_search_person(name) \
            .to_show_person_detail()

        assert name == show_person_detail_page.get_show_person_detail().get("name")
        # 返回到通讯录页面
        show_person_detail_page.one_step_back_contact_page()

    # 递归删除成员和部门成员
    @pytest.mark.parametrize("count", range(1, 11))
    def test_to_recursive_delete_department_person_for_delete(self, count):
        self.contact_page \
            .to_manage_page() \
            .to_recursive_delete_department_person() \
            .delete_person() \
            .cancel_manage()

    # 递归为员工办理离职和部门成员
    @pytest.mark.parametrize("count", range(1, 11))
    def test_to_recursive_delete_department_person_for_depart(self, count):
        self.contact_page \
            .to_manage_page() \
            .to_recursive_delete_department_person() \
            .handle_depart() \
            .cancel_manage()
