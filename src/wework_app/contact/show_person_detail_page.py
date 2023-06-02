# 姓名：郭宏亮
# 时间：2023/5/27 21:15
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from src.wework_app.util_page.base_page import BasePage


class ShowPersonDetailPage(BasePage):
    _name = dict(by=AppiumBy.ID, value="com.tencent.wework:id/kps")
    _email = dict(by=AppiumBy.ID, value="com.tencent.wework:id/c22")

    def __init__(self, driver=None):
        super().__init__(driver)

    def get_show_person_detail(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((AppiumBy.XPATH, "//*[@text='个人信息']")))
        name = self.find_element(**self._name).text
        email = self.find_element(**self._email).text

        return {"name": name, "email": email}

    def two_step_back_contact_page(self):
        self.back()
        self.back()
        from src.wework_app.contact.contact_page import ContactPage
        return ContactPage(self.driver)

    def one_step_back_contact_page(self):
        self.back()
        self.back()
        from src.wework_app.contact.contact_page import ContactPage
        return ContactPage(self.driver)
