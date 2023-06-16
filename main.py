# -*- coding: utf-8 -*-
# Name:         mouse_click.py
# Author:       小菜
# Date:         2023/6/14 20:00
# Description:


import sys
from ctypes import windll

from PySide6.QtWidgets import QApplication

from controllers import ControllerMain

if __name__ == '__main__':
    # 同步图标
    windll.shell32.SetCurrentProcessExplicitAppUserModelID('nothing')
    app = QApplication()
    # 关闭窗口时候不退出程序
    app.setQuitOnLastWindowClosed(False)
    controller = ControllerMain()
    # 事件循环
    sys.exit(app.exec())
