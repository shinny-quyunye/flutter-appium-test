import kuaiqi_driver as KuaiqiDriver
from kuaiqi_driver import Context, Direction, TradeMode
import time
import random
import string

# KuaiqiExecutor
# KuaiqiExecutor类定义了测试需要的APP基本操作，使用KuaiqiDriver提供的元素状态检查和元素操作方法
# 在用户故事与测试用例中，可以复用这些操作，组合成更复杂的测试用例

# 基本操作定义
# 等待APP首页启动加载完成
def waitForLoad():
    # 等待加载转圈结束
    loadingInSingle = KuaiqiDriver.getElementByKey("loadingInSingle")
    KuaiqiDriver.driver.execute_script('flutter:waitForAbsent', loadingInSingle)
    loadingInSingleMain = KuaiqiDriver.getElementByKey("loadingInSingleMain")
    KuaiqiDriver.driver.execute_script('flutter:waitForAbsent', loadingInSingleMain)
    # 检查首页是否已经显示
    flutterElement = KuaiqiDriver.getElementByType("SingleQuote")
    # 等待首页加载完成，超时5秒
    if (KuaiqiDriver.isElementVisible(flutterElement, timeout = 5000)):
        return
    # 如果结算单页面直接弹出，也视为APP加载完成
    if (KuaiqiDriver.isElementVisibleByType("SettlementConfirmation", timeout = 5000)):
        return

# 将APP切换到后台
# 传入参数: seconds, 后台停留时间，超时后返回前台
def toBackground(seconds: int):
    # 切换至NATIVE_APP Context处理前后台切换
    KuaiqiDriver.switchContext(Context.NATIVE)
    KuaiqiDriver.driver.background_app(seconds)
    # 切换回FLUTTER Context
    KuaiqiDriver.switchContext(Context.FLUTTER)

# 单纯等待指定毫秒数，不执行任何操作
def waitForMiliseconds(milliseconds: int):
    seconds: float = milliseconds / 1000.0
    KuaiqiDriver.logEvent(f"等待, 持续时间 {milliseconds} ms")
    time.sleep(seconds)

# 点击指定的文字
def clickText(text: str):
    flutterElement = KuaiqiDriver.getElementByText(text)
    flutterElement.click()

# 进入自选页面
# 如果已经在自选页面，则不执行任何操作
def enterFavoriteSection():
    if KuaiqiDriver.isElementVisibleByText("添加合约"):
        return
    flutterElement = KuaiqiDriver.getElementByKey("favoriteSection")
    flutterElement.click()

# 如果弹出结算单，进行确认
# 传入参数: timeout, 等待结算单弹出的超时时间，默认为5秒，超时后直接返回
def confirmSettlement(timeout: int = 5000):
    if (KuaiqiDriver.isElementVisibleByType("SettlementConfirmation", timeout=timeout)):
        flutterElement = KuaiqiDriver.getElementByText("确认结算单")
        flutterElement.click()

# 图表页: 打开快速下单板
# 首先检查快速下单板是否已经显示，如果已经显示，则不执行任何操作
def showQuickTradeBoard():
    if KuaiqiDriver.isElementVisibleByType("QuickTradeBoard"):
        return
    flutterElement = KuaiqiDriver.getElementByKey("快速下单")
    flutterElement.click()

# 图表页: 显示交易明细
# 首先检查交易明细是否已经显示，如果已经显示，则不执行任何操作
def showTransaction():
    if KuaiqiDriver.isElementVisibleByType("TransactionDetailPanel"):
        return
    flutterElement = KuaiqiDriver.getElementByKey("changeShowTransaction")
    flutterElement.click()

# 在通知弹窗中点击确认按钮
# 将检查弹窗是否存在，仅在存在时执行点击
def confirmAlert():
    if KuaiqiDriver.isElementVisibleByType("AlertDialog"):
        flutterElement = KuaiqiDriver.getElementByKey("confirmButtonInAlertDialog")
        flutterElement.click()
    
# 在下单确认弹窗中点击确认按钮
# 将检查下单确认弹窗是否存在，仅在下单确认弹窗存在时执行点击
def confirmOrder():
    # 检查下单确认弹窗是否存在
    if KuaiqiDriver.isElementVisibleByType("TradeConfirmation"):
        # 在弹窗打开时，点击确认下单按钮
        flutterElement = KuaiqiDriver.getElementByKey("tradeConfirmButton")
        flutterElement.click()

# 快速下单板: 使用指定价格交易
# 传入参数为价格类型，例如: "买1" "买2" "买3" "买4" "买5" "卖1" "卖2" "卖3" "卖4" "卖5"
def tradeWithPrice(price: str):
    flutterElement = KuaiqiDriver.getElementByKey(price)
    flutterElement.click()
    flutterElement = KuaiqiDriver.getElementByKey("卖空")
    flutterElement.click()
    # 如果有下单弹窗，还需要点击确认
    confirmOrder()

