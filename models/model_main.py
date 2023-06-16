# -*- coding: utf-8 -*-
# Name:         model_main.py
# Author:       小菜
# Date:         2023/6/14 20:00
# Description:


from collections import defaultdict
from PySide6.QtCore import (QObject, QRunnable, QThreadPool, Signal)

from models.invoke_func.mouse_click import click_mouse
from models.invoke_func.window_operate import (show_window, hide_window)

flag = True


class WorkerRunnable(QRunnable):

    def __init__(self, func, *args, **kwargs):
        super().__init__()
        self.func = func
        self.args = args
        self.status_signal = kwargs.get('status_signal')

    def run(self):
        if not self.args:
            self.func()
        while flag:
            self.func(*self.args)

    def win_run(self):
        res = self.func(*self.args)
        self.status_signal.emit({'status': res})


class ModelMain(QObject):
    win_status_signal: Signal = Signal(dict)

    def __init__(self):
        super().__init__()
        self.thread_pool = QThreadPool()
        self.thread_status_map = defaultdict(bool)

    def stop_keyboard_listener(self):
        global flag
        if flag:
            flag = False
            thread_name: str = 'click'
            self.thread_status_map[thread_name] = False

    def click_operate(self, frequency: int = 10):
        global flag
        thread_name: str = 'click'
        if self.thread_status_map[thread_name]:
            return
        flag = True
        self.thread_status_map[thread_name] = True
        if frequency < 10:
            frequency = 10
        print(flag, thread_name, self.thread_status_map[thread_name], frequency)
        click_frequency_map = {
            10: [0.09],
            20: [0.035],
            30: [0.027],
            40: [0.014],
            50: [0.013],
            60: [0.005],
            70: [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0],
            80: [0.01, 0.01, 0.01, 0],
            90: [0.01, 0.01, 0],
            100: [0.01, 0.0001, 0.0001, 0, 0],
            150: [0.001, 0.001, 0, 0, 0]
        }
        task = WorkerRunnable(
            click_mouse,
            click_frequency_map.get(frequency, 150)
        )
        self.thread_pool.start(task)

    def show_win_operate(self, title: str = None):
        task = WorkerRunnable(show_window,
                              title,
                              status_signal=self.win_status_signal)
        self.thread_pool.start(task.win_run)

    def hide_win_operate(self, title: str = None):
        task = WorkerRunnable(hide_window,
                              title,
                              status_signal=self.win_status_signal)
        self.thread_pool.start(task.win_run)
