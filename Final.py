# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ff_apdate1.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


import cmath
from PyQt5 import QtCore, QtGui, QtWidgets
import math
import time
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import pandas as pd
from PyQt5 import QtWidgets, uic, QtGui
import numpy as np
import pyqtgraph as pg
import os
from sympy import S, symbols, printing
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, FigureCanvasQTAgg
from matplotlib.figure import Figure
#from .mplwidget import MplWidget
from pyqtgraph import PlotWidget
import matplotlib.pyplot as plt
from PyQt5.QtCore import QObject, QThread, pyqtSignal

class MplCanvas(FigureCanvasQTAgg):

   def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        #self.axes = self.fig.add_subplot(111)
        super(MplCanvas, self).__init__(self.fig)
        
class MplCanvas2(FigureCanvasQTAgg):

   def __init__(self, parent=None, width=5, height=5, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.fig.tight_layout()
        self.axes = self.fig.add_subplot(111)
        super(MplCanvas2, self).__init__(self.fig)

class Ui_MainWindow(QtWidgets.QMainWindow):
   def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1455, 1032)
        MainWindow.setStyleSheet("QMainWindow  { background-color: white ; color: white;}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setStyleSheet("QSplitter { background-color: teal ; color: white;}")
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.all_interpolation_labels_layout = QtWidgets.QVBoxLayout(self.widget)
        self.all_interpolation_labels_layout.setContentsMargins(0, 0, 0, 0)
        self.all_interpolation_labels_layout.setObjectName("all_interpolation_labels_layout")
        self.interpolation_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.interpolation_label.setFont(font)
        self.interpolation_label.setStyleSheet("QLabel { color: white;}")
        self.interpolation_label.setAlignment(QtCore.Qt.AlignCenter)
        self.interpolation_label.setObjectName("interpolation_label")
        self.all_interpolation_labels_layout.addWidget(self.interpolation_label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.all_interpolation_labels_layout.addItem(spacerItem)
        self.choose_chunk_layout = QtWidgets.QHBoxLayout()
        self.choose_chunk_layout.setObjectName("choose_chunk_layout")
        self.chunk_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro")
        font.setPointSize(16)
        self.chunk_label.setFont(font)
        self.chunk_label.setStyleSheet("QLabel { color: white;}")
        self.chunk_label.setObjectName("chunk_label")
        self.choose_chunk_layout.addWidget(self.chunk_label)
        self.comboBox_of_chunk = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_of_chunk.setFont(font)
        self.comboBox_of_chunk.setStyleSheet("QComboBox  { background-color: white ; color: black;}")
        self.comboBox_of_chunk.setObjectName("comboBox_of_chunk")
        self.choose_chunk_layout.addWidget(self.comboBox_of_chunk)
        self.all_interpolation_labels_layout.addLayout(self.choose_chunk_layout)
        self.choose_order_layout = QtWidgets.QHBoxLayout()
        self.choose_order_layout.setObjectName("choose_order_layout")
        self.degree_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro")
        font.setPointSize(16)
        self.degree_label.setFont(font)
        self.degree_label.setStyleSheet("QLabel { color: white;}")
        self.degree_label.setObjectName("degree_label")
        self.choose_order_layout.addWidget(self.degree_label)
        self.degree1 = QtWidgets.QSpinBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.degree1.setFont(font)
        self.degree1.setStyleSheet("QSpinBox  { background-color: white ; color: black;}")
        self.degree1.setMinimum(1)
        self.degree1.setMaximum(100)
        self.degree1.setProperty("value", 1)
        self.degree1.setObjectName("degree1")
        self.choose_order_layout.addWidget(self.degree1)
        self.all_interpolation_labels_layout.addLayout(self.choose_order_layout)
        self.number_of_chunks_layout = QtWidgets.QHBoxLayout()
        self.number_of_chunks_layout.setObjectName("number_of_chunks_layout")
        self.number_of_chunk_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro")
        font.setPointSize(16)
        self.number_of_chunk_label.setFont(font)
        self.number_of_chunk_label.setStyleSheet("QLabel { color: white;}")
        self.number_of_chunk_label.setObjectName("number_of_chunk_label")
        self.number_of_chunks_layout.addWidget(self.number_of_chunk_label)
        self.chunk1 = QtWidgets.QSpinBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.chunk1.setFont(font)
        self.chunk1.setStyleSheet("QSpinBox  { background-color: white ; color: black;}")
        self.chunk1.setMinimum(0)
        self.chunk1.setMaximum(100)
        self.chunk1.setProperty("value", 0)
        self.chunk1.setObjectName("chunk1")
        self.number_of_chunks_layout.addWidget(self.chunk1)
        self.all_interpolation_labels_layout.addLayout(self.number_of_chunks_layout)
        self.portion_signal_layout = QtWidgets.QHBoxLayout()
        self.portion_signal_layout.setObjectName("portion_signal_layout")
        self.portion_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro")
        font.setPointSize(16)
        self.portion_label.setFont(font)
        self.portion_label.setStyleSheet("QLabel { color: white;}")
        self.portion_label.setObjectName("portion_label")
        self.portion_signal_layout.addWidget(self.portion_label)
        self.portion = QtWidgets.QSpinBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.portion.setFont(font)
        self.portion.setStyleSheet("QSpinBox  { background-color: white ; color: black;}")
        self.portion.setMaximum(100)
        self.portion.setSingleStep(10)
        self.portion.setProperty("value", 100)
        self.portion.setObjectName("portion")
        self.portion_signal_layout.addWidget(self.portion)
        self.all_interpolation_labels_layout.addLayout(self.portion_signal_layout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.all_interpolation_labels_layout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.open_button = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.open_button.setFont(font)
        self.open_button.setStyleSheet("QPushButton { background-color: white ; color: black;}")
        self.open_button.setObjectName("open_button")
        self.horizontalLayout_2.addWidget(self.open_button)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.all_interpolation_labels_layout.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.all_interpolation_labels_layout.addItem(spacerItem4)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.error_map_tab_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.error_map_tab_layout.setContentsMargins(0, 0, 0, 0)
        self.error_map_tab_layout.setObjectName("error_map_tab_layout")
        self.error_map_label = QtWidgets.QVBoxLayout()
        self.error_map_label.setObjectName("error_map_label")
        self.errormap_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.errormap_label.setFont(font)
        self.errormap_label.setStyleSheet("QLabel { color: white;}")
        self.errormap_label.setAlignment(QtCore.Qt.AlignCenter)
        self.errormap_label.setObjectName("errormap_label")
        self.error_map_label.addWidget(self.errormap_label)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.error_map_label.addItem(spacerItem5)
        self.error_map_tab_layout.addLayout(self.error_map_label)
        self.constant_parameter_layout = QtWidgets.QHBoxLayout()
        self.constant_parameter_layout.setObjectName("constant_parameter_layout")
        self.constant_parameter_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.constant_parameter_label.setFont(font)
        self.constant_parameter_label.setStyleSheet("QLabel { color: white;}")
        self.constant_parameter_label.setObjectName("constant_parameter_label")
        self.constant_parameter_layout.addWidget(self.constant_parameter_label)
        self.constant_choose = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.constant_choose.setFont(font)
        self.constant_choose.setStyleSheet("QComboBox  { background-color: white ; color: black;}")
        self.constant_choose.setObjectName("constant_choose")
        self.constant_choose.addItem("")
        self.constant_choose.addItem("")
        self.constant_choose.addItem("")
        self.constant_choose.addItem("")
        self.constant_parameter_layout.addWidget(self.constant_choose)
        self.error_map_tab_layout.addLayout(self.constant_parameter_layout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.constant_value_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.constant_value_label.setFont(font)
        self.constant_value_label.setStyleSheet("QLabel { color: white;}")
        self.constant_value_label.setObjectName("constant_value_label")
        self.horizontalLayout_4.addWidget(self.constant_value_label)
        self.other_parameter_value = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.other_parameter_value.setFont(font)
        self.other_parameter_value.setStyleSheet("QSpinBox  { background-color: white ; color: black;}")
        self.other_parameter_value.setMinimum(0)
        self.other_parameter_value.setMaximum(25)
        self.other_parameter_value.setObjectName("other_parameter_value")
        self.horizontalLayout_4.addWidget(self.other_parameter_value)
        self.error_map_tab_layout.addLayout(self.horizontalLayout_4)
        self.x_axis_parameter_layout = QtWidgets.QHBoxLayout()
        self.x_axis_parameter_layout.setObjectName("x_axis_parameter_layout")
        self.x_axis_parameter_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.x_axis_parameter_label.setFont(font)
        self.x_axis_parameter_label.setStyleSheet("QLabel { color: white;}")
        self.x_axis_parameter_label.setObjectName("x_axis_parameter_label")
        self.x_axis_parameter_layout.addWidget(self.x_axis_parameter_label)
        self.x_axis_choose = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.x_axis_choose.setFont(font)
        self.x_axis_choose.setStyleSheet("QComboBox  { background-color: white ; color: black;}")
        self.x_axis_choose.setObjectName("x_axis_choose")
        self.x_axis_choose.addItem("")
        self.x_axis_choose.addItem("")
        self.x_axis_choose.addItem("")
        self.x_axis_choose.addItem("")
        self.x_axis_parameter_layout.addWidget(self.x_axis_choose)
        self.error_map_tab_layout.addLayout(self.x_axis_parameter_layout)
        self.y_axis_parameter_label = QtWidgets.QHBoxLayout()
        self.y_axis_parameter_label.setObjectName("y_axis_parameter_label")
        self.y_axis_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.y_axis_label.setFont(font)
        self.y_axis_label.setStyleSheet("QLabel { color: white;}")
        self.y_axis_label.setObjectName("y_axis_label")
        self.y_axis_parameter_label.addWidget(self.y_axis_label)
        self.y_axis_choose = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.y_axis_choose.setFont(font)
        self.y_axis_choose.setStyleSheet("QComboBox  { background-color: white ; color: black;}")
        self.y_axis_choose.setObjectName("y_axis_choose")
        self.y_axis_choose.addItem("")
        self.y_axis_choose.addItem("")
        self.y_axis_choose.addItem("")
        self.y_axis_choose.addItem("")
        self.y_axis_parameter_label.addWidget(self.y_axis_choose)
        self.error_map_tab_layout.addLayout(self.y_axis_parameter_label)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.error_map_tab_layout.addItem(spacerItem6)
        self.generate_map_layout = QtWidgets.QHBoxLayout()
        self.generate_map_layout.setObjectName("generate_map_layout")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.generate_map_layout.addItem(spacerItem7)
        self.start_cancel = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.start_cancel.setFont(font)
        self.start_cancel.setStyleSheet("QPushButton { background-color: white ; color: black;}")
        self.start_cancel.setIconSize(QtCore.QSize(20, 20))
        self.start_cancel.setFlat(False)
        self.start_cancel.setObjectName("start_cancel")
        self.generate_map_layout.addWidget(self.start_cancel)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.generate_map_layout.addItem(spacerItem8)
        self.error_map_tab_layout.addLayout(self.generate_map_layout)
        self.progressbar_layout = QtWidgets.QHBoxLayout()
        self.progressbar_layout.setObjectName("progressbar_layout")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.progressbar_layout.addItem(spacerItem9)
        self.progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget_2)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.progressbar_layout.addWidget(self.progressBar)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.progressbar_layout.addItem(spacerItem10)
        self.error_map_tab_layout.addLayout(self.progressbar_layout)
        self.warning = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.warning.setFont(font)
        self.warning.setStyleSheet("QLabel{color: yellow}")
        self.warning.setObjectName("warning")
        self.error_map_tab_layout.addWidget(self.warning)
        self.warning_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.warning_2.setFont(font)
        self.warning_2.setStyleSheet("QLabel{color: yellow}")
        self.warning_2.setObjectName("warning_2")
        self.error_map_tab_layout.addWidget(self.warning_2)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.error_map_tab_layout.addItem(spacerItem11)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter_2)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = PlotWidget(self.verticalLayoutWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setBackground('w')

        self.verticalLayout.addWidget(self.graphicsView)
        self.Equation_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro")
        font.setPointSize(16)
        self.Equation_label.setFont(font)
        self.Equation_label.setStyleSheet("QLabel { color: teal;}")
        self.Equation_label.setObjectName("Equation_label")
        self.verticalLayout.addWidget(self.Equation_label)
        self.equation_layout = QtWidgets.QHBoxLayout()
        self.equation_layout.setObjectName("equation_layout")
        self.verticalLayout.addLayout(self.equation_layout)
        self.label_Error = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro")
        font.setPointSize(16)
        self.label_Error.setFont(font)
        self.label_Error.setStyleSheet("QLabel { color: teal;}")
        self.label_Error.setObjectName("label_Error")
        self.verticalLayout.addWidget(self.label_Error)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem12)
        self.Error_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Error_label.setFont(font)
        self.Error_label.setStyleSheet("QLabel {  color: black;}")
        self.Error_label.setText("")
        self.Error_label.setObjectName("Error_label")
        self.horizontalLayout.addWidget(self.Error_label)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem13)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.errormap_title = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.errormap_title.setFont(font)
        self.errormap_title.setStyleSheet("QLabel { color: teal;}")
        self.errormap_title.setText("")
        self.errormap_title.setAlignment(QtCore.Qt.AlignCenter)
        self.errormap_title.setObjectName("errormap_title")
        self.verticalLayout.addWidget(self.errormap_title)
        self.widget_errormap = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget_errormap.setObjectName("widget_errormap")
        self.widget_errormap=MplCanvas2(self)

        self.verticalLayout.addWidget(self.widget_errormap)
        self.gridLayout.addWidget(self.splitter_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1455, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

   def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.interpolation_label.setText(_translate("MainWindow", "Interpolation setting"))
        self.chunk_label.setText(_translate("MainWindow", "Choose the chunk :  "))
        self.degree_label.setText(_translate("MainWindow", "Order of polynomial :"))
        self.number_of_chunk_label.setText(_translate("MainWindow", "Number of chunks :  "))
        self.portion_label.setText(_translate("MainWindow", "Portion of signal :     "))
        self.open_button.setText(_translate("MainWindow", "Open the signal"))
        self.errormap_label.setText(_translate("MainWindow", "Error map setting"))
        self.constant_parameter_label.setText(_translate("MainWindow", "Constant parameter :"))
        self.constant_choose.setItemText(0, _translate("MainWindow", "None"))
        self.constant_choose.setItemText(1, _translate("MainWindow", "overlapping"))
        self.constant_choose.setItemText(2, _translate("MainWindow", "chunks"))
        self.constant_choose.setItemText(3, _translate("MainWindow", "order of interpolation"))
        self.constant_value_label.setText(_translate("MainWindow", "Constant value :"))
        self.x_axis_parameter_label.setText(_translate("MainWindow", "X-axis parameter:"))
        self.x_axis_choose.setItemText(0, _translate("MainWindow", "None"))
        self.x_axis_choose.setItemText(1, _translate("MainWindow", "overlapping"))
        self.x_axis_choose.setItemText(2, _translate("MainWindow", "chunks"))
        self.x_axis_choose.setItemText(3, _translate("MainWindow", "order of interpolation"))
        self.y_axis_label.setText(_translate("MainWindow", "Y-axis parameter :"))
        self.y_axis_choose.setItemText(0, _translate("MainWindow", "None"))
        self.y_axis_choose.setItemText(1, _translate("MainWindow", "overlapping"))
        self.y_axis_choose.setItemText(2, _translate("MainWindow", "chunks"))
        self.y_axis_choose.setItemText(3, _translate("MainWindow", "order of interpolation"))
        self.start_cancel.setText(_translate("MainWindow", "Calculate error map"))
        self.warning.setText(_translate("MainWindow", "*Please complete your data"))
        self.warning_2.setText(_translate("MainWindow", "*Please don\'t choose the same option more than once"))
        self.Equation_label.setText(_translate("MainWindow", "Interpolation equation :"))
        self.label_Error.setText(_translate("MainWindow", "Interpolation error:"))

#-----------------------------------------------------------------------
#                              setting:


        # setting in gui in interpolation side:

        self.Canvas_for_equation = MplCanvas(self, width=0.3, height=0.3)
        self.equation_layout.addWidget(self.Canvas_for_equation)

        self.comboBox_of_chunk.currentIndexChanged.connect(lambda :self.disply_equation())
        self.chunk1.valueChanged.connect(lambda:self.polyfit())
        self.degree1.valueChanged.connect(lambda:self.polyfit())
        self.portion.valueChanged.connect(lambda:self.extrapolation())
        #self.actionOpen.triggered.connect(lambda:self.open_signal())
        self.open_button.clicked.connect(lambda:self.open_signal())

        # setting in gui in error map side:
        self.timer1 = QtCore.QTimer()
        self.progressBar.hide()
       # self.other_parameter_value.hide()
       # self.other_parameter_value.hide()
        self.progressBar.hide()
        self.warning.hide()
        self.warning_2.hide()
        self.widget_errormap.hide()
     #   self.start_cancel.setText('Calculate error map')



        # some of action in error map side:
        self.start_cancel.clicked.connect(self.doAction)

        #  resitting the error map:
        self.constant_choose.currentIndexChanged.connect(self.initiate)
        self.other_parameter_value.valueChanged.connect(self.initiate)
        self.other_parameter_value.valueChanged.connect(self.initiate)
        self.x_axis_choose.currentIndexChanged.connect(self.initiate)
        self.y_axis_choose.currentIndexChanged.connect(self.initiate)

#-------------------------------interpolation---------------------------

   def open_signal(self):
        self.file_name1 = QtWidgets.QFileDialog.getOpenFileNames(
            self, 'Open only txt or CSV or xls', os.getenv('HOME'))
        self.read_file1(self.file_name1[0][0])

    #Define original signal
   x_original_signal=[]
   y_original_signal=[]
   def read_file1(self, file_path):
        self.graphicsView.clear()

        self.path1 = file_path
        data1 = pd.read_csv(self.path1)
        self.y_original_signal = data1.values[:, 1]
        self.x_original_signal = data1.values[:, 0]

        pen = pg.mkPen(color=(200, 10, 0), width=2)
        self.graphicsView.plot(self.x_original_signal, self.y_original_signal, pen=pen)

   def chunker_list(self):
        self.num_chunk = self.chunk1.value()
        self.x1_signal = self.x_original_signal
        self.y1_signal = self.y_original_signal

        self.x_splited = np.array(np.array_split(self.x1_signal,self.num_chunk))
        self.y_splited = np.array(np.array_split(self.y1_signal,self.num_chunk))

        return (self.x_splited,self.y_splited)

   equation_list = []
   errors_list = []
   def polyfit (self):
        self.graphicsView.clear()
        self.comboBox_of_chunk.clear()
        self.equation_list.clear()
        self.errors_list.clear()

        #plot original signal
        pen = pg.mkPen(color=(200, 10, 0), width=2)
        self.graphicsView.plot(self.x_original_signal, self.y_original_signal, pen=pen)

        if self.portion.value() != 100:
            self.extrapolation()
        else:
            self.x_signal = self.chunker_list()[0]
            self.y_signal = self.chunker_list()[1]
            self.degree=self.degree1.value()
            x = symbols("x")

            for i in range(len(self.x_signal)):
                interpolated=np.polyfit(self.x_signal[i],self.y_signal[i],self.degree)
                self.ynew=np.poly1d(interpolated)

                #plot interpolated
                pen = pg.mkPen(color=(0, 0, 255), width=3, style=QtCore.Qt.DotLine)
                self.graphicsView.plot(self.x_signal[i], self.ynew(self.x_signal[i]), pen=pen)

                #error
                self.error1=self.sqr_error(self.ynew, self.x_signal[i], self.y_signal[i])
                self.errors_list.append(str(self.error1))

                #equation
                poly= sum(S("{:6.2f}".format(v))* x ** i for i,v in enumerate(interpolated[::-1]))
                self.eq_latex= printing.latex(poly)
                label = "${}$".format(self.eq_latex)
                self.equation_list.append(label)
                self.comboBox_of_chunk.addItem((str("chunk "+str(i+1))))

            label = self.equation_list[0]
            self.Canvas_for_equation.fig.suptitle(label)
            self.Canvas_for_equation.draw()
            self.Error_label.setText(self.errors_list[0])


   def sqr_error(self,p, x_chunk, y_chunk):
        self.diff2 = (p(x_chunk)-y_chunk)**2
        return self.diff2.sum()


   def disply_equation(self):
        index = self.comboBox_of_chunk.currentIndex()
        label = self.equation_list[index]
        self.Canvas_for_equation.fig.suptitle(label)
        self.Canvas_for_equation.draw()
        error = self.errors_list[index]
        self.Error_label.setText(error)


   def extrapolation(self):
        self.graphicsView.clear()
        self.comboBox_of_chunk.clear()
        self.Error_label.setText(" ")
        label = " "
        self.Canvas_for_equation.fig.suptitle(label)
        self.Canvas_for_equation.draw()

        pen = pg.mkPen(color=(200, 10, 0), width=2)
        self.graphicsView.plot(self.x_original_signal, self.y_original_signal, pen=pen)


        self.percent = self.portion.value()/100
        self.x_first=self.x_original_signal[:int(len( self.x_original_signal)*self.percent)]
        self.y_first=self.y_original_signal[:int(len( self.y_original_signal)*self.percent)]
        self.degree=self.degree1.value()
        interpolated_coeff=np.polyfit(self.x_first,self.y_first,self.degree)
        ynew=np.poly1d(interpolated_coeff)

        pen = pg.mkPen(color=(10, 100, 200), width=3, style=QtCore.Qt.DotLine)
        self.graphicsView.plot(self.x_original_signal,ynew(self.x_original_signal), pen = pen)


#-------------------------------error map----------------------------------

   def update_progressbar(self):
        self.progressBar.setValue(self.progressBar.value()+1)
        if self.progressBar.value()==100:
            self.start_cancel.setText('Calculate error map')
            self.timer1.stop()
            self.progressBar.hide()
            self.widget_errormap.show()
            self.widget_errormap.fig.clear()
            self.axes=self.widget_errormap.fig.add_subplot(111)
            self.widget_errormap.draw()
            self.x_axis_array=[1,2,3,4,5]
            self.countour=self.axes.contourf(self.x_axis_array,self.x_axis_array,self.err,cmap='viridis')
            self.axes.set_xlabel(self.x_parameter)
            self.axes.set_ylabel(self.y_parameter)
            self.widget_errormap.fig.colorbar(self.countour)
            self.widget_errormap.draw()
            self.widget_errormap.show()
            self.errormap_title.setText(' Error map')

            
            


   def doAction(self):
        if self.x_axis_choose.currentText()=='None' or self.y_axis_choose.currentText()=='None' or self.constant_choose.currentText()=='None':
            self.warning.show()
        elif self.x_axis_choose.currentText()==self.y_axis_choose.currentText() or self.y_axis_choose.currentText()==self.constant_choose.currentText() or self.constant_choose.currentText()==self.x_axis_choose.currentText():
            self.warning_2.show()
        else:
            if self.start_cancel.text()=='Calculate error map':
                self.initiate()
                self.start_cancel.setText('Cancel')
                self.timer1.start(50)
                self.timer1.timeout.connect(self.update_progressbar)
                self.progressBar.show()
                self.warning.hide()
                self.warning_2.hide()
                self.constant_parameter=self.constant_choose.currentText()
                self.x_parameter=self.x_axis_choose.currentText()
                self.y_parameter=self.y_axis_choose.currentText()
                self.overlap_array=[5,10,15,20,25]
                self.otherparameter_array=[2,3,4,5,6]

                if self.x_parameter=='overlapping'  :
                    self.create_errormap(self.overlap_array,self.otherparameter_array,self.other_parameter_value.value())
                elif self.y_parameter=='overlapping' :
                    self.create_errormap(self.otherparameter_array,self.overlap_array,self.other_parameter_value.value())
                else:
                    self.create_errormap(self.otherparameter_array,self.otherparameter_array,self.other_parameter_value.value())
            else:
                self.start_cancel.setText('Calculate error map')
                self.timer1.stop()
                self.progressBar.hide()
                self.initiate()


   def create_errormap(self,x_axis,y_axis,constant_value):
        self.x_axis_copy1=x_axis
        self.y_axis_copy1=y_axis
        self.constant_copy1=constant_value
        self.error_array=self.calculate_errormap(self.x_axis_copy1,self.y_axis_copy1,self.constant_copy1)
        self.err=np.reshape(self.error_array,(len(self.x_axis_copy1),len(self.y_axis_copy1)))

   error_f=[]
   def calculate_errormap(self,x_axis1,y_axis1,constant_value1):
        self.x_axis_copy2=x_axis1
        self.y_axis_copy2=y_axis1
        self.constant_copy2=constant_value1

        if  self.constant_parameter=='overlapping':
            for y in self.y_axis_copy2:
                for x in self.x_axis_copy2:
                    self.error_value=self.fill_matrix_chunk_order(x,y,self.constant_copy2)
                    self.error_f.append(self.error_value)
            return self.error_f
        else:
             for y in self.y_axis_copy2:
                for x in self.x_axis_copy2:
                    self.error_value=self.fill_matrix_overlap(x,y,self.constant_copy2)
                    self.error_f.append(self.error_value)
             return self.error_f



   def fill_matrix_chunk_order(self,x_cell,y_cell,constant_value2):
        self.overlapping=constant_value2
        if self.x_parameter=='chunks' and self.y_parameter=='order of interpolation':
               self.num_chunk=x_cell
               self.degree=y_cell
        else:
            self.num_chunk=y_cell
            self.degree=x_cell

        self.cell_error=self.calculate_thecell_error(self.num_chunk,self.degree,self.overlapping)
        return self.cell_error


    #ynew2=[]
   def fill_matrix_overlap(self,x_cell,y_cell,constant_value2):
        self.constant_copy4=constant_value2

# which is in x_axis and which in y_axis:
        if self.x_parameter=='chunks' :
            self.num_chunk=x_cell
            self.degree=constant_value2
            self.overlapping=y_cell

        elif self.x_parameter=='order of interpolation' :
            self.num_chunk=constant_value2
            self.degree=x_cell
            self.overlapping=y_cell
        elif  self.y_parameter=='chunks' :
            self.num_chunk=y_cell
            self.degree=constant_value2
            self.overlapping=x_cell
        else:
            self.num_chunk=constant_value2
            self.degree=y_cell
            self.overlapping=x_cell

        self.cell_error=self.calculate_thecell_error(self.num_chunk,self.degree,self.overlapping)
        return self.cell_error

   def calculate_thecell_error(self,num_chunk,degree,overlapping):
        self.error=[]
        self.ynew_value=[]
        self.num_chunk_copy=num_chunk
        self.degree_copy=degree
        self.percent=overlapping

        self.size_chunck=int(len(self.x_original_signal)/self.num_chunk_copy)
        self.add_item=int(self.size_chunck*self.percent/100)
        self.x_splited =[self.x_original_signal[i:i+self.size_chunck] for i in range(0,len(self.x_original_signal),self.size_chunck-self.add_item)]
        self.y_splited =[self.y_original_signal[i:i+self.size_chunck] for i in range(0,len(self.x_original_signal),self.size_chunck-self.add_item)]
        for i in range(len(self.x_splited)):
            interpolated=np.polyfit(self.x_splited[i],self.y_splited[i],self.degree_copy)
            self.equation_of_ynew=np.poly1d(interpolated)
            self.ynew_value.append(self.equation_of_ynew(self.x_splited[i]))

        for i in range(len(self.y_splited)):
            for j in range(len(self.y_splited[i])):
                self.error.append(((self.y_splited[i][j]-self.ynew_value[i][j])/ self.y_splited[i][j])*100)

        return np.median(self.error)


   def initiate(self):
        self.widget_errormap.hide()
        self.errormap_title.setText(' ')
        self.error=[]
        self.ynew_value=[]
        self.error_f=[]
        self.progressBar.setValue(0)
        self.warning.hide()
        self.warning_2.hide()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
