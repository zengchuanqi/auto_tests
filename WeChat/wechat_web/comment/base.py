from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver

class Base:
    url = ''
    def __init__(self,driver:WebDriver = None,reuse=False):
        if driver == None:
            if reuse==True:
                chrome_options = Options()
                chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
                self.driver = webdriver.Chrome(chrome_options=chrome_options)
            else:
                self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(15)
            self.driver.get(self.url)
        else:
            self.driver = driver


    def css_selector(self,locator):
        return self.driver.find_element_by_css_selector(locator)
