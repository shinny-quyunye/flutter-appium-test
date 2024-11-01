import kuaiqi_driver as KuaiqiDriver
import kuaiqi_executor as kuaiqiExecutor
from kuaiqi_driver import getAppiumServerUrl, getHybridCapabilities, getFlutterCapabilities
from kuaiqi_driver import Context, Direction, TradeMode
import random

# 测试用例1: 探索性测试

# 加载快期驱动，初始化测试环境
KuaiqiDriver.initDriver(getAppiumServerUrl(), getHybridCapabilities())

# 等待APP加载完成
kuaiqiExecutor.waitForLoad()

# 随机选择初始环境（交易账号登录）
# todo

# 执行随机触控（点击/滑动/长按）操作
touchActions = [
    kuaiqiExecutor.randomClick,
    kuaiqiExecutor.randomSwipe,
    kuaiqiExecutor.randomLongPress
]
for i in range(100):
    action = random.choice(touchActions)
    executeCount = random.randint(2, 5)
    action(count = executeCount)

# 开始执行前后台/网络环境的随机切换操作
kuaiqiExecutor.randomKeyboardInput()
kuaiqiExecutor.randomNetworkEnvironment()

# 结束测试
KuaiqiDriver.quit()

