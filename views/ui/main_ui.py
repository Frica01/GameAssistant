# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledOYmRuz.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QCursor, QFont, QIcon)
from PySide6.QtWidgets import (QFrame, QGridLayout, QGroupBox,
                               QHBoxLayout, QLabel, QLineEdit, QPushButton, QTabWidget, QVBoxLayout,
                               QWidget)

from views.ui import utils_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(388, 226)
        icon = QIcon()
        icon.addFile(u":/trash.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.frame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"    QTabWidget::pane {\n"
                                     "        border: 1px solid #C2C7CB;\n"
                                     "        background-color: #F0F0F0;\n"
                                     "    }\n"
                                     "    \n"
                                     "    QTabWidget::tab-bar {\n"
                                     "        alignment: left;\n"
                                     "    }\n"
                                     "    \n"
                                     "    QTabBar::tab {\n"
                                     "        background-color: #C2C7CB;\n"
                                     "        color: #FFFFFF;\n"
                                     "        padding: 8px;\n"
                                     "        border: none;\n"
                                     "        border-top-left-radius: 4px;\n"
                                     "        border-top-right-radius: 4px;\n"
                                     "		font-size: 15px;\n"
                                     "		font-weight: bold;\n"
                                     "		padding-left: 10px;  /* \u8bbe\u7f6e\u5de6\u8fb9\u8ddd\u4e3a 10px */\n"
                                     "    }\n"
                                     "    \n"
                                     "    QTabBar::tab:selected {\n"
                                     "        background-color: #FFFFFF;\n"
                                     "        color: #000000;\n"
                                     "    }")
        self.tab_click = QWidget()
        self.tab_click.setObjectName(u"tab_click")
        self.gridLayout_4 = QGridLayout(self.tab_click)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_2 = QFrame(self.tab_click)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)

        self.horizontalLayout.addWidget(self.label_2)

        self.line_edit_click = QLineEdit(self.frame_2)
        self.line_edit_click.setObjectName(u"line_edit_click")
        self.line_edit_click.setMinimumSize(QSize(200, 30))
        self.line_edit_click.setMaximumSize(QSize(250, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(13)
        font1.setBold(False)
        font1.setItalic(False)
        self.line_edit_click.setFont(font1)
        self.line_edit_click.setStyleSheet(u"font: 13pt \"Microsoft YaHei UI\";")

        self.horizontalLayout.addWidget(self.line_edit_click)

        self.gridLayout_4.addWidget(self.frame_2, 0, 0, 1, 1, Qt.AlignHCenter)

        self.frame_3 = QFrame(self.tab_click)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 80))
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.frame_3)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4, 0, Qt.AlignHCenter)

        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)

        self.gridLayout_4.addWidget(self.frame_3, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_click, "")
        self.tab_on_hook = QWidget()
        self.tab_on_hook.setObjectName(u"tab_on_hook")
        self.tab_on_hook.setStyleSheet(u"QPushButton{	\n"
                                       "	background-position: left center;\n"
                                       "    background-repeat: no-repeat;\n"
                                       "	border-left: 1px solid transparent;\n"
                                       "	background-color:rgb(240, 240, 240);\n"
                                       "	text-align: left;\n"
                                       "	padding-left: 1px;\n"
                                       "	font: 15pt \"Microsoft YaHei UI\";\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover{\n"
                                       "	background-color: rgb(246, 255, 254);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed{	\n"
                                       "	\n"
                                       "	background-color: rgb(251, 254, 255);\n"
                                       "};\n"
                                       "")
        self.verticalLayout_3 = QVBoxLayout(self.tab_on_hook)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_7 = QFrame(self.tab_on_hook)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_7)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_7)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.horizontalLayout_3.addWidget(self.label)

        self.line_edit_title = QLineEdit(self.frame_6)
        self.line_edit_title.setObjectName(u"line_edit_title")
        self.line_edit_title.setMinimumSize(QSize(0, 30))
        self.line_edit_title.setMaximumSize(QSize(200, 16777215))
        self.line_edit_title.setFont(font)

        self.horizontalLayout_3.addWidget(self.line_edit_title)

        self.verticalLayout_2.addWidget(self.frame_6, 0, Qt.AlignHCenter)

        self.frame_5 = QFrame(self.frame_7)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_show_win = QPushButton(self.frame_5)
        self.btn_show_win.setObjectName(u"btn_show_win")
        self.btn_show_win.setMaximumSize(QSize(16777215, 25))
        self.btn_show_win.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btn_show_win, 0, Qt.AlignHCenter)

        self.btn_hide_win = QPushButton(self.frame_5)
        self.btn_hide_win.setObjectName(u"btn_hide_win")
        self.btn_hide_win.setMinimumSize(QSize(0, 25))
        self.btn_hide_win.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btn_hide_win, 0, Qt.AlignHCenter)

        self.verticalLayout_2.addWidget(self.frame_5)

        self.verticalLayout_3.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.tab_on_hook)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 80))
        self.frame_8.setMaximumSize(QSize(16777215, 16777215))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_8)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.groupBox_2 = QGroupBox(self.frame_8)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_4.addWidget(self.label_5, 0, Qt.AlignHCenter)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei UI"])
        font2.setBold(False)
        self.label_6.setFont(font2)

        self.verticalLayout_4.addWidget(self.label_6, 0, Qt.AlignHCenter)

        self.gridLayout_5.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.verticalLayout_3.addWidget(self.frame_8)

        self.tabWidget.addTab(self.tab_on_hook, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u8f85\u52a9\u5c0f\u5de5\u5177", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6bcf\u79d2\u70b9\u51fb\uff1a", None))
        # if QT_CONFIG(tooltip)
        self.line_edit_click.setToolTip(QCoreApplication.translate("MainWindow",
                                                                   u"<html><head/><body><p>\u9ed8\u8ba4\u4e3a10\u3002<br/>100以上按150处理</p></body></html>",
                                                                   None))
        # endif // QT_CONFIG(tooltip)
        self.line_edit_click.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"\u8f93\u516510~100\uff0c\u6b65\u957f\u4e3a10", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u63d0\u793a", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u5f00\u59cb🐱‍🏍\uff1a\u6309\u4e0b<b> Ctrl + Shift + A</b> \u5f00\u59cb\u8fde\u51fb",
                                                        None))
        self.label_4.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u505c\u6b62⚡\uff1a\u6309\u4e0b<b> Ctrl + Shift + Q</b> \u505c\u6b62\u8fde\u51fb",
                                                        None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_click),
                                  QCoreApplication.translate("MainWindow", u"\u9f20\u6807\u8fde\u51fb", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u7a97\u53e3\u6807\u9898\uff1a", None))
        self.line_edit_title.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u7a97\u53e3\u6807\u9898", None))
        self.btn_show_win.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u7a97\u53e3", None))
        self.btn_hide_win.setText(QCoreApplication.translate("MainWindow", u"\u9690\u85cf\u7a97\u53e3", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u63d0\u793a", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u8f93\u5165\u7a97\u53e3\u6807\u9898\uff0c\u7136\u540e\u9009\u62e9<b>\u663e\u793a\u7a97\u53e3&\u9690\u85cf\u7a97\u53e3</b>",
                                                        None))
        self.label_6.setText(QCoreApplication.translate("MainWindow",
                                                        u"ps\uff1a\u9002\u7528\u4e8e\u9700\u8981\u524d\u53f0\u6302\u673a\u7684\u6e38\u620f\uff08\u6216<b>\u6478\u9c7c🐟</b>",
                                                        None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_on_hook),
                                  QCoreApplication.translate("MainWindow", u"\u540e\u53f0\u6302\u673a", None))
    # retranslateUi
