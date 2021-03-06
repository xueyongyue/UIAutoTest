# 定义测试类
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogin:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://tpshop-test.itheima.net/")
        # 点击登录按钮跳转到登录页面
        self.driver.find_element(By.CSS_SELECTOR, ".red").click()

    # 创建方法级别的fixture初始化的操作方法
    def setup(self):
        self.driver.refresh()

    # 创建类级别fixture销毁的操作方法
    def teardown_class(self):
        self.driver.quit()

    # 定义测试方法  账号不存在
    def test_login_01(self):
        # 点击登录按钮跳转到登录页面
        # self.driver.find_element(By.CSS_SELECTOR, ".red").click()
        # 输入手机号码
        self.driver.find_element(By.ID, "username").send_keys("13333337777")
        # 输入密码
        self.driver.find_element(By.ID, "password").send_keys("123456")
        # 输入验证码
        self.driver.find_element(By.ID, "verify_code").send_keys("8888")
        # 点击登录
        self.driver.find_element(By.CSS_SELECTOR, ".J-login-submit").click()
        time.sleep(1)
        # 获取提示信息
        msg = self.driver.find_element(By.CSS_SELECTOR, ".layui-layer-content").text
        assert "账号不存在" in msg
        # self.driver.quit()

    # 定义测试方法  密码错误
    def test_login_02(self):
        # driver = webdriver.Chrome()
        # driver.maximize_window()
        # driver.implicitly_wait(10)
        # driver.get("http://tpshop-test.itheima.net/")
        # # 点击登录按钮跳转到登录页面
        # self.driver.find_element(By.CSS_SELECTOR, ".red").click()
        # 输入手机号码
        self.driver.find_element(By.ID, "username").send_keys("13012345678")
        # 输入密码
        self.driver.find_element(By.ID, "password").send_keys("123456")
        # 输入验证码
        self.driver.find_element(By.ID, "verify_code").send_keys("8888")
        # 点击登录
        self.driver.find_element(By.CSS_SELECTOR, ".J-login-submit").click()
        time.sleep(1)
        # 获取提示信息
        msg = self.driver.find_element(By.CSS_SELECTOR, ".layui-layer-content").text
        assert "密码错误" in msg
        # self.driver.quit()

    # 定义测试方法  用户名为空
    def test_login_03(self):
        # driver = webdriver.Chrome()
        # driver.maximize_window()
        # driver.implicitly_wait(10)
        # driver.get("http://tpshop-test.itheima.net/")
        # # 点击登录按钮跳转到登录页面
        # self.driver.find_element(By.CSS_SELECTOR, ".red").click()
        # 输入手机号码
        self.driver.find_element(By.ID, "username").send_keys(" ")
        # 输入密码
        self.driver.find_element(By.ID, "password").send_keys("123456")
        # 输入验证码
        self.driver.find_element(By.ID, "verify_code").send_keys("8888")
        # 点击登录
        self.driver.find_element(By.CSS_SELECTOR, ".J-login-submit").click()
        time.sleep(1)
        # 获取提示信息
        msg = self.driver.find_element(By.CSS_SELECTOR, ".layui-layer-content").text
        assert "用户名不能为空" in msg
        # self.driver.quit()
