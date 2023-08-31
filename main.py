import cv2
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QDialog,QLabel
from mainwindow import Ui_MainWindow
from manual import Ui_Dialog
from auto import Ui_Dialog2
import serial

import time
ser = serial.Serial("COM3",9600,timeout=1)

class main_window(QMainWindow):#class of main window to take objects from it
    def __init__(self):
       super().__init__()
       self.ui= Ui_MainWindow() #take object from mainwindow.py
       self.ui.setupUi(self)
       self.setWindowTitle('GUI_TEAM5')
       self.ui.ManualMotion.clicked.connect(self.openManualMode)
       self.ui.AutonomousMotion.clicked.connect(self.openautoMode)
    def openManualMode(self):#Showing the Manual motion Window
       man=manual()
       man.show()
       #ser.write(b'm')
       man.exec_()
    def openautoMode(self):#Showing the Autonomous motion Window
       Auto=auto()
       Auto.show()
       Auto.exec_()

class manual(QDialog):
    def __init__(self):
        super().__init__()
        self.win=Ui_Dialog()
        self.win.setupUi(self)
        self.setWindowTitle('Manual Motion')
        self.win.Forward.pressed.connect(self.Forward)
        self.win.Forward.released.connect(self.Stop)
        self.win.Backward.pressed.connect(self.Backward)
        self.win.Backward.released.connect(self.Stop)
        self.win.Left.pressed.connect(self.Left)
        self.win.Left.released.connect(self.Stop)
        self.win.Rigth.pressed.connect(self.Right)
        self.win.Rigth.released.connect(self.Stop)
        self.label = QLabel("0")
        self.win.SpeedSlider.valueChanged.connect(self.speedChange)

    def Forward(self):
        #ser.write(b'f')
        print("odam")
    def Backward(self):
        print("wraa")
       # ser.write(b'b')
    def Left(self):
        print('shemaal')
       # ser.write(b'l')
    def Right(self):
        print("ymeen")
       # ser.write(b'r')
    def Stop(self):
        #ser.write(b's')
        print("w2f")
    def speedChange(self,value):
        #self.label.setText(str(value))
        print(value)
       # ser.write(value)

        #ser.write(b'')
class auto(QDialog):
    def __init__(self):
         super().__init__()
         self.winAuto = Ui_Dialog2()
         self.winAuto.setupUi(self)
         self.setWindowTitle('Autonomous Motion')
         self.winAuto.lineEdit.returnPressed.connect(self.UltrasonicRead)
         self.winAuto.lineEdit.returnPressed.connect(self.CurrentSensorRead)
         self.winAuto.lineEdit.returnPressed.connect(self.VoltageSensorRead)
         self.winAuto.lineEdit.returnPressed.connect(self.MotionState)
         self.winAuto.SpeedSliderAuto.valueChanged.connect(self.speedChange)
    def UltrasonicRead(self):
        self.winAuto.UltrasonicRead_label.setText(self.winAuto.lineEdit.text())#will be change when i connect bluetooth
        #ser.read()
    def CurrentSensorRead(self):
        self.winAuto.CurrentsensorRead.setText(self.winAuto.lineEdit.text())#will be change when i connect bluetooth
        #ser.read()
    def VoltageSensorRead(self):
        self.winAuto.voltagesensorRead.setText(self.winAuto.lineEdit.text())#will be change when i connect bluetooth
        #ser.read()
    def MotionState(self):
        self.winAuto.MotionStateNow.setText(self.winAuto.lineEdit.text())#will be change when i connect bluetooth
        #ser.read()
    def speedChange(self,value):
        #self.label.setText(str(value))
        print(value)
       # ser.write(value)
if __name__ == "__main__":
    import sys
    app = QApplication([])
    MainWindow = main_window()
    Manual=manual()
    MainWindow.show()
    sys.exit(app.exec_())