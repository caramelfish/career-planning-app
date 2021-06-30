# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome_screen_fixed.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WS_Main_Window(object):
    def setupUi(self, WS_Main_Window):
        WS_Main_Window.setObjectName("WS_Main_Window")
        WS_Main_Window.resize(1440, 900)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WS_Main_Window.sizePolicy().hasHeightForWidth())
        WS_Main_Window.setSizePolicy(sizePolicy)
        WS_Main_Window.setMinimumSize(QtCore.QSize(1440, 900))
        WS_Main_Window.setMaximumSize(QtCore.QSize(1488, 900))
        WS_Main_Window.setStyleSheet("background-color: rgb(14, 88, 100);")
        self.centralwidget = QtWidgets.QWidget(WS_Main_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Main_Grid = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Main_Grid.sizePolicy().hasHeightForWidth())
        self.Main_Grid.setSizePolicy(sizePolicy)
        self.Main_Grid.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Main_Grid.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Main_Grid.setObjectName("Main_Grid")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.Main_Grid)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.welcome_back_grid = QtWidgets.QGridLayout()
        self.welcome_back_grid.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.welcome_back_grid.setContentsMargins(-1, -1, -1, 0)
        self.welcome_back_grid.setObjectName("welcome_back_grid")
        self.welcome_back_frame = QtWidgets.QFrame(self.Main_Grid)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.welcome_back_frame.sizePolicy().hasHeightForWidth())
        self.welcome_back_frame.setSizePolicy(sizePolicy)
        self.welcome_back_frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 10px; \n"
"border: 2px;")
        self.welcome_back_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.welcome_back_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.welcome_back_frame.setObjectName("welcome_back_frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.welcome_back_frame)
        self.gridLayout_2.setContentsMargins(35, 10, 20, 30)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.welcome_back_header = QtWidgets.QLabel(self.welcome_back_frame)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans SemiBold")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.welcome_back_header.setFont(font)
        self.welcome_back_header.setObjectName("welcome_back_header")
        self.gridLayout_2.addWidget(self.welcome_back_header, 0, 0, 1, 1)
        self.welcome_back_description = QtWidgets.QLabel(self.welcome_back_frame)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(16)
        self.welcome_back_description.setFont(font)
        self.welcome_back_description.setWordWrap(True)
        self.welcome_back_description.setObjectName("welcome_back_description")
        self.gridLayout_2.addWidget(self.welcome_back_description, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        self.welcome_back_logo = QtWidgets.QLabel(self.welcome_back_frame)
        self.welcome_back_logo.setStyleSheet("")
        self.welcome_back_logo.setText("")
        self.welcome_back_logo.setPixmap(QtGui.QPixmap("Images/pybanner2.png"))
        self.welcome_back_logo.setScaledContents(True)
        self.welcome_back_logo.setObjectName("welcome_back_logo")
        self.gridLayout_2.addWidget(self.welcome_back_logo, 0, 2, 3, 1)
        self.welcome_back_grid.addWidget(self.welcome_back_frame, 0, 0, 1, 1)
        self.lbl_choose_account = QtWidgets.QLabel(self.Main_Grid)
        font = QtGui.QFont()
        font.setFamily("Henriette")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_choose_account.setFont(font)
        self.lbl_choose_account.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_choose_account.setObjectName("lbl_choose_account")
        self.welcome_back_grid.addWidget(self.lbl_choose_account, 1, 0, 1, 1)
        self.gridLayout_5.addLayout(self.welcome_back_grid, 0, 0, 1, 1)
        self.create_account_grid = QtWidgets.QGridLayout()
        self.create_account_grid.setObjectName("create_account_grid")
        self.top_spacer = QtWidgets.QLabel(self.Main_Grid)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_spacer.sizePolicy().hasHeightForWidth())
        self.top_spacer.setSizePolicy(sizePolicy)
        self.top_spacer.setMaximumSize(QtCore.QSize(400, 15))
        self.top_spacer.setText("")
        self.top_spacer.setObjectName("top_spacer")
        self.create_account_grid.addWidget(self.top_spacer, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.Main_Grid)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QtCore.QSize(300, 300))
        self.frame.setStyleSheet("background-color: rgb(228, 219, 163);\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 10px; \n"
"border: 2px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout_9.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(200, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(250, 40))
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans Medium")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setStyleSheet("background-color: rgb(8, 128, 174);\n"
"color: rgb(255, 255, 255);\n"
"border-color:  rgb(8, 128, 174);\n"
"border-radius: 10px; \n"
"border: 2px;")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_9.addWidget(self.pushButton, 0, QtCore.Qt.AlignHCenter)
        self.create_account_grid.addWidget(self.frame, 1, 0, 1, 1)
        self.bottom_spacer = QtWidgets.QLabel(self.Main_Grid)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottom_spacer.sizePolicy().hasHeightForWidth())
        self.bottom_spacer.setSizePolicy(sizePolicy)
        self.bottom_spacer.setMaximumSize(QtCore.QSize(400, 350))
        self.bottom_spacer.setText("")
        self.bottom_spacer.setObjectName("bottom_spacer")
        self.create_account_grid.addWidget(self.bottom_spacer, 2, 0, 1, 1)
        self.gridLayout_5.addLayout(self.create_account_grid, 0, 1, 1, 1)
        self.users_grid = QtWidgets.QGridLayout()
        self.users_grid.setObjectName("users_grid")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.users_grid.addItem(spacerItem1, 1, 1, 1, 1)
        self.userframe_3 = QtWidgets.QFrame(self.Main_Grid)
        self.userframe_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 10px; \n"
