# -*- coding: utf-8 -*-

import sys, os, time

from PyQt5.QtWidgets import  QApplication, QMainWindow, QFileDialog

from PyQt5.QtCore import  pyqtSlot,QCoreApplication,Qt

import numpy as np

import pandas as pd

import matplotlib as mpl

from ui_MainWindow import Ui_MainWindow

from myFigureCanvas import QmyFigureCanvas

class QmyMainWindow(QMainWindow): 

   def __init__(self, parent=None):
      super().__init__(parent)   #调用父类构造函数，创建窗体
      self.ui=Ui_MainWindow()    #创建UI对象
      self.ui.setupUi(self)      #构造UI界面

      self.setWindowTitle("Demo14_4, 几种常见二维图表")
      self.setCentralWidget(self.ui.centralWidget)
      self.list_t = []
      self.current = []
      self.photocurrent = []
      self.ref = []
      pass

##  ==============自定义功能函数========================
   def __drawHist(self,pointCount=2000, binsCount=40):  #绘制统计直方图
      pass


   def __drawFill(self):  ##绘制填充图
      pass


   def __drawPie(self):  ##绘制饼图
      pass


   def __drawStem(self):  ##绘制火柴杆图
      pass

   def __getAllData(self, photocurrent_file):   ##获取所有数据
      list_t, current, photocurrent, ref = [], [], [], []
      for file in photocurrent_file:
         if file[-3:] == 'txt':
            self.ui.logOutputText.appendPlainText(str(file) + '\t analysing...')
            QCoreApplication.processEvents()
            my_data = pd.read_csv(file,sep="\t")
            list_t.extend(my_data['time /s'])
            photocurrent.extend(my_data['Photocurrent A'])
            current.extend(my_data['Current A'])
            ref.extend(my_data['Ref A'])
      list_t=np.array(list_t).reshape(-1,1)
      photocurrent=np.array(photocurrent).reshape(-1,1)
      current=np.array(current).reshape(-1,1)
      ref=np.array(ref).reshape(-1,1)
      return list_t,photocurrent,current,ref   

      
##  ==============event处理函数==========================


##  ==========由connectSlotsByName()自动连接的槽函数============

##===========Action对象============
   @pyqtSlot() 
   def on_actOpenFolder_triggered(self):
      """打开文件夹"""
      folder_path = QFileDialog.getExistingDirectory(self, "选择文件夹", "./")
      if folder_path:
         self.ui.logOutputText.appendPlainText("打开文件夹：" + folder_path)
      os.chdir(folder_path)
      filedir=os.listdir(os.getcwd())
      photocurrent_file=[]
      for filename in filedir:
         if  filename.startswith('Bias')&filename.endswith('.txt'):
            photocurrent_file.append(filename)
      self.ui.logOutputText.appendPlainText("文件夹中的文件有：" + str(photocurrent_file))
      QCoreApplication.processEvents()
      start_time = time.perf_counter()
      self.list_t,self.photocurrent,self.current,self.ref = self.__getAllData(photocurrent_file)
      time_used = (time.perf_counter() - start_time)
      # print("Time used: %s s" % (int(time_used)),'/n','==== Done! ====')
      str_finish = "Time used: %s s" % (int(time_used)) + '\n' + '==== Done! ===='
      self.ui.logOutputText.appendPlainText(str_finish)
      

##===========page 1 直方图============
   @pyqtSlot(bool)   ##显示工具栏
   def on_gBoxHist_toolbar_clicked(self,checked):
      pass

      
   @pyqtSlot(bool)   ## 显示坐标提示
   def on_chkBoxHist_ShowHint_clicked(self,checked):
      pass

      
   @pyqtSlot()    ## 紧凑布局
   def on_btnHist_tightLayout_clicked(self):
      pass


   @pyqtSlot()    ## 重画图表
   def on_btnHist_redraw_clicked(self):
      pass


   @pyqtSlot(bool)   ##显示图例
   def on_chkBoxHist_Legend_clicked(self,checked):
      pass


##=======2.填充图=========
   @pyqtSlot()   ##曲线与0之间填充
   def on_radioFill_Both_clicked(self):
      pass

      
   @pyqtSlot()   ##填充y>=0的部分
   def on_radioFill_Up_clicked(self):
      pass


   @pyqtSlot()   ##填充y<=0的部分
   def on_radioFill_Down_clicked(self):
      pass

      
   @pyqtSlot()   ##紧凑布局
   def on_btnFill_tightLayout_clicked(self):
      pass


   @pyqtSlot(bool)   ##显示网格线
   def on_chkBoxFill_gridLine_clicked(self,checked):
      pass


##=======3.饼图=========
   @pyqtSlot()   ## 重画饼图
   def on_btnPie_redraw_clicked(self):
      pass


   @pyqtSlot()   ## 紧凑布局
   def on_btnPie_tightLayout_clicked(self):
      pass

      
   @pyqtSlot(bool)   ## 显示图例
   def on_chkBoxPie_Legend_clicked(self,checked):
      pass

      
##=====4.火柴杆图==============
   @pyqtSlot()   ## 重画曲线
   def on_btnStem_redraw_clicked(self):
      pass

      
   @pyqtSlot()   ##紧凑布局
   def on_btnStem_tightLayout_clicked(self):
      pass


   @pyqtSlot(bool)   ## 显示连续信号
   def on_chkBoxStem_Analog_clicked(self,checked):
      pass

      
   @pyqtSlot(bool)   ## 显示采样保持信号
   def on_chkBoxStem_Holder_clicked(self,checked):
      pass


   @pyqtSlot(bool)   ## 显示图例
   def on_chkBoxStem_Legend_clicked(self,checked):
      pass


##=====5.极坐标图========
   def __drawPolarSpiral(self):  ##绘制螺旋线
      pass

     
   @pyqtSlot()    ## 重画曲线
   def on_btnPolar_redraw_clicked(self):
      pass


   @pyqtSlot(bool)   ## 逆时针方向
   def on_chkBoxPolar_direction_clicked(self,checked):
      pass


   @pyqtSlot(bool)   ## 显示网格
   def on_chkBoxPolar_gridOn_clicked(self,checked):
      pass


   @pyqtSlot(int)    ## 角度偏移量
   def on_spinPolar_offset_valueChanged(self,arg1):
      pass

      
   @pyqtSlot()   ## 紧凑布局
   def on_btnPolar_tightLayout_clicked(self):
      pass


   @pyqtSlot()   ## 旋转
   def on_btnPolar_rotate_clicked(self):
      pass


##  ============窗体测试程序 ================================
if  __name__ == "__main__":        #用于当前窗体测试
   app = QApplication(sys.argv)    #创建GUI应用程序
   form=QmyMainWindow()            #创建窗体
   form.showMaximized()            #最大化显示窗体
   # form.show()
   sys.exit(app.exec_())
