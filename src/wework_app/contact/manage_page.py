# 姓名：郭宏亮
# 时间：2023/5/27 21:09
from appium.webdriver.common.appiumby import AppiumBy

from src.wework_app.contact.add_person_page import AddPersonPage
from src.wework_app.contact.contact_page import ContactPage
from src.wework_app.util_page.base_page import BasePage


class ManagePage(BasePage):
    _cancel = dict(by=AppiumBy.ID, value="com.tencent.wework:id/lf0")

    def __init__(self, driver=None):
        super().__init__(driver=driver)
        lst = self.driver.find_elements(by=AppiumBy.XPATH, value="//android.view.ViewGroup")
        for item in lst:
            print("-----------")

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