"border: 2px;")
        self.userframe_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.userframe_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.userframe_3.setObjectName("userframe_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.userframe_3)
        self.verticalLayout_3.setContentsMargins(25, -1, -1, 15)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.placeholder_name_3 = QtWidgets.QListWidget(self.userframe_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.placeholder_name_3.sizePolicy().hasHeightForWidth())
        self.placeholder_name_3.setSizePolicy(sizePolicy)
        self.placeholder_name_3.setMaximumSize(QtCore.QSize(300, 50))
        self.placeholder_name_3.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.placeholder_name_3.setFont(font)
        self.placeholder_name_3.setObjectName("placeholder_name_3")
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.placeholder_name_3.addItem(item)
        self.verticalLayout_3.addWidget(self.placeholder_name_3)
        self.users_grid.addWidget(self.userframe_3, 0, 5, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.users_grid.addItem(spacerItem2, 0, 2, 1, 1)
        self.userframe_1 = QtWidgets.QFrame(self.Main_Grid)
        self.userframe_1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 10px; \n"
"border: 2px;")
        self.userframe_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.userframe_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.userframe_1.setObjectName("userframe_1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.userframe_1)
        self.verticalLayout.setContentsMargins(25, -1, -1, 15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.placeholder_name_1 = QtWidgets.QListWidget(self.userframe_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.placeholder_name_1.sizePolicy().hasHeightForWidth())
        self.placeholder_name_1.setSizePolicy(sizePolicy)
        self.placeholder_name_1.setMaximumSize(QtCore.QSize(300, 50))
        self.placeholder_name_1.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.placeholder_name_1.setFont(font)
        self.placeholder_name_1.setObjectName("placeholder_name_1")
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.placeholder_name_1.addItem(item)
        self.verticalLayout.addWidget(self.placeholder_name_1)
        self.users_grid.addWidget(self.userframe_1, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.users_grid.addItem(spacerItem3, 0, 4, 1, 1)
        self.userframe_7 = QtWidgets.QFrame(self.Main_Grid)
        self.userframe_7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 10px; \n"
"border: 2px;")
        self.userframe_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.userframe_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.userframe_7.setObjectName("userframe_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.userframe_7)
        self.verticalLayout_7.setContentsMargins(25, -1, -1, 15)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.placeholder_name_7 = QtWidgets.QListWidget(self.userframe_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.placeholder_name_7.sizePolicy().hasHeightForWidth())
        self.placeholder_name_7.setSizePolicy(sizePolicy)
        self.placeholder_name_7.setMaximumSize(QtCore.QSize(300, 50))
        self.placeholder_name_7.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.placeholder_name_7.setFont(font)
        self.placeholder_name_7.setObjectName("placeholder_name_7")
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.placeholder_name_7.addItem(item)
        self.verticalLayout_7.addWidget(self.placeholder_name_7)
        self.users_grid.addWidget(self.userframe_7, 2, 5, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.users_grid.addItem(spacerItem4, 1, 5, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.users_grid.addItem(spacerItem5, 2, 4, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.users_grid.addItem(spacerItem6, 1, 3, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.users_grid.addItem(spacerItem7, 1, 7, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.users_grid.addItem(spacerItem8, 1, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.users_grid.addItem(spacerItem9, 2, 2, 1, 1)
        self.userframe_6 = QtWidgets.QFrame(self.Main_Grid)
        self.userframe_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 10px; \n"
"border: 2px;")
        self.userframe_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.userframe_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.userframe_6.setObjectName("userframe_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.userframe_6)
        self.verticalLayout_6.setContentsMargins(25, -1, -1, 15)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.placeholder_name_6 = QtWidgets.QListWidget(self.userframe_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.placeholder_name_6.sizePolicy().hasHeightForWidth())
        self.placeholder_name_6.setSizePolicy(sizePolicy)
        self.placeholder_name_6.setMaximumSize(QtCore.QSize(300, 50))
        self.placeholder_name_6.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.placeholder_name_6.setFont(font)
        self.placeholder_name_6.setObjectName("placeholder_name_6")
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.placeholder_name_6.addItem(item)
        self.verticalLayout_6.addWidget(self.placeholder_name_6)
        self.users_grid.addWidget(self.userframe_6, 2, 3, 1, 1)
        self.userframe_5 = QtWidgets.QFrame(self.Main_Grid)
        self.userframe_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 10px; \n"
"border: 2px;")
        self.userframe_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.userframe_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.userframe_5.setObjectName("userframe_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.userframe_5)
        self.verticalLayout_5.setContentsMargins(25, -1, -1, 15)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.placeholder_name_5 = QtWidgets.QListWidget(self.userframe_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.placeholder_name_5.sizePolicy().hasHeightForWidth())
        self.placeholder_name_5.setSizePolicy(sizePolicy)
        self.placeholder_name_5.setMaximumSize(QtCore.QSize(300, 50))
        self.placeholder_name_5.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.placeholder_name_5.setFont(font)
        self.placeholder_name_5.setObjectName("placeholder_name_5")
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.placeholder_name_5.addItem(item)
        self.verticalLayout_5.addWidget(self.placeholder_name_5)
        self.users_grid.addWidget(self.userframe_5, 2, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.users_grid.addItem(spacerItem10, 1, 8, 1, 1)
        self.userframe_4 = QtWidgets.QFrame(self.Main_Grid)
        self.userframe_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 10px; \n"
"border: 2px;")
        self.userframe_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.userframe_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.userframe_4.setObjectName("userframe_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.userframe_4)
        self.verticalLayout_4.setContentsMargins(25, -1, -1, 15)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.placeholder_name_4 = QtWidgets.QListWidget(self.userframe_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.placeholder_name_4.sizePolicy().hasHeightForWidth())
        self.placeholder_name_4.setSizePolicy(sizePolicy)
        self.placeholder_name_4.setMaximumSize(QtCore.QSize(300, 50))
        self.placeholder_name_4.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.placeholder_name_4.setFont(font)
        self.placeholder_name_4.setObjectName("placeholder_name_4")
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.placeholder_name_4.addItem(item)
        self.verticalLayout_4.addWidget(self.placeholder_name_4)
        self.users_grid.addWidget(self.userframe_4, 0, 7, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.users_grid.addItem(spacerItem11, 2, 6, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.users_grid.addItem(spacerItem12, 0, 6, 1, 1)
        self.userframe_8 = QtWidgets.QFrame(self.Main_Grid)
        self.userframe_8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 10px; \n"
"border: 2px;")
        self.userframe_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.userframe_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.userframe_8.setObjectName("userframe_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.userframe_8)
        self.verticalLayout_8.setContentsMargins(25, -1, -1, 15)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.placeholder_name_8 = QtWidgets.QListWidget(self.userframe_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.placeholder_name_8.sizePolicy().hasHeightForWidth())
        self.placeholder_name_8.setSizePolicy(sizePolicy)
        self.placeholder_name_8.setMaximumSize(QtCore.QSize(300, 50))
        self.placeholder_name_8.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.placeholder_name_8.setFont(font)
        self.placeholder_name_8.setObjectName("placeholder_name_8")
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.placeholder_name_8.addItem(item)
        self.verticalLayout_8.addWidget(self.placeholder_name_8)
        self.users_grid.addWidget(self.userframe_8, 2, 7, 1, 1)
        self.userframe_2 = QtWidgets.QFrame(self.Main_Grid)
        self.userframe_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 10px; \n"
"border: 2px;")
        self.userframe_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.userframe_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.userframe_2.setObjectName("userframe_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.userframe_2)
        self.verticalLayout_2.setContentsMargins(25, -1, -1, 15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.placeholder_name_2 = QtWidgets.QListWidget(self.userframe_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.placeholder_name_2.sizePolicy().hasHeightForWidth())
        self.placeholder_name_2.setSizePolicy(sizePolicy)
        self.placeholder_name_2.setMaximumSize(QtCore.QSize(300, 50))
        self.placeholder_name_2.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.placeholder_name_2.setFont(font)
        self.placeholder_name_2.setObjectName("placeholder_name_2")
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.placeholder_name_2.addItem(item)
        self.verticalLayout_2.addWidget(self.placeholder_name_2)
        self.users_grid.addWidget(self.userframe_2, 0, 3, 1, 1)
        self.gridLayout_5.addLayout(self.users_grid, 1, 0, 1, 2)
        self.gridLayout.addWidget(self.Main_Grid, 0, 0, 1, 1)
        WS_Main_Window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(WS_Main_Window)
        self.statusbar.setObjectName("statusbar")
        WS_Main_Window.setStatusBar(self.statusbar)

        self.retranslateUi(WS_Main_Window)
        QtCore.QMetaObject.connectSlotsByName(WS_Main_Window)

    def retranslateUi(self, WS_Main_Window):
        _translate = QtCore.QCoreApplication.translate
        WS_Main_Window.setWindowTitle(_translate("WS_Main_Window", "Welcome Screen"))
        self.welcome_back_header.setText(_translate("WS_Main_Window", "Welcome Back!"))
        self.welcome_back_description.setText(_translate("WS_Main_Window", "Welcome back! Choose an account below or create a new account to begin your job-seeking journey."))
        self.lbl_choose_account.setText(_translate("WS_Main_Window", "Choose your account."))
        self.label.setText(_translate("WS_Main_Window", "Don\'t have an account?"))
        self.pushButton.setText(_translate("WS_Main_Window", "Create Account"))
        __sortingEnabled = self.placeholder_name_3.isSortingEnabled()
        self.placeholder_name_3.setSortingEnabled(False)
        item = self.placeholder_name_3.item(0)
        item.setText(_translate("WS_Main_Window", "Name"))
        self.placeholder_name_3.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.placeholder_name_1.isSortingEnabled()
        self.placeholder_name_1.setSortingEnabled(False)
        item = self.placeholder_name_1.item(0)
        item.setText(_translate("WS_Main_Window", "Name"))
        self.placeholder_name_1.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.placeholder_name_7.isSortingEnabled()
        self.placeholder_name_7.setSortingEnabled(False)
        item = self.placeholder_name_7.item(0)
        item.setText(_translate("WS_Main_Window", "Name"))
        self.placeholder_name_7.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.placeholder_name_6.isSortingEnabled()
        self.placeholder_name_6.setSortingEnabled(False)
        item = self.placeholder_name_6.item(0)
        item.setText(_translate("WS_Main_Window", "Name"))
        self.placeholder_name_6.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.placeholder_name_5.isSortingEnabled()
        self.placeholder_name_5.setSortingEnabled(False)
        item = self.placeholder_name_5.item(0)
        item.setText(_translate("WS_Main_Window", "Name"))
        self.placeholder_name_5.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.placeholder_name_4.isSortingEnabled()
        self.placeholder_name_4.setSortingEnabled(False)
        item = self.placeholder_name_4.item(0)
        item.setText(_translate("WS_Main_Window", "Name"))
        self.placeholder_name_4.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.placeholder_name_8.isSortingEnabled()
        self.placeholder_name_8.setSortingEnabled(False)
        item = self.placeholder_name_8.item(0)
        item.setText(_translate("WS_Main_Window", "Name"))
        self.placeholder_name_8.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.placeholder_name_2.isSortingEnabled()
        self.placeholder_name_2.setSortingEnabled(False)
        item = self.placeholder_name_2.item(0)
        item.setText(_translate("WS_Main_Window", "Name"))
        self.placeholder_name_2.setSortingEnabled(__sortingEnabled)
# import pyqt_resource_file_rc
