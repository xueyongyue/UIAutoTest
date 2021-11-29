# 定义工具类
import time

from selenium import webdriver
from appium import webdriver as app_driver
from selenium.webdriver.common.by import By


class UtilsDriver:
    _mp_driver = None  # 表示的是自媒体平台的浏览器驱动
    _mis_driver = None  # 表示的是后台管理的浏览器驱动
    _app_driver = None  # 表示的是app的驱动

    # 定义获取自媒体平台的浏览器驱动
    @classmethod
    def get_mp_driver(cls):
        if cls._mp_driver is None:
            cls._mp_driver = webdriver.Chrome()
            cls._mp_driver.maximize_window()
            cls._mp_driver.get("http://ttmp.research.itcast.cn/")
        return cls._mp_driver

    # 定义退出自媒体平台的浏览器驱动
    @classmethod
    def quit_mp_driver(cls):
        if cls._mp_driver is not None:
            cls.get_mp_driver().quit()
            cls._mp_driver = None

    # 定义获取后台管理系统的浏览器驱动
    @classmethod
    def get_mis_driver(cls):
        if cls._mis_driver is None:
            cls._mis_driver = webdriver.Chrome()
            cls._mis_driver.maximize_window()
            cls._mis_driver.get("http://ttmis.research.itcast.cn/")
        return cls._mis_driver

    # 定义退出后台管理系统操作方法
    @classmethod
    def quit_mis_driver(cls):
        if cls._mis_driver is not None:
            cls.get_mis_driver().quit()
            cls._mis_driver = None

    # 定义获取app的驱动
    @classmethod
    def get_app_driver(cls):
        if cls._app_driver is None:
            des_cap = {
                "platformName": "android",  # 表示的是android  或者ios
                "platformVersion": "5.1.1",  # 表示的是平台系统的版本号
                "deviceName": "****",  # 表示的是设备的ID名称（如果只有一个设备可以用****来代替）
                "appPackage": "com.itcast.toutiaoApp",  # 表示app的包名
                "appActivity": ".MainActivity",  # 表示的是app的界面名
                "noReset": True,  # 用来记住app的session，如果有登陆或做过初始化的操作，为True时，后面不需要再操作
                "resetKeyboard": True,  # 重置设备的输入键盘
                "unicodeKeyboard": True  # 采用unicode编码输入
            }
            cls._app_driver = app_driver.Remote("http://127.0.0.1:4723/wd/hub", des_cap)
        return cls._app_driver

    # 定义退出app驱动的方法
    @classmethod
    def quit_app_driver(cls):
        if cls._app_driver is not None:
            cls.get_app_driver().quit()
            cls._app_driver = None


# 封装一个选择频道的方法
def choice_channel(driver, element, channel):
    """
    :param driver:  浏览器驱动对象
    :param element:  元素对象
    :param channel:  要选择的文本内容
    :return:
    """
    element.click()
    time.sleep(1)
    xpath = "//*[@class='el-select-dropdown__wrap el-scrollbar__wrap']//*[text()='{}']".format(channel)
    driver.find_element(By.XPATH, xpath).click()


# 封装一个方法判断元素是否存在
def is_exist(driver, text):
    """
    :param driver:  浏览器驱动对象
    :param text:   定位元素的文本内容
    :return:
    """
    xpath = "//*[contains(text(), '{}')]".format(text)
         #   //*[contains(text(), '新增文章成功']
    try:
        time.sleep(2)
        return driver.find_element(By.XPATH, xpath)
    except Exception as e:
        return False
