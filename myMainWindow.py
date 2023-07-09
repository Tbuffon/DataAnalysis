# -*- coding: utf-8 -*-

import sys, os, time

from PyQt5.QtWidgets import  QApplication, QMainWindow, QFileDialog

from PyQt5.QtCore import  pyqtSlot,QCoreApplication,Qt

import numpy as np

import pandas as pd

import matplotlib as mpl

import mpl_scatter_density

from scipy.signal import find_peaks

from matplotlib.colors import LinearSegmentedColormap

from ui_MainWindow import Ui_MainWindow

from myFigureCanvas import QmyFigureCanvas

class QmyMainWindow(QMainWindow): 

   def __init__(self, parent=None):
      super().__init__(parent)   #调用父类构造函数，创建窗体
      self.ui=Ui_MainWindow()    #创建UI对象
      self.ui.setupUi(self)      #构造UI界面

      self.setWindowTitle("光电数据分析软件")
      self.setCentralWidget(self.ui.centralWidget)

      self.list_t = []
      self.current = []
      self.photocurrent = []
      self.ref = []
      self.quan_conduc=7.75*1e-5
      self.labels = None
      self.conditions_filename = None
      self.data = None
      self.tdms_file_reduced = None
      self.break_data = None
      self.close_data = None
      self.BD_low_lim = -1.5
      self.BD_up_lim = 0.6
      self.BD_step = 0.01
      self.CD_low_lim = -1.5
      self.CD_up_lim = 0.6
      self.CD_step = 0.01
      # self.__drawHist()  #直方图
      pass

##  ==============自定义功能函数========================

