# -*- coding: utf-8 -*-
# Name:         controller_main.py
# Author:       小菜
# Date:         2023/6/14 20:00
# Description:

import keyboard
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QSystemTrayIcon

from views import ViewMain
from models import (ModelMain, WorkerRunnable)

round_to_nearest_10 = lambda number: min(round(number / 10) * 10, 150)


class ControllerMain:

    def __init__(self):
        self.view = ViewMain()
        self.model = ModelMain()
        # 显示窗口
        self.view.show()
        # 初始化 键盘监听
        self.init_operate()

        # 绑定按钮
        self.view.btn_show_win.clicked.connect(self.show_win_operate)
        self.view.btn_hide_win.clicked.connect(self.hide_win_operate)

        # 绑定信号到槽函数
        self.model.win_status_signal.connect(self.window_listen)

    def init_operate(self):
        task = WorkerRunnable(self.listen_keyboard)
        self.model.thread_pool.start(task)

    def listen_keyboard(self):
        keyboard.add_hotkey('Ctrl+Shift+A', self.click_operate)
        keyboard.add_hotkey('Ctrl+Shift+Q', self.model.stop_keyboard_listener)
        keyboard.wait()

    def click_operate(self):
        frequency = 10
        # 创建匿名函数
        try:
            frequency = round_to_nearest_10(int(self.view.line_edit_click.text()))
            print(frequency)
        except (ValueError, TypeError):
            ...
        finally:
            self.model.click_operate(frequency=frequency)
            self.view.show_notification(text='开始点击')

    def show_win_operate(self):
        win_title = self.view.line_edit_title.text()
        if not win_title:
            return
        self.model.show_win_operate(title=win_title)

    def hide_win_operate(self):
        win_title = self.view.line_edit_title.text()
        if not win_title:
            return
        self.model.hide_win_operate(title=win_title)

    @Slot(dict)
    def window_listen(self, item):
        if not item.get('status'):
            self.view.show_notification(
                title='警告警告⚠',
                text='找不到窗口！！！',
                icon=QSystemTrayIcon.MessageIcon.Warning
            )