# 使用改单功能调整价格
# 传入参数为挂单id，从0开始，默认为首条挂单
def changeOrder(id: int = 0):
    flutterElement = KuaiqiDriver.getElementByKey("改单")
    # 检查是否处于挂单可以更改的状态
    if KuaiqiDriver.isElementVisible(flutterElement):
        flutterElement.click()
        # 如果存在多条挂单，则选择指定挂单进行修改
        flutterElement = KuaiqiDriver.getElementByKey("orderAction" + str(id))
        if KuaiqiDriver.isElementVisible(flutterElement):
            flutterElement.click()
        # 修改价格，点击价格输入框的加号进行微调
        flutterElement = KuaiqiDriver.getElementByKey("add" + "价格")
        flutterElement.click()
        # 点击确认，提交改单
        flutterElement = KuaiqiDriver.getElementByKey("orderDialogConfirmButton")
        flutterElement.click()
        # 如果存在多条挂单，则需要从挂单条目列表返回快速下单板
        flutterElement = KuaiqiDriver.getElementByText("返回")
        if KuaiqiDriver.isElementVisible(flutterElement):
            flutterElement.click()

# 报价页: 按照最新价排列行情列表
def sortByLatestPrice():
    flutterElement = KuaiqiDriver.getElementByKey("最新SortItem")
    flutterElement.click()

# 报价页: 取消排序
def cancelSort():
    flutterElement = KuaiqiDriver.getElementByKey("cancelSort")
    flutterElement.click()

# 进入行情页
def enterQuoteSection():
    flutterElement = KuaiqiDriver.getElementByKey("quoteSection")
    flutterElement.click()

# 进入图表页: 根据指定的合约名称
def enterChart(symbol: str):
    flutterElement = KuaiqiDriver.getElementByKey("tradeOrderGrid")
    if KuaiqiDriver.isElementVisible(flutterElement):
        # 如果当前位于交易页
        # 点击合约后，还需要点击图表按钮进入图表页
        for i in range(100):
            flutterElement = KuaiqiDriver.getElementByKey("order_" + str(i))
            if KuaiqiDriver.isElementVisible(flutterElement, timeout=10) and flutterElement.text.split("_")[0] == symbol:
                flutterElement.click()
                # 点击图表按钮进入图表页
                flutterElement = KuaiqiDriver.getElementByKey("图表")
                flutterElement.click()
                break
    else:
        # 如果当前位于行情页，直接点击合约进入图表页
        flutterElement = KuaiqiDriver.getElementByText(symbol)
        flutterElement.click()

# 获取图表页当前展示图表的key
def getChartKey():
    chartKeys = ["CurrentDayChart", "ChartCanvasFree", "ComboCurrentDayChart"]
    chartKey = None
    for key in chartKeys:
        if KuaiqiDriver.isElementVisibleByKey(key):
            chartKey = key
            break
    return chartKey

# 在图表处移动光标查看走势情况
def moveCursorInChart():
    chartKey = getChartKey()
    # 开始执行滑动操作
    KuaiqiDriver.driver.execute_script('flutter:longTap', KuaiqiDriver.finder.by_value_key(chartKey), {
        'durationMilliseconds': 200,
        'frequency': 30,
        })
    # 先向左上滑动
    KuaiqiDriver.driver.execute_script('flutter:scroll', KuaiqiDriver.finder.by_value_key(chartKey), {
        'dx': -100,
        'dy': -50,
        'durationMilliseconds': 200,
        'frequency': 30,
    })
    # 先向右下滑动
    KuaiqiDriver.driver.execute_script('flutter:scroll', KuaiqiDriver.finder.by_value_key(chartKey), {
        'dx': 100,
        'dy': 50,
        'durationMilliseconds': 200,
        'frequency': 30,
    })
    # 退出滑动模式
    flutterElement = KuaiqiDriver.getElementByKey(chartKey)
    flutterElement.click()

# 通过上下滑动切换图表页合约
def movetoSwitchSymbol(direction: Direction = Direction.NEXT):
    chartKey = getChartKey()
    # 确定滑动方向
    dy = None
    if direction == Direction.PREVIOUS:
        dy = 100
    else:
        dy = -100
    # 执行滑动操作
    KuaiqiDriver.driver.execute_script('flutter:scroll', KuaiqiDriver.finder.by_value_key(chartKey), {
        'dx': 0,
        'dy': dy,
        'durationMilliseconds': 200,
        'frequency': 30,
    })

# 我的页: 切换实盘/模拟账户
def switchSimOrRealInUserProfile(tradeMode: TradeMode=TradeMode.REAL):
    flutterElement = KuaiqiDriver.getElementByText(tradeMode.value)
    flutterElement.click()
    # 将弹出确认弹窗，点击确认
    confirmAlert()