##===========page 1 散点密度图============

   def __drawScatter(self):  ##绘制散点密度图
      white_viridis = LinearSegmentedColormap.from_list('white_viridis', [
         (0, '#ffffff'),
         (1e-20, '#440053'),
         (0.2, '#404388'),
         (0.4, '#2a788e'),
         (0.6, '#21a784'),
         (0.8, '#78d151'),
         (1, '#fde624'),
      ], N=256) # 设置颜色映射

      x=self.data['Conductance logG/G0'] 
      y=self.data['Photocurrent A']

      fig = self.ui.figScatter.figure
      fig.clear() #清空绘图区内容
      ax = fig.add_subplot(1, 1, 1, projection='scatter_density')
      density = ax.scatter_density(x, y, cmap=white_viridis)
      fig.colorbar(density, label='Number of points per pixel')
      ax.set_xlim(-1.5,1)
      density.set_clim(0, 2000)
      ax.set_xlabel('Conductance /log($G$/$G$$_0$)')
      ax.set_ylabel('I$_P$$_C$ /nA')
      ax.plot([0, 0], [0,100], 'k-', lw=2)
      fig.canvas.draw()
      pass

   def __drawScatterBreakData(self):  ##绘制break_data散点密度图
      white_viridis = LinearSegmentedColormap.from_list('white_viridis', [
         (0, '#ffffff'),
         (1e-20, '#440053'),
         (0.2, '#404388'),
         (0.4, '#2a788e'),
         (0.6, '#21a784'),
         (0.8, '#78d151'),
         (1, '#fde624'),
      ], N=256) # 设置颜色映射

      x=self.break_data['time ms']/1000
      y=self.break_data['Photocurrent A']*1e9

      fig = self.ui.figScatter.figure
      fig.clear() #清空绘图区内容
      ax = fig.add_subplot(1, 1, 1, projection='scatter_density')
      density = ax.scatter_density(x, y, cmap=white_viridis)
      fig.colorbar(density, label='Number of points per pixel')
      density.set_clim(0, 200)
      ax.set_xlabel('Time /s')
      ax.set_ylabel('I$_P$$_C$ /nA')
      fig.canvas.draw()
      pass

   def __drawScatterCloseData(self):  ##绘制close_data散点密度图
      white_viridis = LinearSegmentedColormap.from_list('white_viridis', [
         (0, '#ffffff'),
         (1e-20, '#440053'),
         (0.2, '#404388'),
         (0.4, '#2a788e'),
         (0.6, '#21a784'),
         (0.8, '#78d151'),
         (1, '#fde624'),
      ], N=256) # 设置颜色映射

      x=self.close_data['time ms']/1000
      y=self.close_data['Photocurrent A']*1e9

      fig = self.ui.figScatter.figure
      fig.clear() #清空绘图区内容
      ax = fig.add_subplot(1, 1, 1, projection='scatter_density')
      density = ax.scatter_density(x, y, cmap=white_viridis)
      fig.colorbar(density, label='Number of points per pixel')
      density.set_clim(0, 200)
      ax.set_xlabel('Time /s')
      ax.set_ylabel('I$_P$$_C$ /nA')
      fig.canvas.draw()
      pass

   def __drawCruve(self):  ##绘制曲线图
      fig = self.ui.figCurve.figure
      fig.clear() #清空绘图区内容
      for i in range(12, 22):
         single_curve=self.break_data.loc[self.break_data['Number']==i]
         ax = fig.add_subplot(2, 5, i-11)
         ax.plot(single_curve['time ms']/1000,single_curve['Conductance G/G0'],color='blue')
         ax.set_xlabel('Time s',fontsize=12)
         ax.set_ylabel('Conductance /$G$$_0$',color='blue',fontsize=12)
         ax.plot([min(single_curve['time ms']/1000), max(single_curve['time ms']/1000)], [1, 1], 'k-', lw=2)
         ax2=ax.twinx()
         ax2.plot(single_curve['time ms']/1000,single_curve['Photocurrent A']*1e9,color='red')
         ax2.set_ylabel('I$_P$$_C$ /nA',color='red',fontsize=12)
         ax.set_xlim(0, 2.500)
      fig.tight_layout()
      fig.canvas.draw()
   
   def __drawBreakDataErrorBar(self, low_lim, up_lim, step): ##绘制break_data误差棒图
      conductance_min=low_lim #conductance的范围
      conductance_max=up_lim
      binsize=step #间隔
      conductance_range=np.arange(conductance_min,conductance_max+binsize,binsize) #起始值
      conductance_range= np.round(conductance_range,3)#保留几位有效数字
      len_conduc_range=len(conductance_range)
      mean_pc,std_pc,mean_ref,std_ref,mean_diff_pc,std_diff_pc,mean_pc_i,std_pc_i,mean_ref_i,std_ref_i=[],[],[],[],[],[],[],[],[],[]

      for i in range(0,len_conduc_range-1):
         new=self.break_data[self.break_data['Conductance logG/G0'].between(conductance_range[i],conductance_range[i+1])]
         mean_pc.append(new['Photocurrent A'].mean())
         std_pc.append(new['Photocurrent A'].std())
         mean_ref.append(new['Ref A'].mean())
         std_ref.append(new['Ref A'].std())
         mean_diff_pc.append(new['Diff_Photocurrent A'].mean())
         std_diff_pc.append(new['Diff_Photocurrent A'].std())
         mean_pc_i.append(new['PC/Current'].mean())
         std_pc_i.append(new['PC/Current'].std())
         mean_ref_i.append(new['Ref/Current'].mean())
         std_ref_i.append(new['Ref/Current'].std())
      # conductance_range_2=conductance_range[:len(mean_pc)]
      # break_conductance_dataset=pd.DataFrame({'Conductance G/G0': list(conductance_range),'Mean_Photocurrent_A':list(mean_pc),'Std_Photocurrent':list(std_pc)
      #                            ,'Mean_Ref_A':list(mean_ref),'Std_Ref':list(std_ref),
      #                             'Mean_Diff_pc_A':list(mean_diff_pc),'Std_Diff_pc_A':list(std_diff_pc),
      #                             'Mean_PC/I_A':list(mean_pc_i),'Std_PC/I_A':list(std_pc_i),
      #                             'Mean_ref/I_A':list(mean_ref_i),'Std_ref/I_A':list(std_ref_i)
      #                            })
      fig = self.ui.figErrorBar.figure
      fig.clear() #清空绘图区内容
      ax = fig.add_subplot(2, 3, 1)
      ax.errorbar(conductance_range[:len(mean_pc)],mean_pc,yerr=std_pc,ecolor='red')
      ax.set_yscale('log')
      ax.set_xlabel('Conductance /$G$$_0$')
      ax.set_ylabel('Photocurrent A')

      ax = fig.add_subplot(2, 3, 2)
      ax.errorbar(conductance_range[:len(mean_pc)],mean_ref,yerr=std_ref,ecolor='red')
      ax.set_yscale('log')
      ax.set_xlabel('Conductance /$G$$_0$')
      ax.set_ylabel('Ref A')
      
      ax = fig.add_subplot(2, 3, 3)
      ax.errorbar(conductance_range[:len(mean_pc)],mean_diff_pc,yerr=std_diff_pc,ecolor='red')
      # ax.set_yscale('log')
      ax.set_xlabel('Conductance /$G$$_0$')
      ax.set_ylabel('Diff_Photocurrent A')
      
      ax = fig.add_subplot(2, 3, 4)
      ax.errorbar(conductance_range[:len(mean_pc)],mean_pc_i,yerr=std_pc_i,ecolor='red')
      # ax.set_yscale('log')
      ax.set_xlabel('Conductance /$G$$_0$')
      ax.set_ylabel('PC/Current')
      
      ax = fig.add_subplot(2, 3, 5)
      ax.errorbar(conductance_range[:len(mean_pc)],mean_ref_i,yerr=std_ref_i,ecolor='red')
      # ax.set_yscale('log')
      ax.set_xlabel('Conductance /$G$$_0$')
      ax.set_ylabel('Ref/Current')

      fig.tight_layout()
      fig.canvas.draw()
   
   def __drawCloseDataErrorBar(self, low_lim, up_lim, step): ##绘制close_data误差棒图
      conductance_min=low_lim #conductance的范围
      conductance_max=up_lim
      binsize=step #间隔
      conductance_range=np.arange(conductance_min,conductance_max+binsize,binsize) #起始值
      conductance_range= np.round(conductance_range,3)#保留几位有效数字
      len_conduc_range=len(conductance_range)
      mean_pc,std_pc,mean_ref,std_ref,mean_diff_pc,std_diff_pc,mean_pc_i,std_pc_i,mean_ref_i,std_ref_i=[],[],[],[],[],[],[],[],[],[]

      for i in range(0,len_conduc_range-1):
         new=self.close_data[self.close_data['Conductance logG/G0'].between(conductance_range[i],conductance_range[i+1])]
         mean_pc.append(new['Photocurrent A'].mean())
         std_pc.append(new['Photocurrent A'].std())
         mean_ref.append(new['Ref A'].mean())
         std_ref.append(new['Ref A'].std())
         mean_diff_pc.append(new['Diff_Photocurrent A'].mean())
         std_diff_pc.append(new['Diff_Photocurrent A'].std())
         mean_pc_i.append(new['PC/Current'].mean())
         std_pc_i.append(new['PC/Current'].std())
         mean_ref_i.append(new['Ref/Current'].mean())
         std_ref_i.append(new['Ref/Current'].std())
      # conductance_range_2=conductance_range[:len(mean_pc)]

      fig = self.ui.figErrorBar.figure
      fig.clear() #清空绘图区内容
      ax = fig.add_subplot(2, 3, 1)
      ax.errorbar(conductance_range[:len(mean_pc)],mean_pc,yerr=std_pc,ecolor='red')
      ax.set_yscale('log')
      ax.set_xlabel('Conductance /$G$$_0$')
      ax.set_ylabel('Photocurrent A')

      ax = fig.add_subplot(2, 3, 2)
      ax.errorbar(conductance_range[:len(mean_pc)],mean_ref,yerr=std_ref,ecolor='red')
      ax.set_yscale('log')
      ax.set_xlabel('Conductance /$G$$_0$')
      ax.set_ylabel('Ref A')
      
      ax = fig.add_subplot(2, 3, 3)
      ax.errorbar(conductance_range[:len(mean_pc)],mean_diff_pc,yerr=std_diff_pc,ecolor='red')
      # ax.set_yscale('log')
      ax.set_xlabel('Conductance /$G$$_0$')
      ax.set_ylabel('Diff_Photocurrent A')
      
      ax = fig.add_subplot(2, 3, 4)
      ax.errorbar(conductance_range[:len(mean_pc)],mean_pc_i,yerr=std_pc_i,ecolor='red')
      # ax.set_yscale('log')
      ax.set_xlabel('Conductance /$G$$_0$')
      ax.set_ylabel('PC/Current')
      
      ax = fig.add_subplot(2, 3, 5)
      ax.errorbar(conductance_range[:len(mean_pc)],mean_ref_i,yerr=std_ref_i,ecolor='red')
      # ax.set_yscale('log')
      ax.set_xlabel('Conductance /$G$$_0$')
      ax.set_ylabel('Ref/Current')

      fig.tight_layout()
      fig.canvas.draw()
   
   def __drawBreakDataHist(self):
      fig = self.ui.figHist.figure
      fig.clear() #清空绘图区内容
      ax = fig.add_subplot(1, 1, 1)
      ax.hist(self.break_data['Conductance G/G0'],bins=600,color='#607c8e')
      ax.grid(True)
      ax.set_xlabel('Conductance /$G$$_0$')
      fig.tight_layout()
      fig.canvas.draw()
   
   def __drawCloseDataHist(self):
      fig = self.ui.figHist.figure
      fig.clear() #清空绘图区内容
      ax = fig.add_subplot(1, 1, 1)
      ax.hist(self.close_data['Conductance G/G0'],bins=600,color='#607c8e')
      ax.grid(True)
      ax.set_xlabel('Conductance /$G$$_0$')
      fig.tight_layout()
      fig.canvas.draw()


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
   
   def __getLabels(self, filename): ##获取标签
    bias_voltage=float(filename[filename.index('Bias')+4:filename.index('mV')])/1000
    wavelength=float(filename[filename.index('Wavelength')+10:filename.index('nm')])
    pump_power=float(filename[filename.index('Power')+5:filename.index('mW')])
    freq=float(filename[filename.index('Freq')+4:filename.index('Hz')])
    labels=[bias_voltage,wavelength,pump_power,freq]
    conditions_filename='Bias'+str(labels[0])+'mV_'+'Wavelength'+str(labels[1])+'nm_'+'Power'+str(labels[2])+'mW_'+'Freq'+str(labels[3])+'Hz'
    return labels,conditions_filename

   def __ImportData(self, photocurrent_file): ##导入数据
      self.labels,self.conditions_filename=self.__getLabels(photocurrent_file[0])
      self.data=pd.DataFrame(self.list_t,columns=['Time s'])
      self.data['Photocurrent A']=pd.DataFrame(self.photocurrent)
      self.data['Current A']=pd.DataFrame(self.current)
      self.data['Ref A']=pd.DataFrame(self.ref)
      self.data['Conductance G/G0']=self.data['Current A']/(np.sqrt(2)*self.labels[0]*self.quan_conduc)
      self.data['Conductance logG/G0']=np.log10(self.data['Conductance G/G0'])
      self.data['Diff_Photocurrent A']=self.data['Photocurrent A']-self.data['Ref A']
      self.data['PC/Current']=self.data['Photocurrent A']/(self.data['Current A']/np.sqrt(2))
      self.data['Ref/Current']=self.data['Ref A']/(self.data['Current A']/np.sqrt(2))
      
   def __reduceDataPoints(self, data_pd):
      reduced_data_pd=data_pd[(self.data['Conductance G/G0']<=6.5)]
      rr_test=reduced_data_pd.reset_index(drop=True)
      return rr_test
   
   def __splitData(self):
      #find break data
      log_G=self.tdms_file_reduced['Conductance logG/G0'].values
      start, end = [], []
      cut_trigger = []
      ii = 0
      STEP = 50  #-1.2 +7
      start_all,_=find_peaks(self.tdms_file_reduced['Conductance G/G0'],height=4,distance=5000)
      point_num=len(start_all)
      log_G=self.tdms_file_reduced['Conductance logG/G0'].values
      start=start_all[0:point_num-2]
      #find break curve>-4 logG
      for i in start:
         n=0
         while True:  
            n+=1
            if np.mean(log_G[n*STEP+i:(n+1)*STEP+i])>np.mean(log_G[(n+1)*STEP+i:(n+2)*STEP+i]) and np.mean(log_G[(n+1)*STEP+i:(n+2)*STEP+i])<=-1.51:
                  end.append(n*STEP+i)
                  break
      break_dataset=[]
      curve_num=len(start)
      datalenth=[]
      for i in range(0,curve_num):
         data_mediate_forward=self.tdms_file_reduced.loc[start[i]:end[i]]
         data_mediate_forward['Number']=[i]*len(data_mediate_forward.index)
         break_dataset.append(data_mediate_forward)
         datalenth.append(end[i]-start[i]+1)
      self.break_data=pd.concat(break_dataset)
      dt=0.1
      time_list=[]
      for i in range(0,curve_num):
         time_list.extend(np.linspace(0,datalenth[i]*dt,datalenth[i]))
      self.break_data['time ms']=time_list

      #find clos curve >-4logG
      start_close=start[1::]
      end_close=[]
      STEP = 50
      for i in start_close:
         n=0
         while True:  
            n+=1
            if np.mean(log_G[i-(n+1)*STEP:i-n*STEP])>np.mean(log_G[i-(n+2)*STEP:i-(n+1)*STEP]) and np.mean(log_G[i-(n+2)*STEP:i-(n+1)*STEP])<=-1.51:
                  end_close.append(i-n*STEP)
                  break
      close_dataset=[]
      curve_num=len(start_close)
      datalenth=[]
      for i in range(0,curve_num):
         data_mediate_forward=self.tdms_file_reduced.loc[end_close[i]:start_close[i]]
         data_mediate_forward['Number']=[i]*len(data_mediate_forward.index)
         close_dataset.append(data_mediate_forward)
         datalenth.append(start_close[i]-end_close[i]+1)
      self.close_data=pd.concat(close_dataset)
      dt=0.1
      time_list=[]
      for i in range(0,curve_num):
         time_list.extend(np.linspace(0,datalenth[i]*dt,datalenth[i]))
      # self.close_data['time ms']=time_list
         
      
