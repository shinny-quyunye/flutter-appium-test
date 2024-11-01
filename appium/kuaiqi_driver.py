from appium import webdriver
from appium_flutter_finder.flutter_finder import FlutterElement, FlutterFinder
from appium.webdriver.webdriver import AppiumOptions, WebDriver
from selenium.common.exceptions import WebDriverException
from enum import Enum
from datetime import datetime

# KuaiqiDriver
# 封装了Appium的WebDriver, Appium Flutter Driver, UIAutomator2 / XCUITest 等驱动的基本配置
# 提供了测试驱动初始化、视图元素访问接口、启动和退出Appium会话的方法，KuaiqiExecutor使用这些方法定义APP基本操作

# 驱动WebDriver和FlutterFinder定义
driver: WebDriver = None
finder: FlutterFinder = None

# 启动Appium会话，获取驱动
# 在开始执行测试前调用
def initDriver(url, capabilities):
    global driver, finder
    options = AppiumOptions()
    options.load_capabilities(capabilities)
    driver = webdriver.Remote(url, options=options)
    finder = FlutterFinder()

# 退出Appium会话
# 在测试结束时调用
def quit():
    if driver:
        driver.quit()

# 服务端URL
def getAppiumServerUrl() -> str:
    return 'http://localhost:4723'

# Appium配置
def getHybridCapabilities() -> dict:
    capabilities_hybrid = dict(
        platformName = 'Android',
        platformVersion = '11',
        deviceName = '7bc1cde8',
        appPackage = 'com.shinnytech.futures.kuaiqixiaoq.debug',
        appActivity = 'com.shinnytech.futures.view.CustomFlutterActivity',
        noReset = True,
        automationName = 'flutter',
    )
    return capabilities_hybrid

# Appium配置
def getFlutterCapabilities() -> dict:
    capabilities_flutter = dict(
        platformName = 'Android',
        platformVersion = '11',
        deviceName = '7bc1cde8',
        appPackage = 'com.example.shinny_flutter_module.host',
        appActivity = 'com.example.shinny_flutter_module.host.MainActivity',
        noReset = True,
        automationName = 'flutter',
        #observatoryWsUri = 'ws://127.0.0.1:50807/_a4bN7V5rHM=/ws',
    )
    return capabilities_flutter

# 基本元素操作定义
# 根据key获取元素
def getElementByKey(key: str):
    flutterFinder = finder.by_value_key(key)
    return FlutterElement(driver, flutterFinder)

# 根据type获取元素
def getElementByType(type: str):
    flutterFinder = finder.by_type(type)
    return FlutterElement(driver, flutterFinder)

# 根据text获取元素
def getElementByText(text: str):
    flutterFinder = finder.by_text(text)
    return FlutterElement(driver, flutterFinder)

# 检查元素是否存在，存在返回True，否则返回False
# 在没有计划的待处理帧后执行检查，超时时间默认为1秒，可传入指定超时时间
def isElementVisible(element: FlutterElement, timeout = 1000):
    try:
        driver.execute_script('flutter:waitFor', element, timeout)
        return True
    except WebDriverException as e:
        if "TimeoutException" in str(e):
            return False
        else:
            raise e

# 检查指定key的元素是否存在，存在返回True，否则返回False
# 在没有计划的待处理帧后执行检查，超时时间默认为1秒，可传入指定超时时间
def isElementVisibleByKey(key: str, timeout = 1000):
    return isElementVisible(getElementByKey(key), timeout)

# 检查指定type的元素是否存在，存在返回True，否则返回False
# 在没有计划的待处理帧后执行检查，超时时间默认为1秒，可传入指定超时时间
def isElementVisibleByType(type: str, timeout = 1000):
    return isElementVisible(getElementByType(type), timeout)

# 检查指定text的元素是否存在，存在返回True，否则返回False
# 在没有计划的待处理帧后执行检查，超时时间默认为1秒，可传入指定超时时间
def isElementVisibleByText(text: str, timeout = 1000):
    return isElementVisible(getElementByText(text), timeout)

# 定义Context类型
class Context(Enum):
    FLUTTER = 'FLUTTER'
    NATIVE = 'NATIVE_APP'

# 切换至指定的Context
# 能够在Flutter和Native上下文之间切换，执行不同驱动的接口
def switchContext(context: Context):
    driver.switch_to.context(context.value)

# 定义滑动切换方向
class Direction(Enum):
    PREVIOUS = 'previous'
    NEXT = 'next'

# 定义交易模拟: 实盘/模拟
class TradeMode(Enum):
    REAL = '实盘'
    SIM = '模拟'

# 用于提供日志id
logId: int = 0

# 记录日志
def logEvent(event: str):
    global logId
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    print(f"[log{logId} {current_time}] 执行操作: {event}")
    logId += 1

