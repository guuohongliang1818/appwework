# 姓名：郭宏亮
# 时间：2023/5/27 21:00
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

from src.wework_app.contact.add_person_page import AddPersonPage
from src.wework_app.contact.show_person_detail_page import ShowPersonDetailPage
from src.wework_app.util_page.base_page import BasePage


class ContactPage(BasePage):
    _manage = dict(by=AppiumBy.ID, value="com.tencent.wework:id/lf5")

    def __init__(self, driver=None):
        super().__init__(driver=driver)

    def to_search(self):
        pass

    def to_manage_page(self):
        self.click(**self._manage)
        # 解救循环依赖，局部导入
        from src.wework_app.contact.manage_page import ManagePage
        return ManagePage(self.driver)

    def to_add_person_page(self):
        # 获取移动设备的长度和宽度
        size = self.driver.get_window_size()
        width = size["width"]
        height = size["height"]

        def to_swipe(driver):
            driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.2)
            return driver.find_element(by=AppiumBy.XPATH, value="//*[@text='添加成员']")

        WebDriverWait(self.driver, 10).until(to_swipe).click()
        return AddPersonPage(self.driver)

    def to_show_person_detail(self):
        return ShowPersonDetailPage(self.driver)


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]
    print(len())