# 我的页: 切换交易账户
# 输入参数为账户序号，默认为0，即切换至首个交易账户
def switchAccountInUserProfile(id: int = 0):
    flutterElement = KuaiqiDriver.getElementByKey("account_" + str(id))
    flutterElement.click()
    # 如果指定的交易账号不是当前的交易账号，那么将弹出确认弹窗
    # 检查确认弹窗弹出，在需要时点击确认
    confirmAlert()

# 交易页: 对持仓合约进行下单
# 传入参数 operation: 操作类型，例如: "平仓" "锁仓" "买多" "卖空" "加多" "加空" 
# 传入参数 price: 价格类型，例如: "对价" "挂价" "市价" "最新价"
def placeOrderInTradePage(operation: str, price: str):
    # 首先选择合约
    flutterElement = KuaiqiDriver.getElementByKey("order_0")
    if KuaiqiDriver.isElementVisible(flutterElement, timeout=10):
        flutterElement.click()
        # 点击价格选择输入框
        flutterElement = KuaiqiDriver.getElementByType("PriceEnterField")
        flutterElement.click()
        # 在价格选择键盘中选择指定的价格类型
        flutterElement = KuaiqiDriver.getElementByKey(price)
        flutterElement.click()
        # 关闭价格选择键盘
        flutterElement = KuaiqiDriver.getElementByKey("keyboard")
        flutterElement.click()
        # 点击指定的下单按钮
        flutterElement = KuaiqiDriver.getElementByKey(operation + "Button")
        flutterElement.click()
        # 如果存在下单确认弹窗，点击确认
        confirmOrder()

# 返回上一级页面
def pageBack():
    # 如果当前页面存在自定义的返回按钮，点击该按钮
    flutterElement = KuaiqiDriver.getElementByKey("backButton")
    if KuaiqiDriver.isElementVisible(flutterElement):
        flutterElement.click()
    else:
        # 如果当前页面没有自定义的返回按钮
        # 尝试使用 Material 或 Cupertino 框架的后退功能按钮
        buttoTypes = ["BackButton", "CloseButton"]
        for type in buttoTypes:
            if KuaiqiDriver.isElementVisibleByType(type):
                flutterElement = KuaiqiDriver.getElementByType(type)
                flutterElement.click()
                break

# 进入我的页
def enterUserProfile():
    flutterElement = KuaiqiDriver.getElementByKey("我的")
    flutterElement.click()

# 进入交易页
def enterTrade():
    flutterElement = KuaiqiDriver.getElementByKey("交易")
    flutterElement.click()



# --------checker--------
# 获取报价页当前行情数据
# 返回一个二维列表，包含当前报价页合约的最新价、涨幅和成交量数据
# 传入参数: limitCount, 限制获取的合约数量，默认为None，获取当前页面全部合约数据
# 返回格式示例:
# [['name', 'id', 'last_price', 'change_percent', 'volume'],
# ['玻璃2510', 'FG510', '1528', '+0.39%', '147']
# ['螺纹2510', 'rb2510', '3423', '-0.55%', '909']
# ['螺纹2505', 'rb2505', '3385', '-0.41%', '52695']
# ['玻璃2505', 'FG505', '1437', '+1.20%', '12.76万']]
def getQuoteData(limitCount: int = None) -> list:
    quoteDataList, quoteId = [["name", "id", "last_price", "change_percent", "volume"]], 0
    # 遍历当前页面的全部合约
    while KuaiqiDriver.isElementVisibleByKey("instrument_id_" + str(quoteId), timeout = 1):
        # 获取合约名称、ID、最新价、涨幅和成交量数据
        name = KuaiqiDriver.getElementByKey("instrument_name_" + str(quoteId)).text
        id = KuaiqiDriver.getElementByKey("instrument_id_" + str(quoteId)).text
        last_price = KuaiqiDriver.getElementByKey("last_price" + str(quoteId)).text
        change_percent = KuaiqiDriver.getElementByKey("change_percent" + str(quoteId)).text
        volumn = KuaiqiDriver.getElementByKey("volume" + str(quoteId)).text
        # 构建数据行
        list_item = [name, id, last_price, change_percent, volumn]
        quoteDataList.append(list_item)
        quoteId += 1
        if limitCount and quoteId >= limitCount:
            break
    return quoteDataList

