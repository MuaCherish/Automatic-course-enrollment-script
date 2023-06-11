import pyautogui
import time

# 初始化
index = []
i = 0

# 开始刷课
while i < len(index):
    # 点击下一个坐标
    pyautogui.click(index[i])

    # 判断是不是播放键，是的话就开启长时间等待,不是就等待3秒钟
    x, y = index[i]
    if 628 <= x <= 801 and 849 <= y <= 1046:  # 是播放键
        for j in range(600):  # 等待视频刷完
            print(f'视频已经播放了{j}秒')
            time.sleep(1)
    else:
        time.sleep(3)  # 等3秒钟

    # i++
    i = i + 1

print(f'刷课已完成！用时{i}秒')
