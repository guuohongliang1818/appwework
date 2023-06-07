# 姓名：郭宏亮
# 时间：2023/6/2 19:28
from time import sleep

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from src.wework_app.util_page.base_page import BasePage


class DepartPage(BasePage):
    # 发起离职
    _launch_depart = dict(by=AppiumBy.ACCESSIBILITY_ID, value="发起离职")
    # 离职姓名
    _to_input_depart_name = dict(by=AppiumBy.XPATH, value="//android.widget.Button[@index='4']")
    # 离职日期
    _to_input_depart_date = dict(by=AppiumBy.XPATH, value="//android.widget.Button[@index='7']")
    # 离职类型
    _to_input_depart_type = dict(by=AppiumBy.XPATH, value="//android.widget.Button[@index='10']")
    # 离职原因
    _to_input_depart_reason = dict(by=AppiumBy.XPATH, value="//android.widget.Button[@index='13']")

    # 搜索离职人按钮
    _search_depart_name = dict(by=AppiumBy.ID, value="com.tencent.wework:id/lf5")
    _input_depart_name = dict(by=AppiumBy.ID, value="com.tencent.wework:id/jn1")
    _select_depart_name = dict(by=AppiumBy.ID, value="com.tencent.wework:id/jrl")
    # 确认姓名按钮
    _confirm_depart_name_button = dict(by=AppiumBy.ID, value="com.tencent.wework:id/jri")
    # 确认日期按钮
    _confirm_depart_date_button = dict(by=AppiumBy.ACCESSIBILITY_ID, value="确定")
    # 确认发起离职
    _confirm_launch_depart = dict(by=AppiumBy.ACCESSIBILITY_ID, value="确认发起")

    # 离职管理页面，点击搜索发起离职人的姓名
    _search_launch_name = dict(by=AppiumBy.XPATH, value="//android.widget.Button[@index='2']")
    _search_person_name = dict(by=AppiumBy.XPATH, value="//*[contains(@text,'搜索员工姓名')]")

    def __init__(self, driver=None, name=None):
        self.name = name
        super().__init__(driver)

    def launch_depart(self):
        # 有弹出框，确认弹出框已弹出，在取消，并且取消按钮可点击
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "为员工发起离职")))
        sleep(0.5)
        # 取消弹出框
        self.click(by=AppiumBy.ACCESSIBILITY_ID, value="取消")
        # 发起离职
        self.click(**self._launch_depart)
        return self

    def input_depart_info_and_launch(self):
        print("name：", self.name)
        # 因为已离职的xpath与_to_input_depart_name有冲突，
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
            (AppiumBy.ACCESSIBILITY_ID, "发起后，员工将进入待离职状态，请尽快和员工沟通工作交接事宜")))
        # 输入离职姓名
        self.click(**self._to_input_depart_name)
        self.click(**self._search_depart_name)
        self.send_keys(**self._input_depart_name, text=self.name)
        self.click(**self._select_depart_name)
        self.click(**self._confirm_depart_name_button)
        # 输入离职日期
        self.click(**self._to_input_depart_date)
        self.click(**self._confirm_depart_date_button)
        # 输入离职类型
        self.click(**self._to_input_depart_type)
        self.click(by=AppiumBy.XPATH, value="//android.view.View[@content-desc='主动离职']")
        # 输入离职原因
        self.click(**self._to_input_depart_reason)
        self.click(by=AppiumBy.XPATH, value="//android.view.View[@content-desc='薪资福利不满意']")
        # 确认发起离职
        self.click(**self._confirm_launch_depart)
        return self

    def search_and_confirm_depart(self):
        # 只有返回三个元素才能进行点击
        WebDriverWait(self.driver, 3).until(
            lambda x: len(x.find_elements(**self._search_launch_name)) == 3)
        self.find_elements(**self._search_launch_name)[0].click()
        self.send_keys(**self._search_person_name, text=self.name)
        sleep(1)
        print("page_source==2", self.driver.page_source)
        print("value=", "*[content-desc|=" + self.name + "]")
        # WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(
        #     (AppiumBy.XPATH, "//*[contains(@content-desc,'" + self.name[0:1:] + "')]"))).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(
            (AppiumBy.CSS_SELECTOR, "*[content-desc|=" + self.name + "]"))).click()
        # self.click(by=AppiumBy.XPATH, value="//*[contains(@content-desc,'" + self.name + "')]")
        self.click(by=AppiumBy.ACCESSIBILITY_ID, value="确认离职")
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
            (AppiumBy.ACCESSIBILITY_ID, "确认后，员工将被移出通讯录，消息数据将被删除，你可在确认后交接员工的数据资产")))
        self.click(by=AppiumBy.ACCESSIBILITY_ID, value="确认离职")

    def two_step_back_manage_page(self):
        sleep(1)
        self.back()
        sleep(1)
        self.back()
        from src.wework_app.contact.manage_page import ManagePage
        return ManagePage(self.driver)


if __name__ == '__main__':
    s = "赵六03004531"
    print(s[0:1:])
