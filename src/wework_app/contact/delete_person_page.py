# 姓名：郭宏亮
# 时间：2023/6/2 10:49
from time import sleep

from appium.webdriver.common.appiumby import AppiumBy

from src.wework_app.contact.depart_page import DepartPage
from src.wework_app.contact.manage_page import ManagePage


class DeletePersonPage(ManagePage):
    # 删除
    _delete = dict(by=AppiumBy.ID, value="com.tencent.wework:id/cw1")
    # 办理离职
    _handle_depart = dict(by=AppiumBy.ID, value="com.tencent.wework:id/lah")
    # 取消
    _cancel_delete = dict(by=AppiumBy.ID, value="com.tencent.wework:id/bda")

    def __init__(self, driver=None, depart_name=None):
        self.depart_name = depart_name
        super().__init__(driver)

    def delete_person(self):
        self.click(**self._delete)
        return ManagePage(self.driver)

    def handle_depart(self):
        self.click(**self._handle_depart)
        print("DeletePersonPage：", self.depart_name)
        depart_page = DepartPage(self.driver, self.depart_name)
        return_page = depart_page.launch_depart().input_depart_info_and_launch().search_and_confirm_depart()
        return return_page

    def cancel_delete(self):
        self.click(**self._cancel_delete)
        self.back()
        return ManagePage(self.driver)
