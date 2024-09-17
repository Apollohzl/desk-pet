import tkinter as tk
import pyautogui
import math
import random

class SmoothMouseFollowWindow:
    def __init__(self, root):
        self.root = root
        self.t = 0
        
        self.root.title("Smooth Mouse Follow Window")
        self.root.geometry("200x100")  # 窗口的大小
        self.root.attributes('-topmost', True)  # 窗口始终在最上层

        # 变量初始化
        self.target_x = 0
        self.target_y = 0
        self.smoothness = 0.05  # 控制移动平滑度的因子
        self.adjustment_step = 10  # 微调步长

        # 创建退出按钮
        self.quit_button = tk.Button(self.root, text="made with Apollo", command=self.quit_program)
        self.quit_button.pack(pady=20)

        # 绑定键盘事件
        self.root.bind("<Up>", self.adjust_position)
        self.root.bind("<Down>", self.adjust_position)
        self.root.bind("<Left>", self.adjust_position)
        self.root.bind("<Right>", self.adjust_position)

        # 确保窗口获得焦点
        self.root.focus_set()

        # 调用更新位置的方法
        self.update_position()

    def update_position(self):
        # 获取鼠标的坐标
        x, y = pyautogui.position()
        
        # 目标位置更新
        self.target_x = x + 20
        self.target_y = y + 20  # 鼠标下方的一点，避免窗口遮挡鼠标

        # 获取窗口当前的位置
        current_x = self.root.winfo_x()
        current_y = self.root.winfo_y()

        # 平滑过渡
        new_x = current_x + (self.target_x - current_x) * self.smoothness
        new_y = current_y + (self.target_y - current_y) * self.smoothness

        # 设置窗口的新位置
        self.root.geometry(f'+{int(new_x)}+{int(new_y)}')
        self.t += 0.01
        print(self.t,{x==current_x},{y==current_y})
        if self.t >= random.randint(10,15):
            print("10秒!")
            self.t = 0
            self.shake_window()

        # 继续调用自身以保持窗口位置更新
        self.root.after(10, self.update_position)  # 每10毫秒更新一次

    def shake_window(self):
        x = root.winfo_x()
        y = root.winfo_y()
        center_x = x + root.winfo_width() // 2
        center_y = y + root.winfo_height() // 2
        radius = 10
        shake_times = 9
        interval = 10
        for r in range(2):
            for i in range(shake_times):
                angle = (i / shake_times) * 2 * math.pi
                offset_x = int(radius * math.cos(angle))
                offset_y = int(radius * math.sin(angle))
                new_x = center_x + offset_x - root.winfo_width() // 2
                new_y = center_y + offset_y - root.winfo_height() // 2
                root.geometry(f"+{new_x}+{new_y}")
                root.update_idletasks()
                root.after(interval)

    def adjust_position(self, event):
        # 设置距离阈值
        threshold = 50  # 5像素的阈值

        # 获取当前窗口位置
        current_x = self.root.winfo_x()
        current_y = self.root.winfo_y()

        # 计算目标位置
        if event.keysym == "Up":
            new_y = current_y - self.adjustment_step
            if abs(new_y - self.target_y) > threshold:
                self.root.geometry(f'+{current_x}+{new_y}')
        elif event.keysym == "Down":
            new_y = current_y + self.adjustment_step
            if abs(new_y - self.target_y) > threshold:
                self.root.geometry(f'+{current_x}+{new_y}')
        elif event.keysym == "Left":
            new_x = current_x - self.adjustment_step
            if abs(new_x - self.target_x) > threshold:
                self.root.geometry(f'+{new_x}+{current_y}')
        elif event.keysym == "Right":
            new_x = current_x + self.adjustment_step
            if abs(new_x - self.target_x) > threshold:
                self.root.geometry(f'+{new_x}+{current_y}')
        
    def quit_program(self):
        self.root.quit()  # 退出主事件循环
        self.root.destroy()  # 销毁窗口

# 创建 Tkinter 主窗口
root = tk.Tk()
app = SmoothMouseFollowWindow(root)

root.mainloop()
