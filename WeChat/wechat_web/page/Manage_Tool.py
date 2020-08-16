from time import sleep

from wechat_web.comment.base import Base


class ManageTool(Base):
    url = 'https://work.weixin.qq.com/wework_admin/frame#manageTools'
    def mass_message(self):
        self.driver.find_element_by_link_text('选择需要发消息的应用').click()
        self.css_selector('[data-name="自动机器人"]').click()
        self.driver.find_element_by_link_text('确定').click()
        self.driver.find_element_by_link_text('选择发送范围').click()
        self.driver.find_element_by_link_text('曾传途').click()
        self.driver.find_element_by_link_text('确认').click()
        self.css_selector('.js_send_msg_text').send_keys('123456')

    def memberJoin(self):
        pass


    def material(self):
        sleep(2)
        self.css_selector('[href="#material/text"]').click()
        self.driver.find_element_by_link_text('添加文字').click()
        self.css_selector('[placeholder="直接开始输入"]').send_keys('123456')

