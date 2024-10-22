# bs://3c1b9fe340d1525fbfa43cb39599ab90f5b88e42

import unittest
from appium import webdriver
from appium_flutter_finder.flutter_finder import FlutterElement, FlutterFinder
from appium.webdriver.webdriver import AppiumOptions
import time

# 定义一组Capabilities参数，用于发送至Appium服务器
capabilities = dict(
    # 测试设备的参数
    platformName= 'Android',
    platformVersion= '11',
    deviceName= '7bc1cde8',
    # 提供APP的路径信息
    app= r'/Users/quyunye/dev/shinny-flutter-module/build/host/outputs/apk/debug/app-debug.apk',
    automationName= 'flutter',
)

# 服务端URL
appium_server_url = 'http://localhost:4723'

class FlutterTest(unittest.TestCase):
    def setUp(self) -> None:
        # 启动Appium会话
        self.driver = webdriver.Remote(appium_server_url, options=AppiumOptions().load_capabilities(capabilities))
        self.finder = FlutterFinder()

    def tearDown(self) -> None:
        # 结束测试
        if self.driver:
            self.driver.quit()

    def test_flutter(self):
        # 测试用例定义
        # 使用Flutter端组件的key值进行查找
        button_finder = self.finder.by_value_key("setting")
        # 使用execute_script等待元素出现（调用Flutter API）
        self.driver.execute_script('flutter:waitFor', button_finder, 10000)
        # 获取控件元素
        button_element = FlutterElement(self.driver, button_finder)
        # 执行点击操作
        button_element.click()

if __name__ == '__main__':
     unittest.main()
