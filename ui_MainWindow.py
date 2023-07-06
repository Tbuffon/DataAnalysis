# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(649, 489)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_16.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_16.setSpacing(6)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(6)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_2 = QtWidgets.QFrame(self.tab)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setMaximumSize(QtCore.QSize(230, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.btn = QtWidgets.QPushButton(self.groupBox_2)
        self.btn.setObjectName("btn")
        self.gridLayout.addWidget(self.btn, 5, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.frame)
        self.widgetHist = QmyFigureCanvas(self.frame_2)
        self.widgetHist.setObjectName("widgetHist")
        self.horizontalLayout.addWidget(self.widgetHist)
        self.verticalLayout_11.addWidget(self.frame_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.tab_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_10 = QtWidgets.QFrame(self.frame_3)
        self.frame_10.setMaximumSize(QtCore.QSize(220, 16777215))
        self.frame_10.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_14.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_14.setSpacing(6)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.groupBox_6 = QtWidgets.QGroupBox(self.frame_10)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_13.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_13.setSpacing(12)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.radioFill_Both = QtWidgets.QRadioButton(self.groupBox_6)
        self.radioFill_Both.setChecked(True)
        self.radioFill_Both.setObjectName("radioFill_Both")
        self.verticalLayout_13.addWidget(self.radioFill_Both)
        self.radioFill_Up = QtWidgets.QRadioButton(self.groupBox_6)
        self.radioFill_Up.setObjectName("radioFill_Up")
        self.verticalLayout_13.addWidget(self.radioFill_Up)
        self.radioFill_Down = QtWidgets.QRadioButton(self.groupBox_6)
        self.radioFill_Down.setObjectName("radioFill_Down")
        self.verticalLayout_13.addWidget(self.radioFill_Down)
        self.btnFill_tightLayout = QtWidgets.QPushButton(self.groupBox_6)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/39.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnFill_tightLayout.setIcon(icon)
        self.btnFill_tightLayout.setObjectName("btnFill_tightLayout")
        self.verticalLayout_13.addWidget(self.btnFill_tightLayout)
        self.chkBoxFill_gridLine = QtWidgets.QCheckBox(self.groupBox_6)
        self.chkBoxFill_gridLine.setObjectName("chkBoxFill_gridLine")
        self.verticalLayout_13.addWidget(self.chkBoxFill_gridLine)
        self.verticalLayout_14.addWidget(self.groupBox_6)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_14.addItem(spacerItem1)
        self.horizontalLayout_2.addWidget(self.frame_10)
        self.widgetHist_2 = QmyFigureCanvas(self.frame_3)
        self.widgetHist_2.setObjectName("widgetHist_2")
        self.horizontalLayout_2.addWidget(self.widgetHist_2)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_4 = QtWidgets.QFrame(self.tab_3)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_7 = QtWidgets.QFrame(self.frame_4)
        self.frame_7.setMaximumSize(QtCore.QSize(220, 16777215))
        self.frame_7.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame_7)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setVerticalSpacing(12)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btnPie_tightLayout = QtWidgets.QPushButton(self.groupBox_4)
        self.btnPie_tightLayout.setIcon(icon)
        self.btnPie_tightLayout.setObjectName("btnPie_tightLayout")
        self.gridLayout_3.addWidget(self.btnPie_tightLayout, 4, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        self.chkBoxPie_Legend = QtWidgets.QCheckBox(self.groupBox_4)
        self.chkBoxPie_Legend.setChecked(True)
        self.chkBoxPie_Legend.setObjectName("chkBoxPie_Legend")
        self.gridLayout_3.addWidget(self.chkBoxPie_Legend, 2, 1, 1, 1)
        self.btnPie_redraw = QtWidgets.QPushButton(self.groupBox_4)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/828.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPie_redraw.setIcon(icon1)
        self.btnPie_redraw.setObjectName("btnPie_redraw")
        self.gridLayout_3.addWidget(self.btnPie_redraw, 4, 0, 1, 1)
        self.spinPie_HoleSize = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.spinPie_HoleSize.setMaximum(0.9)
        self.spinPie_HoleSize.setSingleStep(0.1)
        self.spinPie_HoleSize.setProperty("value", 0.1)
        self.spinPie_HoleSize.setObjectName("spinPie_HoleSize")
        self.gridLayout_3.addWidget(self.spinPie_HoleSize, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)
        self.comboPie_explode = QtWidgets.QComboBox(self.groupBox_4)
        self.comboPie_explode.setObjectName("comboPie_explode")
        self.comboPie_explode.addItem("")
        self.comboPie_explode.addItem("")
        self.comboPie_explode.addItem("")
        self.comboPie_explode.addItem("")
        self.comboPie_explode.addItem("")
        self.comboPie_explode.addItem("")
        self.comboPie_explode.addItem("")
        self.comboPie_explode.addItem("")
        self.gridLayout_3.addWidget(self.comboPie_explode, 1, 1, 1, 1)
        self.verticalLayout_5.addWidget(self.groupBox_4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.horizontalLayout_7.addWidget(self.frame_7)
        self.widgetPie = QmyFigureCanvas(self.frame_4)
        self.widgetPie.setObjectName("widgetPie")
        self.horizontalLayout_7.addWidget(self.widgetPie)
        self.verticalLayout_8.addWidget(self.frame_4)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_5 = QtWidgets.QFrame(self.tab_4)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setMaximumSize(QtCore.QSize(230, 16777215))
        self.frame_6.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame_6)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.spinStem_PointCount = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinStem_PointCount.setMinimum(1)
        self.spinStem_PointCount.setMaximum(900000)
        self.spinStem_PointCount.setProperty("value", 20)
        self.spinStem_PointCount.setObjectName("spinStem_PointCount")
        self.horizontalLayout_4.addWidget(self.spinStem_PointCount)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.chkBoxStem_Analog = QtWidgets.QCheckBox(self.groupBox_3)
        self.chkBoxStem_Analog.setChecked(True)
        self.chkBoxStem_Analog.setObjectName("chkBoxStem_Analog")
        self.verticalLayout_4.addWidget(self.chkBoxStem_Analog)
        self.chkBoxStem_Holder = QtWidgets.QCheckBox(self.groupBox_3)
        self.chkBoxStem_Holder.setChecked(True)
        self.chkBoxStem_Holder.setObjectName("chkBoxStem_Holder")
        self.verticalLayout_4.addWidget(self.chkBoxStem_Holder)
        self.chkBoxStem_Legend = QtWidgets.QCheckBox(self.groupBox_3)
        self.chkBoxStem_Legend.setChecked(True)
        self.chkBoxStem_Legend.setObjectName("chkBoxStem_Legend")
        self.verticalLayout_4.addWidget(self.chkBoxStem_Legend)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btnStem_redraw = QtWidgets.QPushButton(self.groupBox_3)
        self.btnStem_redraw.setIcon(icon1)
        self.btnStem_redraw.setObjectName("btnStem_redraw")
        self.horizontalLayout_6.addWidget(self.btnStem_redraw)
        self.btnStem_tightLayout = QtWidgets.QPushButton(self.groupBox_3)
        self.btnStem_tightLayout.setIcon(icon)
        self.btnStem_tightLayout.setObjectName("btnStem_tightLayout")
        self.horizontalLayout_6.addWidget(self.btnStem_tightLayout)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.verticalLayout_6.addWidget(self.groupBox_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem3)
        self.horizontalLayout_5.addWidget(self.frame_6)
        self.widgetStem = QmyFigureCanvas(self.frame_5)
        self.widgetStem.setObjectName("widgetStem")
        self.horizontalLayout_5.addWidget(self.widgetStem)
        self.verticalLayout_7.addWidget(self.frame_5)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(6)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_8 = QtWidgets.QFrame(self.tab_5)
        self.frame_8.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_9 = QtWidgets.QFrame(self.frame_8)
        self.frame_9.setMaximumSize(QtCore.QSize(230, 16777215))
        self.frame_9.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_10.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.groupBox_5 = QtWidgets.QGroupBox(self.frame_9)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_9.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setHorizontalSpacing(6)
        self.gridLayout_4.setVerticalSpacing(10)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.chkBoxPolar_direction = QtWidgets.QCheckBox(self.groupBox_5)
        self.chkBoxPolar_direction.setChecked(True)
        self.chkBoxPolar_direction.setObjectName("chkBoxPolar_direction")
        self.gridLayout_4.addWidget(self.chkBoxPolar_direction, 0, 0, 1, 1)
        self.chkBoxPolar_gridOn = QtWidgets.QCheckBox(self.groupBox_5)
        self.chkBoxPolar_gridOn.setChecked(True)
        self.chkBoxPolar_gridOn.setObjectName("chkBoxPolar_gridOn")
        self.gridLayout_4.addWidget(self.chkBoxPolar_gridOn, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_5)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 1, 0, 1, 1)
        self.spinPolar_offset = QtWidgets.QSpinBox(self.groupBox_5)
        self.spinPolar_offset.setMinimum(-180)
        self.spinPolar_offset.setMaximum(180)
        self.spinPolar_offset.setSingleStep(10)
        self.spinPolar_offset.setProperty("value", 0)
        self.spinPolar_offset.setObjectName("spinPolar_offset")
        self.gridLayout_4.addWidget(self.spinPolar_offset, 1, 1, 1, 1)
        self.btnPolar_tightLayout = QtWidgets.QPushButton(self.groupBox_5)
        self.btnPolar_tightLayout.setIcon(icon)
        self.btnPolar_tightLayout.setObjectName("btnPolar_tightLayout")
        self.gridLayout_4.addWidget(self.btnPolar_tightLayout, 2, 1, 1, 1)
        self.btnPolar_redraw = QtWidgets.QPushButton(self.groupBox_5)
        self.btnPolar_redraw.setIcon(icon1)
        self.btnPolar_redraw.setObjectName("btnPolar_redraw")
        self.gridLayout_4.addWidget(self.btnPolar_redraw, 2, 0, 1, 1)
        self.verticalLayout_9.addLayout(self.gridLayout_4)
        self.line = QtWidgets.QFrame(self.groupBox_5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_9.addWidget(self.line)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setHorizontalSpacing(6)
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtWidgets.QLabel(self.groupBox_5)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.spinPolar_rotation = QtWidgets.QSpinBox(self.groupBox_5)
        self.spinPolar_rotation.setMinimum(-180)
        self.spinPolar_rotation.setMaximum(180)
        self.spinPolar_rotation.setProperty("value", 90)
        self.spinPolar_rotation.setObjectName("spinPolar_rotation")
        self.gridLayout_2.addWidget(self.spinPolar_rotation, 0, 1, 1, 1)
        self.btnPolar_rotate = QtWidgets.QPushButton(self.groupBox_5)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/images/exec.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPolar_rotate.setIcon(icon2)
        self.btnPolar_rotate.setObjectName("btnPolar_rotate")
        self.gridLayout_2.addWidget(self.btnPolar_rotate, 1, 1, 1, 1)
        self.verticalLayout_9.addLayout(self.gridLayout_2)
        self.verticalLayout_10.addWidget(self.groupBox_5)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem4)
        self.horizontalLayout_8.addWidget(self.frame_9)
        self.widgetPolar = QmyFigureCanvas(self.frame_8)
        self.widgetPolar.setObjectName("widgetPolar")
        self.horizontalLayout_8.addWidget(self.widgetPolar, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_12.addWidget(self.frame_8)
        self.tabWidget.addTab(self.tab_5, "")
        self.verticalLayout_16.addWidget(self.tabWidget)
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setMinimumSize(QtCore.QSize(100, 100))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 200))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_17.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_17.setSpacing(6)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.logOutputText = QtWidgets.QPlainTextEdit(self.groupBox)
        self.logOutputText.setReadOnly(True)
        self.logOutputText.setObjectName("logOutputText")
        self.verticalLayout_17.addWidget(self.logOutputText)
        self.verticalLayout_16.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 649, 19))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menuBar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menuBar)
        self.actQuit = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/images/exit_24.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actQuit.setIcon(icon3)
        self.actQuit.setObjectName("actQuit")
        self.actTightLayout = QtWidgets.QAction(MainWindow)
        self.actTightLayout.setIcon(icon)
        self.actTightLayout.setObjectName("actTightLayout")
        self.actScatterAgain = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/images/017.GIF"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actScatterAgain.setIcon(icon4)
        self.actScatterAgain.setObjectName("actScatterAgain")
        self.actSetCursor = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/images/range.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actSetCursor.setIcon(icon5)
        self.actSetCursor.setObjectName("actSetCursor")
        self.actOpenFolder = QtWidgets.QAction(MainWindow)
        self.actOpenFolder.setObjectName("actOpenFolder")
        self.menu_2.addAction(self.actOpenFolder)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.actQuit.triggered.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QChart绘图详细功能"))
        self.groupBox_2.setTitle(_translate("MainWindow", "操作"))
        self.btn.setText(_translate("MainWindow", "运行"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "直方图"))
        self.groupBox_6.setTitle(_translate("MainWindow", "图表操作"))
        self.radioFill_Both.setText(_translate("MainWindow", "曲线与0之间填充"))
        self.radioFill_Up.setText(_translate("MainWindow", "填充y>=0的部分"))
        self.radioFill_Down.setText(_translate("MainWindow", "填充y<=0的部分"))
        self.btnFill_tightLayout.setText(_translate("MainWindow", "紧凑布局"))
        self.chkBoxFill_gridLine.setText(_translate("MainWindow", "显示网格线"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "填充图"))
        self.groupBox_4.setTitle(_translate("MainWindow", "图表操作"))
        self.btnPie_tightLayout.setText(_translate("MainWindow", "紧凑布局"))
        self.label_4.setText(_translate("MainWindow", "空心圆大小"))
        self.chkBoxPie_Legend.setText(_translate("MainWindow", "显示图例"))
        self.btnPie_redraw.setText(_translate("MainWindow", "重画饼图"))
        self.label_5.setText(_translate("MainWindow", "突出显示的块"))
        self.comboPie_explode.setItemText(0, _translate("MainWindow", "Monday"))
        self.comboPie_explode.setItemText(1, _translate("MainWindow", "Tuesday"))
        self.comboPie_explode.setItemText(2, _translate("MainWindow", "Wednesday"))
        self.comboPie_explode.setItemText(3, _translate("MainWindow", "Thursday"))
        self.comboPie_explode.setItemText(4, _translate("MainWindow", "Friday"))
        self.comboPie_explode.setItemText(5, _translate("MainWindow", "Saturday"))
        self.comboPie_explode.setItemText(6, _translate("MainWindow", "Sunday"))
        self.comboPie_explode.setItemText(7, _translate("MainWindow", "None"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "饼图"))
        self.groupBox_3.setTitle(_translate("MainWindow", "图表操作"))
        self.label_3.setText(_translate("MainWindow", "采样点数"))
        self.chkBoxStem_Analog.setText(_translate("MainWindow", "显示连续信号"))
        self.chkBoxStem_Holder.setText(_translate("MainWindow", "显示采样保持信号"))
        self.chkBoxStem_Legend.setText(_translate("MainWindow", "显示图例"))
        self.btnStem_redraw.setText(_translate("MainWindow", "重画曲线"))
        self.btnStem_tightLayout.setText(_translate("MainWindow", "紧凑布局"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "火柴杆图"))
        self.groupBox_5.setTitle(_translate("MainWindow", "极坐标图"))
        self.chkBoxPolar_direction.setText(_translate("MainWindow", "逆时针方向"))
        self.chkBoxPolar_gridOn.setText(_translate("MainWindow", "显示网格"))
        self.label_6.setText(_translate("MainWindow", "角度偏移量"))
        self.spinPolar_offset.setSuffix(_translate("MainWindow", "°"))
        self.btnPolar_tightLayout.setText(_translate("MainWindow", "紧凑布局"))
        self.btnPolar_redraw.setText(_translate("MainWindow", "曲线复位"))
        self.label_7.setText(_translate("MainWindow", "旋转角度"))
        self.spinPolar_rotation.setSuffix(_translate("MainWindow", "°"))
        self.btnPolar_rotate.setText(_translate("MainWindow", "旋转"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "极坐标图"))
        self.groupBox.setTitle(_translate("MainWindow", "log"))
        self.menu_2.setTitle(_translate("MainWindow", "文件"))
        self.actQuit.setText(_translate("MainWindow", "退出"))
        self.actQuit.setToolTip(_translate("MainWindow", "退出"))
        self.actTightLayout.setText(_translate("MainWindow", "紧凑布局"))
        self.actTightLayout.setToolTip(_translate("MainWindow", "重新紧凑布局"))
        self.actScatterAgain.setText(_translate("MainWindow", "重新生成散点数据"))
        self.actScatterAgain.setToolTip(_translate("MainWindow", "重新生成散点数据"))
        self.actSetCursor.setText(_translate("MainWindow", "十字光标"))
        self.actSetCursor.setToolTip(_translate("MainWindow", "设置为十字光标"))
        self.actOpenFolder.setText(_translate("MainWindow", "打开文件夹"))
from myFigureCanvas import QmyFigureCanvas
import res_rc