##  ==============event处理函数==========================


##  ==========由connectSlotsByName()自动连接的槽函数============

##===========Action对象============
   @pyqtSlot() 
   def on_actImportData_triggered(self):
      """导入数据"""
      # 找到文件夹内所有文件
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

      # 读取数据
      start_time = time.perf_counter()
      self.list_t,self.photocurrent,self.current,self.ref = self.__getAllData(photocurrent_file)
      time_used = (time.perf_counter() - start_time)
      # print("Time used: %s s" % (int(time_used)),'/n','==== Done! ====')
      str_finish = "Time used: %s s" % (int(time_used)) + '\n' + '==== Done! ===='
      self.ui.logOutputText.appendPlainText(str_finish)

      # 导入数据
      self.__ImportData(photocurrent_file)
      self.ui.logOutputText.appendPlainText("\n数据导入完成！")
      QCoreApplication.processEvents()

      # 分割数据
      start_time = time.perf_counter()
      self.ui.logOutputText.appendPlainText("\n正在分割数据，请稍候......")
      QCoreApplication.processEvents() 
      self.tdms_file_reduced=self.__reduceDataPoints(self.data)
      self.__splitData()
      time_used = (time.perf_counter() - start_time)
      str_finish = "Time used: %s s" % (int(time_used)) + '\n' + '==== Done! ===='
      self.ui.logOutputText.appendPlainText(str_finish)
      self.ui.logOutputText.appendPlainText("\n数据分割完成！")
