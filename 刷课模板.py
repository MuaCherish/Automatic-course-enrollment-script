import pyautogui
import time

# 自定义
Display_x = (628, 801)              # 电脑播放键x范围
Display_y = (849, 1046)             # 电脑播放键y范围
index = [(933, 1737), (769, 937)]   # 鼠标坐标记录

# 初始化
i = 0
x_min, x_max = Display_x
y_min, y_max = Display_y

# 开始刷课
while i < len(index):
    # 点击下一个坐标
    pyautogui.click(index[i])

    # 判断是不是播放键，是的话就开启长时间等待,不是就等待3秒钟
    x, y = index[i]
    if x_min <= x <= x_max and y_min <= y <= y_max:  # 是播放键
        for j in range(600):  # 等待视频刷完
            print(f'视频已经播放了{j}秒')
            time.sleep(1)
    else:
        time.sleep(3)  # 等3秒钟

    # i++
    i = i + 1

print(f'刷课已完成！用时{i}秒')
