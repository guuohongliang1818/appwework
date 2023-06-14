# 姓名：郭宏亮
# 时间：2023/5/27 21:09
from time import sleep

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

from src.wework_app.contact.add_person_page import AddPersonPage
from src.wework_app.contact.contact_page import ContactPage
from src.wework_app.util_page.base_page import BasePage


class ManagePage(BasePage):
    # 管理通讯录
    _manage_contact = dict(by=AppiumBy.ID, value="com.tencent.wework:id/len")
    # 蓝天科技有限公司/非公司名称
    _blue_sky_tech = dict(by=AppiumBy.ID, value="com.tencent.wework:id/let")

    _cancel_manage = dict(by=AppiumBy.ID, value="com.tencent.wework:id/lf0")
    # 编辑员工操作按钮：com.tencent.wework:id/j_a
    _edit = dict(by=AppiumBy.ID, value="com.tencent.wework:id/jeo")

    # 管理通讯录公司下部门的定位标记
    _department = dict(by=AppiumBy.ID, value="com.tencent.wework:id/mid1Txt")
    # 管理通讯录部门下部门的定位标记(部门嵌套部门)
    _department_xpath = dict(by=AppiumBy.XPATH,
                             value="//*[@class='androidx.recyclerview.widget.RecyclerView']"
                                   "/android.view.ViewGroup[1]"
                                   "/android.widget.TextView[@resource-id='com.tencent.wework:id/mid1Txt'][1]")
    _flag = True

    # 删除成员按钮
    _delete_person = dict(by=AppiumBy.XPATH, value="//*[@text='删除成员']")
    # 详情页面名字
    _person_name = dict(by=AppiumBy.ID, value="com.tencent.wework:id/c1a")
    # 在输入子部门弹框，输入子部门名称
    _input_sub_department = dict(by=AppiumBy.ID, value="com.tencent.wework:id/cmj")
    # 确定输入的部门名称
    _confirm_sub_department = dict(by=AppiumBy.ID, value="com.tencent.wework:id/cmw")
    # 确定删除部门按钮
    _confirm_delete_department = dict(by=AppiumBy.ID, value="com.tencent.wework:id/cmw")

    def __init__(self, driver=None):
        super().__init__(driver)
        size = self.driver.get_window_size()
        self.width = size["width"]
        self.height = size["height"]

    def to_add_person_page(self):
        self.click(by=AppiumBy.XPATH, value="//*[@text='添加成员']")
        return AddPersonPage(self.driver)

    def to_add_sub_department(self, sub_depart):
        self.click(by=AppiumBy.XPATH, value="//*[@text='添加子部门']")
        self.send_keys(**self._input_sub_department, text=sub_depart)
        self.click(**self._confirm_sub_department)
        return self

    def to_more_manage_page(self):
        self.click(by=AppiumBy.XPATH, value="//*[@text='更多管理']")
        self.click(by=AppiumBy.XPATH, value="//*[@text='删除部门']")
        self.click(**self._confirm_delete_department)
        return self

    def cancel_manage(self):
        self.click(**self._cancel_manage)
        return ContactPage(self.driver)

    # 进入编辑员工的页面，点击删除按钮，跳转到删除员工的页面，可进行删除员工，办理离职，取消等功能
    def to_delete_person_page(self):
        lst = self.driver.find_elements(**self._edit)
        if len(lst) > 1:
            # 进入编辑详情页面
            lst[1].click()
            # 获取离职人的名字
            depart_name = self.find_element(**self._person_name).get_attribute("text")
            print("depart_name：", depart_name)

            # 找到删除成员的按钮
            def to_swipe(driver):
                driver.swipe(self.width * 0.5, self.height * 0.9, self.width * 0.5, self.height * 0.1)
                sleep(0.5)
                return driver.find_element(**self._delete_person)

            WebDriverWait(self.driver, 3).until(to_swipe).click()
            from src.wework_app.contact.delete_person_page import DeletePersonPage
            return DeletePersonPage(self.driver, depart_name)

        # 停留在管理页面
        return self

    # 子类DeletePersonPage重写该方法
    def delete_person(self):
        return self

    def handle_depart(self):
        return self

    def cancel_delete(self):
        return self

    def to_find_sub_department_manage(self, sub_depart):
        # 滑动窗口找到创建的部门，可进行添加员工操作
        def to_swipe(driver):
            driver.swipe(self.width * 0.5, self.height * 0.9, self.width * 0.5, self.height * 0.1)
            sleep(0.5)
            return driver.find_element(by=AppiumBy.XPATH, value="//*[@text='" + sub_depart + "']")

        WebDriverWait(self.driver, 5).until(to_swipe).click()
        return self

    # 该方法为批量递归删除部门员工信息，如果部门没有员工，则删除部门信息
    def to_recursive_delete_department_person(self):
        """
        逻辑补充：
            首先判断一下是是不是公司管理页面
            if 管理通讯录：
                获取列表的第2条信息
                if 该条目是人员信息：
                    进入人员详情页面，
                    点击删除成员按钮，
                    进行删除操作
                    删除成功进入部门管理页面
                    return
                else 进入部门管理页面：
                    获取该列表的第1条信息：
                    if 有第一条信息：
                        进入人员详情页面
                        点击删除成员按钮，
                        进行删除操作
                        删除成功进入部门管理页面
                        return
                    else
                        删除部门
                        return
            else
                进入人员详情页面，
                点击删除成员按钮，
                进行删除操作
                删除成功进入部门管理页面
                return
        """
        sleep(0.5)
        lst1 = self.driver.find_elements(**self._manage_contact)
        is_manage_contact = False
        if len(lst1) > 0:
            is_manage_contact = "管理通讯录" == lst1[0].get_attribute("text")

        if is_manage_contact:
            # 公司管理通讯录页面和部门管理通讯录页面
            page_source1 = self.driver.page_source
            print("page_source111==", page_source1)
            lst2 = self.driver.find_elements(**self._edit)
            if len(lst2) > 1:  # 如果大于1，则进行删除成员的操作
                lst2[1].click()
                return self.to_recursive_delete_department_person()
            elif len(lst2) == 1:  # 如果==1，则进行删除部门中的成员操作
                page_source2 = self.driver.page_source
                print("page_source222==", page_source2)
                lst3 = self.driver.find_elements(
                    **(self._department if self._flag else self._department_xpath))  # 查部门列表看
                if len(lst3) > 0:  # 如果部门列表大于0，则进入部门中
                    lst3[0].click()
                    self._flag = False
                    return self.to_recursive_delete_department_person()
                else:
                    return self.to_more_manage_page()
            return self
        else:
            # 编辑成员页面
            # 获取离职人的名字
            depart_name = self.find_element(**self._person_name).get_attribute("text")
            print("depart_name：", depart_name)

            # 找到删除成员的按钮
            def to_swipe(driver):
                driver.swipe(self.width * 0.5, self.height * 0.9, self.width * 0.5, self.height * 0.1)
                sleep(0.5)
                return driver.find_element(**self._delete_person)

            WebDriverWait(self.driver, 3).until(to_swipe).click()
            from src.wework_app.contact.delete_person_page import DeletePersonPage
            return DeletePersonPage(self.driver, depart_name)
