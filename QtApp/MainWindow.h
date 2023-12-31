﻿#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include    <QMainWindow>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

private:

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private slots:

   void on_actTightLayout_triggered();

   void on_actSetCursor_triggered();

   void on_actScatterAgain_triggered();

   void on_gBoxHist_toolbar_clicked(bool checked);

   void on_chkBoxHist_ShowHint_clicked(bool checked);

   void on_btnHist_tightLayout_clicked();

   void on_btnHist_redraw_clicked();

   void on_btnStem_redraw_clicked();

   void on_btnStem_tightLayout_clicked();

   void on_chkBoxStem_Analog_clicked(bool checked);

   void on_chkBoxStem_Holder_clicked(bool checked);

   void on_chkBoxStem_Legend_clicked(bool checked);

   void on_btnPie_redraw_clicked();

   void on_btnPie_tightLayout_clicked();

   void on_chkBoxPie_Legend_clicked(bool checked);

   void on_radioPolar_spiral_clicked();

   void on_radioPolar_rose_clicked();

   void on_chkBoxPolar_direction_clicked(bool checked);

   void on_chkBoxPolar_gridOn_clicked(bool checked);

   void on_spinPolar_offset_valueChanged(int arg1);

   void on_btnPolar_tightLayout_clicked();

   void on_btnPolar_rotate_clicked();

   void on_radioFill_Both_clicked();

   void on_btnFill_tightLayout_clicked();

   void on_chkBoxFill_gridLine_clicked(bool checked);

   void on_chkBoxHist_Legend_clicked(bool checked);

   void on_btnPolar_redraw_clicked();

   void on_actOpenFolder_triggered();

   void on_pushButton_clicked();

   void on_btn_clicked();

   void on_btnRun_clicked();

   void on_btnBreakData_clicked();

   void on_btnCloseData_clicked();

   void on_btnDraw_curve_clicked();

   void on_doubleSpinBox_valueChanged(double arg1);

   void on_btnDraw_BDErrorBar_clicked();

   void on_btnDraw_BDErrorBar_2_clicked();

   void on_btnDraw_CDErrorBar_clicked();

   void on_btn_DrawBDHist_clicked();

   void on_btnDraw_CDHist_clicked();

   void on_dsb_BD_low_lim_valueChanged(double arg1);

   void on_dsb_BD_up_lim_valueChanged(double arg1);

   void on_dsb_BD_step_valueChanged(double arg1);

   private:
    Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H
