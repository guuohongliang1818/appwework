# 姓名：郭宏亮
# 时间：2023/5/26 22:39
from src.wework.contact.search_page import SearchPage

from src.wework.contact.contact_page import ContactPage


class HomePage:

    def to_message(self):
        pass

    def to_email(self):
        pass

    def to_document(self):
        pass

    def to_workbench(self):
        pass

    def to_contact(self):
        return ContactPage()
