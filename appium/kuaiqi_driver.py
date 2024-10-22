from appium import webdriver
from appium_flutter_finder.flutter_finder import FlutterElement, FlutterFinder
from appium.webdriver.webdriver import AppiumOptions, WebDriver
import time

# 操作定义

# 等待APP首页加载
def waitForLoad():
    button_finder = finder.by_value_key("setting")
    # 使用execute_script调用Flutter API
    # 等待元素出现，超时10秒
    driver.execute_script('flutter:waitFor', button_finder, 10000)

# 单纯等待指定毫秒数，不执行任何操作
def waitForMiliseconds(milliseconds: int):
    seconds: float = milliseconds / 1000.0
    time.sleep(seconds)

# 进入自选页面
def enterFavoriteSection():
    button_finder = finder.by_value_key("favoriteSection")
    button_element = FlutterElement(driver, button_finder)
    button_element.click()

# 图表页: 打开快速下单板
def showQuickTradeBoard():
    button_finder = finder.by_value_key("快速下单")
    button_element = FlutterElement(driver, button_finder)
    button_element.click()

# 图表页: 显示交易明细
def showTransaction():
    button_finder = finder.by_value_key("changeShowTransaction")
    button_element = FlutterElement(driver, button_finder)
    button_element.click()

# 快速下单板: 使用指定价格交易
# "买1" "买2" "买3" "买4" "买5" "卖1" "卖2" "卖3" "卖4" "卖5"
def tradeWithPrice(price: str):
    button_finder = finder.by_value_key(price)
    button_element = FlutterElement(driver, button_finder)
    button_element.click()
    button_finder = finder.by_value_key("卖空")
    button_element = FlutterElement(driver, button_finder)
    button_element.click()
    # 如果有下单弹窗，则点击确认
    button_finder = finder.by_value_key("tradeConfirmButton")
    button_element = FlutterElement(driver, button_finder)
    # 先判断元素是否存在
    driver.elementClick(button_element)
        
    

# 报价页: 按照最新价排列行情列表
def sortByLatestPrice():
    button_finder = finder.by_value_key("最新SortItem")
    button_element = FlutterElement(driver, button_finder)
    button_element.click()

# 报价页: 取消排序
def cancelSort():
    button_finder = finder.by_value_key("cancelSort")
    button_element = FlutterElement(driver, button_finder)
    button_element.click()

# 进入行情页
def enterQuoteSection():
    button_finder = finder.by_value_key("quoteSection")
    button_element = FlutterElement(driver, button_finder)
    button_element.click()

# 点击指定的文本
def clickText(text: str):
    button_finder = finder.by_text(text)
    button_element = FlutterElement(driver, button_finder)
    button_element.click()

# 进入图表页: 根据指定的合约名称
def enterChart(symbol: str):
    button_finder = finder.by_text(symbol)
    button_element = FlutterElement(driver, button_finder)
    button_element.click()

driver: WebDriver = None
finder: FlutterFinder = None

# 启动Appium会话，获取驱动
def initDriver(url, capabilities):
    global driver, finder
    options = AppiumOptions()
    options.load_capabilities(capabilities)
    driver = webdriver.Remote(url, options=options)
    finder = FlutterFinder()

def quit():
    if driver:
        driver.quit()

# 服务端URL
appium_server_url = 'http://localhost:4723'

capabilities_hybrid = {
    'platformName': 'Android',
    'platformVersion': '11',
    'deviceName': '7bc1cde8',
    'appPackage': 'com.shinnytech.futures.kuaiqixiaoq.debug',
    'appActivity': 'com.shinnytech.futures.view.CustomFlutterActivity',
    'noReset': True,
    'automationName': 'flutter',
}

capabilities_flutter = dict(
    platformName= 'Android',
    platformVersion= '11',
    deviceName= '7bc1cde8',
    appPackage= 'com.example.shinny_flutter_module.host',
    appActivity= 'com.example.shinny_flutter_module.host.MainActivity',
    noReset= True,
    automationName= 'flutter',
)

