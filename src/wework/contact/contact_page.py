# 姓名：郭宏亮
# 时间：2023/5/27 21:00
from src.wework.contact.add_person_page import AddPersonPage
from src.wework.contact.show_person_detail_page import ShowPersonDetailPage


class ContactPage:

    def to_search(self):
        pass

    def to_manage_page(self):
        return ManagePage()

    def to_add_person_page(self):
        return AddPersonPage()

    def to_show_person_detail(self):
        return ShowPersonDetailPage()
