# 姓名：郭宏亮
# 时间：2023/5/27 21:04
from appium.webdriver.common.appiumby import AppiumBy


from src.wework_app.util_page.base_page import BasePage


class AddPersonPage(BasePage):
    _input_name = dict(by=AppiumBy.ID, value="com.tencent.wework:id/c1a")
    _input_phone = dict(by=AppiumBy.ID, value="com.tencent.wework:id/iaq")
    _save = dict(by=AppiumBy.ID, value="com.tencent.wework:id/b0b")
    _to_write = dict(by=AppiumBy.XPATH, value="//*[@text='手动输入添加']")

    def __init__(self, driver=None):
        super().__init__(driver=driver)

    # 定义6种添加成员的方法
    def to_wechat_invite(self):
        return self

    def to_face_to_face_invite(self):
        return self

    def to_add_from_group(self):
        return self

    def to_add_from_contacts(self):
        return self

    def to_write(self, name, phone):
        self.click(**self._to_write)
        self.send_keys(**self._input_name, text=name)
        self.send_keys(**self._input_phone, text=phone)
        self.click(**self._save)
        # 返回添加成员页面
        return self

    def to_upload_sheet(self):
        return self

    def back_manage_page(self):
        # 必须找到“手动输入添加”添加这个按钮，才能返回，否则不报错，也不会有返回
        self.driver.find_element(**self._to_write)
        self.back()
        from src.wework_app.contact.manage_page import ManagePage
        return ManagePage(self.driver)

    def back_contact_page(self):
        # 必须找到“手动输入添加”添加这个按钮，才能返回，否则不报错，也不会有返回
        self.driver.find_element(**self._to_write)
        self.back()
        from src.wework_app.contact.contact_page import ContactPage
        return ContactPage(self.driver)
