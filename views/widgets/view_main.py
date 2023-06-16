# -*- coding: utf-8 -*-
# Name:         view_main.py
# Author:       小菜
# Date:         2023/6/14 20:00
# Description:
import os

from PySide6.QtGui import (QAction, QIcon, QShortcut, QKeySequence)
from PySide6.QtWidgets import (QMainWindow, QSystemTrayIcon, QMenu)

from views import Ui_MainWindow


class ViewMain(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.setupUi(self)

        # 创建系统托盘图标相关的变量和对象
        self._restore_action = QAction()
        self._quit_action = QAction()
        self._tray_icon_menu = QMenu()

        # 创建系统托盘图标
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon(u":/trash.png"))
        self.tray_icon.setToolTip("辅助小工具")

        # 创建系统托盘图标的菜单和动作
        self.create_actions()
        self.create_tray_icon()
        self.tray_icon.show()

        # 连接系统托盘图标的激活信号到槽函数
        self.tray_icon.activated.connect(self.tray_icon_activated)

        # 键盘监听
        self.listen_keyboard()

    def tray_icon_activated(self, reason):
        # 当系统托盘图标被激活时的操作
        if reason == QSystemTrayIcon.ActivationReason.Trigger:
            self.restore_from_tray()

    def restore_from_tray(self):
        # 还原窗口
        if self.isMinimized():
            self.showNormal()
        elif self.isMaximized():
            self.showMaximized()
        else:
            self.show()

    def create_actions(self):
        # 创建系统托盘图标菜单的动作
        self._restore_action = QAction("显示", self)
        self._restore_action.triggered.connect(self.restore_from_tray)  # "显示"菜单项触发还原窗口的操作

        self._quit_action = QAction("退出", self)
        self._quit_action.triggered.connect(lambda: os._exit(0))  # "退出"菜单项触发退出应用程序的操作

    def create_tray_icon(self):
        # 创建系统托盘图标的菜单
        self._tray_icon_menu = QMenu(self)
        self._tray_icon_menu.addAction(self._restore_action)
        self._tray_icon_menu.addSeparator()
        self._tray_icon_menu.addAction(self._quit_action)

        self.tray_icon.setContextMenu(self._tray_icon_menu)
        self.tray_icon.show()

    def show_notification(self, title: str = '连击信息⚠', text: str = None, icon=QSystemTrayIcon.MessageIcon.Information):
        # 显示系统通知
        self.tray_icon.showMessage(
            title,
            f"警告！！！{text}",
            icon,
            2000
        )

    def listen_keyboard(self):
        # 键盘监听
        shortcut = QShortcut(QKeySequence("Esc"), self)
        # 当按下 Esc 键时隐藏窗口
        shortcut.activated.connect(self.hide)
