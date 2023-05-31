# 姓名：郭宏亮
# 时间：2023/5/27 21:09
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from src.wework_app.contact.add_person_page import AddPersonPage
from src.wework_app.contact.contact_page import ContactPage
from src.wework_app.util_page.base_page import BasePage


class ManagePage(BasePage):
    _cancel = dict(by=AppiumBy.ID, value="com.tencent.wework:id/lf0")
    _edit = dict(by=AppiumBy.ID, value="com.tencent.wework:id/jeo")
    _delete_person = dict(by=AppiumBy.XPATH, value="//*[@text='删除成员']")
    _delete = dict(by=AppiumBy.ID, value="com.tencent.wework:id/cw1")

    def __init__(self, driver=None):
        super().__init__(driver=driver)

    def to_add_person_page(self):
        self.click(by=AppiumBy.XPATH, value="//*[@text='添加成员']")
        return AddPersonPage(self.driver)

    def to_add_sub_department(self):
        return

    def more_manage_page(self):
        return

    def cancel_manage(self):
        self.click(**self._cancel)
        return ContactPage(self.driver)

    # 删除员工信息
    def delete_person(self):
        lst = self.driver.find_elements(**self._edit)
        if len(lst) > 1:
            # 进入编辑详情页面
            lst[1].click()
            # 在编辑的详情页面获取移动设备的长度和宽度

            # 找到删除成员的按钮
            self.click(**self._delete_person)

            WebDriverWait(self.driver, 10).until(
                expected_conditions.element_to_be_clickable((AppiumBy.ID, "com.tencent.wework:id/cw1"))).click()

        return self
