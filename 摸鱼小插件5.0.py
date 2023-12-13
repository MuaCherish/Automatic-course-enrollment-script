import tkinter as tk
import pyautogui
from pynput import mouse
import threading
import time
import ast

# ###################### 全局变量 ############################

# 鼠标路径坐标
index = []
listener = None
scroll_listener = None
Display_x = (0, 0)
Display_y = (0, 0)
scoll_distance = 120
delay_time = 600


# ###################### 函数区域 ############################


# 如果点击鼠标 + 终止监听
def on_click(x, y, button, pressed):  # 鼠标监听事件
    global listener, scroll_listener

    # 检测鼠标左键是否按下
    if button == mouse.Button.left and pressed:
        x, y = pyautogui.position()
        positions = (x, y)
        update_text_box(f'已记录坐标：{positions}\n')
        index.append(positions)

    # 检测鼠标中间是否按下
    elif button == mouse.Button.middle and pressed:
        listener.stop()
        scroll_listener.stop()


# 如果按下滚轮
def on_scroll(x, y, dx, dy):
    if dy > 0:
        update_text_box("鼠标上滚: index+1\n")
        index.append(1)

    elif dy < 0:
        update_text_box("鼠标下滚: index-1\n")
        index.append(-1)

    else:
        update_text_box("错误！dy == 0\n")

    x, y = pyautogui.position()
    positions = (x, y)
    index.append(positions)


# 更新窗口
def update_text_box(content):
    text_box.insert(tk.END, content)
    text_box.see(tk.END)
    window.update_idletasks()  # 更新窗口并响应用户操作


# 创建播放按钮
def display():
    global index

    # 识别是否有导入配置，以及导入配置是否符合规范
    data = data_box.get().strip()
    if data:
        if data[:5] == "index":
            try:
                start = data.index("[")
                index = ast.literal_eval(data[start:])
            except (SyntaxError, ValueError, IndexError) as e:
                update_text_box("用户配置导入错误，请输入正确的数据格式。\n")
                return

        elif "delay" in data:
            global delay_time
            try:
                start = data.index("=") + 1
                delay_time = int(data[start:])
                update_text_box("========================\n")
                update_text_box("调试模式已启动，延迟时间为%d秒。\n" % delay_time)
                return
            except ValueError:
                update_text_box("错误的延迟时间格式。\n")
                return

        else:
            update_text_box("用户配置导入错误，请输入正确的数据格式。\n")
            return

    # 初始化
    i = 2
    x_min, y_min = index[0]
    x_max, y_max = index[1]

    Display_x = (x_min, x_max)
    Display_y = (y_min, y_max)

    x_min, x_max = Display_x
    y_min, y_max = Display_y
    # slide_index = index[2]

    while i < len(index):
        if isinstance(index[i], tuple):
            pyautogui.click(index[i])
            x, y = index[i]

            if x_min <= x <= x_max and y_min <= y <= y_max:
                for j in range(delay_time):
                    update_text_box(f'视频已经播放了{j + 1}秒\n')
                    window.update()  # 更新窗口，保持响应
                    time.sleep(1)
            else:
                for j in range(3):
                    update_text_box('=')
                    window.update()  # 更新窗口，保持响应
                    time.sleep(1)
                update_text_box("\n")
        else:
            pyautogui.moveTo(index[i + 1])

            if index[i] == 1:
                pyautogui.scroll(scoll_distance)
                i = i + 1

            elif index[i] == -1:
                pyautogui.scroll(-scoll_distance)
                i = i + 1

            for j in range(3):  # 等3秒钟
                update_text_box('=')
                window.update()  # 更新窗口，保持响应
                time.sleep(1)
        i = i + 1

    update_text_box(f'\n==模拟完成==')


# 点击模拟按钮
def simulate_mouse_input():
    update_text_box("========================\n")
    update_text_box("按钮已点击，模拟开始：\n\n")
    global listener, scroll_listener

    # 创建鼠标监听器
    listener = mouse.Listener(on_click=on_click)
    listener.start()

    # 创建鼠标滚轮监听器
    scroll_listener = mouse.Listener(on_scroll=on_scroll)
    scroll_listener.start()

    # 创建一个线程来等待监听器停止
    thread = threading.Thread(target=wait_for_listeners_stop)
    thread.start()


# 等待监听器停止
def wait_for_listeners_stop():
    # 等待监听器停止
    listener.join()
    scroll_listener.join()

    # 更新视频所在坐标
    x_min, y_min = index[0]
    x_max, y_max = index[1]
    Display_x = (x_min, x_max)
    Display_y = (y_min, y_max)

    # 计算需要多长时间
    summ = 0
    o = 2
    while o < len(index):
        if isinstance(index[o], tuple):
            summ += 1
        elif index[o] == -1 or index[o] == 1:
            pass
        o += 2

    # 更新文本框内容
    update_text_box('-----------------------------------\n')
    update_text_box('用户配置已记录！\n\n')
    update_text_box(f'index = {index}\n')
    update_text_box(f'\n预计需要：{(summ * (delay_time / 60) / 60):.1f} 小时\n')
    update_text_box('-----------------------------------\n')


# ###################### 主函数 ############################


# 创建主窗口
window = tk.Tk()
window.title('CryMelloryS')

# 将窗口置顶
window.attributes('-topmost', True)

# 获取屏幕的宽度和高度
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# 设置窗口的宽度和高度
window_width = 500
window_height = 425

# 计算窗口的左上角坐标，使其位于屏幕中间偏上一点
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 5

# 设置窗口的位置
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# 禁止窗口调整大小
window.resizable(False, False)

# 创建文本框显示输出内容
text_box = tk.Text(window, height=10, width=100)
text_box.pack()

# 添加准备工作声明内容
update_text_box("========================\n")
update_text_box(">>>使用手册:\n")
update_text_box("1. 点击Mimic开始行为模拟\n")
update_text_box("2. 前两下确认窗口位置\n")
update_text_box("3. 鼠标中键结束模拟\n")
update_text_box("========================\n")
update_text_box(">>>注意事项:\n")
update_text_box("1. 是否已经提前开启2倍速\n")
update_text_box("2. 是否已经关闭那该死的有道词典\n")
update_text_box("3. 前两下确定视频窗口坐标\n")
update_text_box("4. 别忘了按滚轮停止模拟\n")
update_text_box("5. 至少点两下再退出，不然会报错\n")
update_text_box("6. 不要手痒点两下模拟，不然会出现两个并行进程\n")

# 创建模拟按钮
simulate_button1 = tk.Button(window, text="模拟", command=simulate_mouse_input, width=8, height=2)
simulate_button1.pack()
simulate_button1.place(x=110, y=280)

# 创建播放按钮
simulate_button2 = tk.Button(window, text="播放", command=display, width=8, height=2)
simulate_button2.pack()
simulate_button2.place(x=245, y=280)

# 创建标签
label = tk.Label(window, text="MuaCherish")
label.place(relx=1.0, rely=1.0, anchor="se")
# label.bind("<Control-c>", lambda e: "break")

# 创建文本框显示输出内容
data_box = tk.Entry(window, width=8)
data_box.pack()
data_box.place(x=10, y=window_height - 40, relheight=0.08)

##################################################################

# 启动GUI事件循环
window.mainloop()

# 打包代码
# pyinstaller -w --hidden-import=pynput --icon=D:\Pycharm\Project\刷课小玩意儿\icon_fish.ico Pynput模拟器5.0.py
