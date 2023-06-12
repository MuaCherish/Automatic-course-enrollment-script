# Automatic-course-enrollment-script
ps:一个使用python做的刷一些水课的脚本


## 索引
- [前言](#前言)
- [用户配置](#用户配置)
- [后言](#后言)
- [帮助文档](#帮助文档)
- [其他](#其他)


## :tropical_fish:前言：

```
开发目的：
1. 一个不想看网课的大学生随便做出来的脚本，给自己刷完水课之后又改进了一下代码拿来给大伙儿一块用用hh
2. 学习python的库，在实际应用上又进一步
```

## :gear:用户配置：

1. <font color = "orange">测试鼠标位置.py</font>：
	- 确认一下自己电脑播放键的大致矩形范围 
	- 填写 <font color = "orange">刷客模板.py</font>的Display_x和Display_y里面

```python
Display_x = (628, 801) # 电脑播放键x范围  
Display_y = (849, 1046) # 电脑播放键y范围
```

2.  <font color = "orange">自动监听.py</font>：
	- 打开自动监听脚本
	- 开始模拟脚本要点击的部分(3s检测一次)
		- 要点击的部分停留两秒，脚本就会自动记录
		- 完成之后将鼠标移动到屏幕左上角停止监听
		- 复制index列表文件

```python
index = [(933, 1737), (769, 937)] # 鼠标坐标记录
```

3.   <font color = "orange">刷课模板.py</font>：
        - 自定义你自己的Display_x和Display_y范围
        - 自定义你自己的index监听数据
        - 运行<font color = "orange">刷课模板.py</font>.

---

## :fish:后言：

```c
该脚本调用了python自带的pyautogui库来进行一个鼠标的模拟输入
自我感觉比使用网页脚本来刷课更不容易被检测到
这个先用着，我这边正在测试更好的方法
附赠一个我自己写的pyautogui的帮助文档
end
```



---

# :bookmark_tabs:Pyautogui库帮助文档：

## 一. 故障保险

```python
# 将鼠标快速移到左上角即可中断程序
# 或者是鼠标左键+Ctrl键中断程序
pyautogui.FAILSAFE = True
```

## 二. 测试坐标

```python
# 测试鼠标位置  
while True:  
	x, y = pyautogui.position()  
	print(f'鼠标当前坐标：({x},{y})')  
	time.sleep(1)
```

## 三. 鼠标控制

<font size = "4"color = "pink">1. 移动</font>：

```python
# 直接移动
pyautogui.moveTo(x, y)

# 以当前位置做相对移动
pyautogui.moveRel(x, y)
```

<font size = "4"color = "pink">2. 拖着移动</font>：

```python
# 直接拖着移动
pyautogui.dragTo(x, y)

# 相对位置拖着移动
pyautogui.dragRel(x, y)
```

<font size = "4"color = "pink">3. 点击</font>：

```python
# 移动到某地+点击
pyautogui.click(x,y)

# 其他点击方式
pyautogui.middleClick(x,y)   # 中键
pyautogui.rightClick(x,y)    # 右键
pyautogui.doubleClick(x,y)   # 双击
```

<font size = "4"color = "pink">4. 滚动</font>：

```python
pyautogui.scroll(-25)
```

## 三. 键盘

<font size = "4"color = "pink">1. 在光标处自动打字</font>：

```python
# 自动打字
pyautogui.typewrite('Hello world!\n')
```

<font size = "4"color = "pink">2. 自动复制+粘贴</font>：

```python
pyautogui.hotkey('ctrl', 'a')  # ctrl-a 全选
pyautogui.hotkey('ctrl', 'c')  # ctrl-c 复制  
pyautogui.hotkey('ctrl', 'v')  # ctrl-v 粘贴
```

## 四. 其他

<font size = "4"color = "pink">1. 消息框</font>：

```python
pyautogui.alert('这将显示带有确定按钮的文本。')
```

<font size = "4"color = "pink">2. 获取屏幕大小</font>：

```python
Screen_size = pyautogui.size()
```

<font size = "4"color = "pink">3. 获取鼠标位置</font>：

```python
pyautogui.position()
```

<font size = "4"color = "pink">4. 睡眠时间</font>

```python
import time
time.sleep(2)
```

---

```
关键词：刷课脚本，网课，水课，大学生
开发者：MuaCherish
```
