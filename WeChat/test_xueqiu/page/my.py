from selenium.webdriver.common.by import By

from test_xueqiu.comment.base import Base


class My(Base):

    def login_in(self):
        self.find_element(By.XPATH,"//*[contains(@resource-id,'tab_name') and @text='我的']").click()
        self.find_element(By.ID,"com.xueqiu.android:id/rl_login").click()
        self.find_element(By.ID,"com.xueqiu.android:id/login_account").send_keys("17872301006")