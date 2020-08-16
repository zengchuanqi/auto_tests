from wechat_web.comment.base import Base


class Customer_contact(Base):
    url='https://work.weixin.qq.com/wework_admin/frame#customer/analysis'
    def productAlbum(self):
        self.driver.find_element_by_link_text('产品图册').click()
        self.driver.find_element_by_link_text('添加').click()
        path = r'E:\11.png'
        self.driver.find_element_by_name('uploadImageFile').send_keys(path)
        self.css_selector('.inputDlg_item_right  .ww_inputText_Big ').send_keys(1000000)
