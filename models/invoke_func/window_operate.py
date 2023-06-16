# -*- coding: utf-8 -*-
# Name:         mouse_click.py
# Author:       小菜
# Date:         2023/6/14 20:00
# Description:

import win32gui
import win32con


def get_window_handle(class_name=None, title=None):
    """
    通过类名和标题查找窗口句柄.

    Args:
        class_name(str|None):窗口的类名. 默认为None.
        title(str|None):窗口的标题. 默认为None.

    Returns:
        int: 返回找到的窗口句柄，如果没有找到则返回0.
    """
    return win32gui.FindWindow(class_name, title)


def set_top_window(hwnd):
    """
    窗口置顶
    """
    win32gui.SetForegroundWindow(hwnd)


def hide_window(title=None):
    """
    隐藏窗口

    Args:
        title(str|None):窗口的标题. 默认为None.

    Returns:
        None
    """
    hwnd = get_window_handle(title=title)
    if hwnd == 0:
        return False
    set_top_window(hwnd=hwnd)
    win32gui.ShowWindow(hwnd, win32con.SW_HIDE)
    return True


def show_window(title=None):
    """
    显示窗口

    Args:
        title(str|None):窗口的标题. 默认为None.

    Returns:
        None
    """
    hwnd = get_window_handle(title=title)
    if hwnd == 0:
        return False
    win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
    set_top_window(hwnd=hwnd)
    return True
