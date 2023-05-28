# 姓名：郭宏亮
# 时间：2023/5/27 21:00
from appium.webdriver.common.appiumby import AppiumBy

from src.wework_app.contact.show_person_detail_page import ShowPersonDetailPage
from src.wework_app.util_page.base_page import BasePage


class ContactPage(BasePage):
    _manage = dict(by=AppiumBy.ID, value="com.tencent.wework:id/lf5")

    def to_search(self):
        pass

    def to_manage_page(self):
        self.click(**self._manage)
        # 解救循环依赖，局部导入
        from src.wework_app.contact.manage_page import ManagePage
        return ManagePage()

    def to_add_person_page(self):
        print("=========")
        # self.driver.find_element().click()
        # return AddPersonPage()

    def to_show_person_detail(self):
        return ShowPersonDetailPage()
