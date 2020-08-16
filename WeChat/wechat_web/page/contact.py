
from selenium import webdriver

from wechat_web.comment.base import Base


class Contacts(Base):
    # 添加成员
    '''
    name:姓名
    english_name:别名
    acctid：账号
    gender:性别
    mobile:手机号
    telephone:座机号
    email: 邮箱
    address:地址
    '''
    def add_member(self,member_msg):
        self.driver.find_element_by_css_selector('#username').send_keys(member_msg["name"])
        self.driver.find_element_by_css_selector('#memberAdd_english_name').send_keys(member_msg['english_name'])
        self.driver.find_element_by_css_selector('#memberAdd_acctid').send_keys(member_msg['acctid'])
        if member_msg['gender']=='男':
            self.driver.find_element_by_css_selector('[name="gender"][value="1"]').click()
        else:
            self.driver.find_element_by_css_selector('[name="gender"][value="1"]').click()
        self.driver.find_element_by_css_selector('#memberAdd_phone').send_keys(member_msg['mobile'])
        self.driver.find_element_by_css_selector('#memberAdd_telephone').send_keys(member_msg['telephone'])
        self.driver.find_element_by_css_selector('#memberAdd_mail').send_keys(member_msg['email'])
        self.driver.find_element_by_css_selector('#memberEdit_address').send_keys(member_msg['address'])


    def import_contact(self):
        path = r'C:\Users\Administrator\Desktop\interview_data.xls'
        self.css_selector('[value="上传文件"]').send_keys(path)