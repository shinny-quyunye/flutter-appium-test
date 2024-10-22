# bs://3c1b9fe340d1525fbfa43cb39599ab90f5b88e42
import json
import unittest
from appium import webdriver
from appium_flutter_finder.flutter_finder import FlutterElement, FlutterFinder
from appium.webdriver.webdriver import AppiumOptions
import time


executor_object = {
    'action': 'session-status',
    'arguments': {
        'status': "passed",
        'reason': "passed reason"
    }
}

desired_cap = {
 "platformName" : "android",
 "appium:platformVersion" : "9.0",
 "appium:deviceName" : "Huawei P30",
 "appium:app" : "bs://3c1b9fe340d1525fbfa43cb39599ab90f5b88e42",
 "appium:automationName" : "Flutter",
 'bstack:options' : {
   "userName" : "yunyequ_9PF2VB",
   "accessKey" : "z1rq9pWdysrmJDZzt7Lp",
   "appiumVersion" : "2.6.0",
   "projectName" : "flutter-test-project",
   "buildName" : "KuaiQi XiaoQ test build",
   "sessionName" : "KuaiQi XiaoQ test session",
   "video" : "true",
 }
}


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
appium_server_url = 'http://localhost:4723/wd/hub'

options = AppiumOptions().load_capabilities(desired_cap)

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
finder = FlutterFinder()

# 使用Flutter端组件的key值进行查找
button_finder = finder.by_value_key("setting")
# 使用execute_script等待元素出现（调用Flutter API）
driver.execute_script('flutter:waitFor', button_finder, 10000)
# 获取控件元素
button_element = FlutterElement(driver, button_finder)
# 执行点击操作
button_element.click()

# Invoke driver.quit() after the test is done to indicate that the test is completed.
driver.quit()
