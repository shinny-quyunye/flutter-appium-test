import kuaiqi_driver as KuaiqiDriver


# 获取快期驱动
KuaiqiDriver.initDriver(KuaiqiDriver.appium_server_url, KuaiqiDriver.capabilities_flutter)

# 测试用例定义


# 等待APP加载完成
#KuaiqiDriver.waitForLoad()

# 进入图表页面
#KuaiqiDriver.enterChart("玻璃2210")

# 分别选择1时、2时、15分周期
#KuaiqiDriver.clickText("1时")
#KuaiqiDriver.waitForMiliseconds(1000)

# 打开快速下单板
#KuaiqiDriver.showQuickTradeBoard()

# 使用指定价格交易
KuaiqiDriver.tradeWithPrice("卖2")

# 显示交易明细
#KuaiqiDriver.showTransaction()

# 进入自选页面
#KuaiqiDriver.enterFavoriteSection()

# 按照最新价排列
#KuaiqiDriver.sortByLatestPrice()

# 取消排序
#KuaiqiDriver.waitForMiliseconds(2000)
#KuaiqiDriver.cancelSort()
# 返回行情页
#KuaiqiDriver.enterQuoteSection()


# 结束测试
KuaiqiDriver.quit()