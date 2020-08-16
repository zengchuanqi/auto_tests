from wechat_web.comment.base import Base
from wechat_web.page.Manage_Tool import ManageTool
from wechat_web.page.contact import Contacts


class Index(Base):
    url = 'https://work.weixin.qq.com/wework_admin/frame#index'

    def add_member(self):
        self.driver.find_element_by_link_text('添加成员').click()
        return Contacts(self.driver)

    def import_contact(self):
        self.driver.find_element_by_link_text('导入通讯录').click()
        return Contacts(self.driver)

    def member_join(self):
        self.driver.find_element_by_link_text('成员加入').click()
        return ManageTool(self.driver)

    def mass_message(self):
        self.driver.find_element_by_link_text('消息群发').click()
        return ManageTool(self.driver)


    def customer_contact(self):
        pass

    def clock_in(self):
        pass