# 检查行情数据是否正常更新
# seconds: 检查间隔时间，默认为2s
# limitCount: 限制获取的合约数量，默认为None，检查当前页面全部合约数据
# 返回False: 指定时间内行情数据未发生任何变化
# 返回True: 指定时间内行情数据至少发生一处变化
def checkQuoteDataUpdate(seconds: int = 2, limitCount: int = None) -> bool:
    # 获取当前行情数据
    quoteDataListBegin = getQuoteData(limitCount = limitCount)
    # 等待指定时间
    waitForMiliseconds(seconds * 1000)
    # 再次获取行情数据
    quoteDataListEnd = getQuoteData(limitCount = limitCount)
    # 检查两次行情数据是否一致
    if len(quoteDataListBegin) != len(quoteDataListEnd):
        return False
    for instrument1, instrument2 in zip(quoteDataListBegin, quoteDataListEnd):
        if instrument1 != instrument2:
            return False
    return True

# 随机点击
# 传入参数: count，点击次数，默认为1次
# 当count>1时，间隔0.01-0.1s执行
def randomClick(count: int = 1):
    # 切换至NATIVE_APP Context处理屏幕尺寸与坐标点击事件
    KuaiqiDriver.switchContext(Context.NATIVE)
    width = KuaiqiDriver.driver.get_window_size()['width']
    height = KuaiqiDriver.driver.get_window_size()['height']
    for i in range(count):
        # 生成屏幕范围内的随机坐标
        x = random.randint(100, width - 100)
        y = random.randint(100, height - 100)
        # 执行点击，可以使用相对坐标和绝对坐标
        KuaiqiDriver.logEvent(f"随机点击, 坐标 {x}, {y}")
        KuaiqiDriver.driver.tap([(x,y)])
        # 每次点击的间隔时间
        if count > 1:
            waitForMiliseconds(random.randint(10, 100))
    # 切换回FLUTTER Context
    KuaiqiDriver.switchContext(Context.FLUTTER)

# 随机滑动
# 传入参数: count, 滑动次数，默认为1次
# 当count>1时，间隔0.01-0.1s执行
# 滑动持续时间，随机选取100-2000ms时长
def randomSwipe(count: int = 1):
    # 切换至NATIVE_APP Context处理屏幕尺寸与坐标滑动件
    KuaiqiDriver.switchContext(Context.NATIVE)
    width = KuaiqiDriver.driver.get_window_size()['width']
    height = KuaiqiDriver.driver.get_window_size()['height']
    for i in range(count):
        # 生成屏幕范围内的随机坐标用于滑动
        # 为了避免屏幕手势操作，滑动起点需要留有间隔
        start_x = random.randint(100, width - 100)
        start_y = random.randint(100, height - 100)
        end_x = random.randint(0, width)
        end_y = random.randint(0, height)
        duration = random.randint(100, 2000)
        # 4个参数：startx，starty，endx，endy, duration
        KuaiqiDriver.logEvent(f"随机滑动, 坐标 {start_x}, {start_y} -> {end_x}, {end_y}, 持续时间 {duration} ms")
        KuaiqiDriver.driver.swipe(start_x, start_y, end_x, end_y, duration)
        # 每次滑动的间隔时间
        if count > 1:
            waitForMiliseconds(random.randint(10, 100))
    # 切换回FLUTTER Context
    KuaiqiDriver.switchContext(Context.FLUTTER)

# 随机长按
# 传入参数: count, 长按次数，默认为1次
# 当count>1时，间隔0.01-0.1s执行
# 长按持续时间，随机选取100-5000ms时长
def randomLongPress(count: int = 1):
    # 切换至NATIVE_APP Context处理屏幕尺寸与坐标长按事件
    KuaiqiDriver.switchContext(Context.NATIVE)
    width = KuaiqiDriver.driver.get_window_size()['width']
    height = KuaiqiDriver.driver.get_window_size()['height']
    for i in range(count):
        # 生成屏幕范围内的随机坐标
        x = random.randint(100, width - 100)
        y = random.randint(100, height - 100)
        duration = random.randint(100, 5000)
        # 执行点击，可以使用相对坐标和绝对坐标
        KuaiqiDriver.logEvent(f"随机长按, 坐标 {x}, {y}, 持续时间 {duration} ms")
        KuaiqiDriver.driver.tap([(x,y)], duration)
        # 每次长按的间隔时间
        if count > 1:
            waitForMiliseconds(random.randint(10, 100))
    # 切换回FLUTTER Context
    KuaiqiDriver.switchContext(Context.FLUTTER)

# 随机切换前后台
# 传入参数: min_seconds, max_seconds, 后台停留时间将在指定的范围内随机选取
def randomBackground(min_seconds: int = 1, max_seconds: int = 30):
    seconds = random.randint(min_seconds, max_seconds)
    KuaiqiDriver.logEvent(f"随机切换前后台, 后台停留时间 {seconds} 秒")
    toBackground(seconds)

# todo: 随机输入
def randomKeyboardInput():
    KuaiqiDriver.logEvent(f"随机输入")
        
# todo: 随机切换网络环境
def randomNetworkEnvironment():
    KuaiqiDriver.logEvent(f"随机切换网络环境, 暂未实现")

