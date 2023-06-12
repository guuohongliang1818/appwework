# 姓名：郭宏亮
# 时间：2023/6/5 9:19
import pytest

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
        assert sub_department == self.contact_page.to_manage_page().to_add_sub_department(
            sub_department).cancel_manage().to_search_sub_department(sub_department)

    # 递归删除成员和部门成员
    @pytest.mark.parametrize("count", range(1, 20))
    def test_to_recursive_delete_department_person(self, count):
        self.contact_page \
            .to_manage_page() \
            .to_recursive_delete_department_person() \
            .delete_person() \
            .cancel_manage()
