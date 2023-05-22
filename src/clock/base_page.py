# 姓名：郭宏亮
# 时间：2023/5/22 22:14
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:

    def __init__(self, driver=None):
        self.driver: WebDriver = driver

    def close(self):
        self.driver.quit()

    def back(self):
        pass

    def click(self):
        """
        自动截图
        :return:
        """
        pass

    def send_keys(self):
        pass
