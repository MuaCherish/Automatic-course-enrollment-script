import pyautogui
import time

# 测试鼠标位置
while True:
    x, y = pyautogui.position()
    print(f'鼠标当前坐标：({x},{y})')
    time.sleep(1)

# Surface 8 Pro播放键坐标范围： 628<=x<=801 and 849<=y<=1046

