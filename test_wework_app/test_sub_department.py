# 姓名：郭宏亮
# 时间：2023/6/5 9:19
import pytest
import datetime
from src.wework_app.home_page import HomePage


class TestSubDepartment:
    def setup_class(self):
        self.home_page = HomePage()

    def setup_method(self):
        # 每次都从首页切换到通讯录，可以获取最新的成员数据
        self.contact_page = self.home_page.to_message().to_contact()

    def teardown_class(self):
        pass

    # 添加部门
    @pytest.mark.parametrize("sub_department", ["部门1", "部门2", "部门3"])
    def test_add_sub_department(self, sub_department):
        contact_page = self.contact_page \
            .to_manage_page() \
            .to_add_sub_department(sub_department) \
            .cancel_manage()
        assert sub_department == contact_page.to_search_sub_department(sub_department)
        contact_page.back()

    # 递归删除成员和部门成员
    @pytest.mark.parametrize("count", range(1, 20))
    def test_to_recursive_delete_department_person(self, count):
        self.contact_page \
            .to_manage_page() \
            .to_recursive_delete_department_person() \
            .delete_person() \
            .cancel_manage()

    @pytest.mark.parametrize("sub_department", ["部门1", "部门2"])
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
            .back_contact_page() \
            .to_search_person(name) \
            .to_show_person_detail()

        assert name == show_person_detail_page.get_show_person_detail().get("name")
        # 返回到通讯录页面
        show_person_detail_page.one_step_back_contact_page()
