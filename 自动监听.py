import pyautogui
import time

# 初始化数据
index = []
previous_positions = (0, 0)
positions = (0, 0)
i = 0

# 自动监听
while True:
    # 等待三秒钟
    for i in range(3):
        time.sleep(1)
        print('=', end=' ', flush=True)  # 刷新输出缓冲区
    # 读取一个坐标
    x, y = pyautogui.position()
    positions = (x, y)
    # 判断与上一个读取到的是否相同，如果相同，则输出坐标已记录并保存到position里面
    if positions == previous_positions:
        print("坐标已记录:", positions)
        index.append(positions)
    else:
        previous_positions = positions
        print(previous_positions)
    # 如果坐标为(0,0),退出循环
    if positions == (0, 0):
        break

print(index)
