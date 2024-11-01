import kuaiqi_driver as KuaiqiDriver
import kuaiqi_executor as kuaiqiExecutor
from kuaiqi_driver import getAppiumServerUrl, getHybridCapabilities, getFlutterCapabilities
from kuaiqi_driver import Context, Direction, TradeMode

# KuaiqiStory
# 定义了用户故事的操作序列，通过组合KuaiqiExecutor提供的基本操作，实现更复杂的测试操作流程

# 加载快期驱动，初始化测试环境
KuaiqiDriver.initDriver(getAppiumServerUrl(), getHybridCapabilities())

# 等待APP加载完成
kuaiqiExecutor.waitForLoad()

# 如果弹出结算单界面，进行确认
kuaiqiExecutor.confirmSettlement()

# 查看自选合约开盘行情: 玻璃2505, 螺纹2505, 玻璃2510, 螺纹2510, 玻璃主连, 螺纹主连
# 进入自选页面
kuaiqiExecutor.enterFavoriteSection()
# 检查当前页面的全部行情数据
kuaiqiExecutor.getQuoteData()
# 检查行情数据更新
kuaiqiExecutor.checkQuoteDataUpdate()
# 按照最新价排列自己的自选列表
kuaiqiExecutor.sortByLatestPrice()
# 查看行情3秒后，取消排序
kuaiqiExecutor.waitForMiliseconds(milliseconds = 3000)
kuaiqiExecutor.cancelSort()

# 查看图表数据
# 进入螺纹主力合约的图表页
kuaiqiExecutor.enterChart(symbol = "rb2501")
# 打开成交明细功能
kuaiqiExecutor.showTransaction()
# 分别查看1时、2时和15分钟k线图表
kuaiqiExecutor.clickText("1时")
kuaiqiExecutor.waitForMiliseconds(1000)
kuaiqiExecutor.clickText("2时")
kuaiqiExecutor.waitForMiliseconds(1000)
kuaiqiExecutor.clickText("15分")
kuaiqiExecutor.waitForMiliseconds(1000)

# 打开快速下单板
kuaiqiExecutor.showQuickTradeBoard()

# 使用指定价格交易
kuaiqiExecutor.tradeWithPrice("卖2")

# 使用改单功能调整价格
kuaiqiExecutor.changeOrder()

# 将APP切换到后台
kuaiqiExecutor.toBackground(seconds= 3)

# 进入我的页
kuaiqiExecutor.enterUserProfile()
# 我的页: 切换交易账户
kuaiqiExecutor.switchAccountInUserProfile()
# 进入交易页
kuaiqiExecutor.enterTrade()

# 从交易页前往查看图表
kuaiqiExecutor.enterChart(symbol = "FG501")
# 在图表页移动光标确认走势情况
kuaiqiExecutor.moveCursorInChart()
# 在图表页上下滑动切换合约
kuaiqiExecutor.movetoSwitchSymbol(direction = Direction.PREVIOUS)
# 返回上一级页面
kuaiqiExecutor.pageBack()

# 交易页: 对持仓合约进行下单
kuaiqiExecutor.placeOrderInTradePage("平仓", "对价")
# 进入我的页
kuaiqiExecutor.enterUserProfile()
# 我的页: 切换交易账户
kuaiqiExecutor.switchAccountInUserProfile()
# 返回行情页
kuaiqiExecutor.enterQuoteSection()

# 结束测试
KuaiqiDriver.quit()

