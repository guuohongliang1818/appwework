# 姓名：郭宏亮
# 时间：2023/5/27 21:00
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

from src.wework_app.contact.add_person_page import AddPersonPage
from src.wework_app.contact.show_person_detail_page import ShowPersonDetailPage
from src.wework_app.util_page.base_page import BasePage


class ContactPage(BasePage):
    # 搜索按钮
    _search = dict(by=AppiumBy.ID, value="com.tencent.wework:id/lf_")
    # 文本输入框
    _input_text = dict(by=AppiumBy.ID, value="com.tencent.wework:id/jn1")
    # 管理按钮
    _manage = dict(by=AppiumBy.ID, value="com.tencent.wework:id/lf5")
    # 个人详情按钮
    _person_detail = dict(by=AppiumBy.ID, value="com.tencent.wework:id/f_k")
    # 退出搜索按钮
    _cancel_search = dict(by=AppiumBy.ID, value="com.tencent.wework:id/lea")

    def to_search_person(self, name):
        self.click(**self._search)
        self.send_keys(**self._input_text, text=name)
        return self

    def to_search_sub_department(self, sub_department):
        self.click(**self._search)
        self.send_keys(**self._input_text, text=sub_department)
        sub_department = self.find_element(by=AppiumBy.XPATH,
                                           value="//android.widget.TextView[@text='" + sub_department + "']").text
        return sub_department

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

        WebDriverWait(self.driver, 5).until(to_swipe).click()
        return AddPersonPage(self.driver)

    def to_show_person_detail(self):
        # 进入个人详情页面
        self.find_elements(**self._person_detail)[0].click()
        # self.click(**self._person_detail)
        return ShowPersonDetailPage(self.driver)

    def cancel_search(self):
        self.click(**self._cancel_search)
        return self
