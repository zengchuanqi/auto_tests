import logging
from time import sleep

import yaml
from appium import webdriver
from appium.webdriver import WebElement
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    driver: WebDriver
    black_list = [
        (By.ID, 'tv_agree'),
        (By.XPATH, '//*[@text="确定"]'),
        (By.ID, 'image_cancel'),
        (By.XPATH, '//*[@text="下次再说"]'),
        (By.XPATH, '//*[@text="取消"]')
    ]
    max_find = 0

    # 设备信息
    def __init__(self):
        caps = {}
        caps["platformName"] = "android"
        caps["platformVersion"] = "6"
        caps["deviceName"] = "xueqiu"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".common.splash.SplashActivity"
        # caps["noReset"] = True
        caps['dontStopAppOnReset'] = True
        caps["chromedriverExecutable"] = r"D:\webdrivers\chromedriver57.exe"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    # 处理各种弹框
    def find_element(self, locator, values:str=None):
        logging.info(locator)
        logging.info(values)
        try:
            if isinstance(locator, tuple):
                ele = self.driver.find_element(*locator)
            else:
                ele = self.driver.find_element(locator, values)
            self.max_find = 0
            return ele
        except Exception:
            print(self.max_find)
            self.max_find += 1
            if self.max_find > 3:
                raise Exception
            for element in self.black_list:
                eles = self.driver.find_elements(*element)
                if len(eles) > 0:
                    eles[0].click()
                    return self.find_element(locator, values)

    # 读取yaml文件
    @classmethod
    def yaml_load(self):
        with open('../data/searchdata.yaml', 'r', encoding='utf-8') as f:
            return (yaml.safe_load(f))

    def steps(self):
        with open('../data/step.yaml') as f:
            steps: list[dict] = yaml.safe_load(f)
            # print(steps)
            element: WebElement = None
            for step in steps:
                # logging.info(step)
                if 'by' in step.keys():
                    element = self.find_element(step['by'], step['locator'])
                if 'action' in step.keys():
                    action = step['action']
                    if action == "find":
                        pass
                    elif action == 'click':
                        element.click()

    def find_text(self, key):
        return self.find_element(By.XPATH, '//*[@text="%s"]' % key)


    def wait_main(self):
        def wait(driver):
            source = self.driver.page_source
            if "我的" in source:
                return True
            if "同意" in source:
                return True
            return False

        WebDriverWait(self.driver, 30).until(wait)
        return self
