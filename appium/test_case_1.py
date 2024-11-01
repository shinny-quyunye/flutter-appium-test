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

# 定义随机触控操作的类型范围: 点击, 滑动, 长按
touchActions = [
    kuaiqiExecutor.randomClick,
    kuaiqiExecutor.randomSwipe,
    kuaiqiExecutor.randomLongPress
]

# 记录随机操作执行次数
executeCount: int = 0
while True:
    executeCount += 1
    # 执行随机触控操作(点击 / 滑动 / 长按)
    action = random.choice(touchActions)
    action(count = random.randint(2, 5))
    if executeCount % 100 == 0:
        # 执行前后台随机切换操作
        kuaiqiExecutor.randomBackground(min_seconds = 1, max_seconds = 30)
    elif executeCount % 300 == 0:
        # 执行网络环境的随机切换操作
        kuaiqiExecutor.randomNetworkEnvironment()

# 结束测试
KuaiqiDriver.quit()

