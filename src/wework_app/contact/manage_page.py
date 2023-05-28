# 姓名：郭宏亮
# 时间：2023/5/27 21:09
from appium.webdriver.common.appiumby import AppiumBy

from src.wework_app.contact.add_person_page import AddPersonPage
from src.wework_app.contact.contact_page import ContactPage
from src.wework_app.util_page.base_page import BasePage


class ManagePage(BasePage):
    _cancel = dict(by=AppiumBy.ID, value="com.tencent.wework:id/lf0")

    def to_add_person_page(self):
        self.click(by=AppiumBy.XPATH, value="//*[@text='添加成员']")
        return AddPersonPage()

    def to_add_sub_department(self):
        return

    def more_manage_page(self):
        return

    def cancel_manage(self):
        print("取消管理界面111")
        self.click(**self._cancel)
        print("取消管理界面222")
        return ContactPage()