##===========page 1 散点密度图============
   @pyqtSlot()  ##绘制All_data散点密度图
   def on_btnRun_clicked(self):
      self.__drawScatter()
      self.ui.logOutputText.appendPlainText("\n散点密度图绘制完成！")

   @pyqtSlot()  ##绘制Break_data散点密度图
   def on_btnBreakData_clicked(self):
      self.__drawScatterBreakData()
      self.ui.logOutputText.appendPlainText("Break_data散点密度图绘制完成！")
   
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


##=======page 2 曲线图=========
   @pyqtSlot()  ##绘制曲线图
   def on_btnDraw_curve_clicked(self):
      self.__drawCruve()
      self.ui.logOutputText.appendPlainText("曲线图绘制完成！")

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


##=======page 3 误差棒图=========

   @pyqtSlot()  ##绘制Break_data误差棒图
   def on_btnDraw_BDErrorBar_clicked(self):
      self.__drawBreakDataErrorBar(self.BD_low_lim, self.BD_up_lim, self.BD_step)
      self.ui.logOutputText.appendPlainText("Break_data误差棒图绘制完成！")
   
   @pyqtSlot()  ##绘制Close_data误差棒图
   def on_btnDraw_CDErrorBar_clicked(self):
      self.__drawCloseDataErrorBar(self.CD_low_lim, self.CD_up_lim, self.CD_step)
      self.ui.logOutputText.appendPlainText("Close_data误差棒图绘制完成！")
   
   @pyqtSlot(float)  ##修改break_data误差棒图的下限
   def on_dsb_BD_low_lim_valueChanged(self,value):
      self.BD_low_lim=value
   
   @pyqtSlot(float)  ##修改break_data误差棒图的上限
   def on_dsb_BD_up_lim_valueChanged(self,value):
      self.BD_up_lim=value
   
   @pyqtSlot(float)  ##修改break_data误差棒图的步长
   def on_dsb_BD_step_valueChanged(self,value):
      self.BD_step=value
   
   @pyqtSlot(float)  ##修改close_data误差棒图的下限
   def on_dsb_CD_low_lim_valueChanged(self,value):
      self.CD_low_lim=value
   
   @pyqtSlot(float)  ##修改close_data误差棒图的上限
   def on_dsb_CD_up_lim_valueChanged(self,value):
      self.CD_up_lim=value
   
   @pyqtSlot(float)  ##修改close_data误差棒图的步长
   def on_dsb_CD_step_valueChanged(self,value):
      self.CD_step=value


   @pyqtSlot()   ## 重画饼图
   def on_btnPie_redraw_clicked(self):
      pass


   @pyqtSlot()   ## 紧凑布局
   def on_btnPie_tightLayout_clicked(self):
      pass

      
   @pyqtSlot(bool)   ## 显示图例
   def on_chkBoxPie_Legend_clicked(self,checked):
      pass

      
##=====page 4 直方图==============

   @pyqtSlot()  ##绘制Break_data直方图
   def on_btn_DrawBDHist_clicked(self): 
      self.__drawBreakDataHist()
      self.ui.logOutputText.appendPlainText("Break_data直方图绘制完成！")
   
   @pyqtSlot()  ##绘制Close_data直方图
   def on_btnDraw_CDHist_clicked(self): 
      self.__drawCloseDataHist()
      self.ui.logOutputText.appendPlainText("Close_data直方图绘制完成！")


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
