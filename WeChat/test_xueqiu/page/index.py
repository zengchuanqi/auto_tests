import pytest
from selenium.webdriver.common.by import By

from test_xueqiu.comment.base import Base
from test_xueqiu.page.my import My


class Index(Base):

    def search(self,name,stoke):
        self.find_element(By.ID,'home_search').click()
        self.find_element(By.ID,'search_input_text').send_keys(name)
        print(name, stoke)
        self.find_element(By.XPATH, "//*[@text ='{}' and contains(@resource-id,'code')]".
                            format(stoke)).click()

        self.find_element(By.XPATH,
                          '//*[contains(@resource-id,"title_text")and @text="股票"]').click()

        text = self.find_element(By.XPATH,
            "//*[@text='{}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']"
                .format(stoke)).text
        text = float(text)
        print(text)

    def goto_my(self):
        self.find_element(By.XPATH,"//*[contains(@resource-id,'tab_name') and @text='我的']").click()
        return My()