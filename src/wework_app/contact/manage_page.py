# 姓名：郭宏亮
# 时间：2023/5/27 21:09
from time import sleep

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

from src.wework_app.contact.add_person_page import AddPersonPage
from src.wework_app.contact.contact_page import ContactPage
from src.wework_app.util_page.base_page import BasePage


class ManagePage(BasePage):
    _cancel = dict(by=AppiumBy.ID, value="com.tencent.wework:id/lf0")
    _edit = dict(by=AppiumBy.ID, value="com.tencent.wework:id/jeo")
    # 删除成员按钮
    _delete_person = dict(by=AppiumBy.XPATH, value="//*[@text='删除成员']")
    # 详情页面名字
    _person_name = dict(by=AppiumBy.ID, value="com.tencent.wework:id/c1a")

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

    # 进入编辑员工的页面，点击删除按钮，跳转到删除员工的页面
    def to_delete_person_page(self):
        lst = self.driver.find_elements(**self._edit)
        if len(lst) > 1:
            # 进入编辑详情页面
            lst[1].click()
            # 获取离职人的名字
            depart_name = self.find_element(**self._person_name).get_attribute("text")
            print("depart_name：", depart_name)
            # 找到删除成员的按钮
            size = self.driver.get_window_size()
            width = size["width"]
            height = size["height"]

            def to_swipe(driver):
                driver.swipe(width * 0.5, height * 0.9, width * 0.5, height * 0.1)
                sleep(0.5)
                return driver.find_element(**self._delete_person)

            WebDriverWait(self.driver, 10).until(to_swipe).click()
            from src.wework_app.contact.delete_person_page import DeletePersonPage
            return DeletePersonPage(self.driver, depart_name)

        # 停留在管理页面
        return self

    # 子类DeletePersonPage重写该方法
    def delete_person(self):
        return self

    def handle_depart(self):
        return self
