import winreg
import sys
from ddootui import *
from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    status2 = ()
    status3 = ()
    status4 = ()

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

    def checkStatus(self):
        access_registry = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
        access_key = winreg.OpenKeyEx(access_registry, r"SYSTEM\CurrentControlSet\Services\UsoSvc",0,winreg.KEY_READ)
        usosvcStatus = winreg.QueryValueEx(access_key, "Start")
        access_key = winreg.OpenKeyEx(access_registry, r"SYSTEM\CurrentControlSet\Services\WaasMedicSVC",0,winreg.KEY_READ)
        waasMedicServiceStatus = winreg.QueryValueEx(access_key, "Start")
        access_key = winreg.OpenKeyEx(access_registry, r"SYSTEM\CurrentControlSet\Services\DoSvc",0,winreg.KEY_READ)
        deliveryOptimizationStatus = winreg.QueryValueEx(access_key, "Start")
        if deliveryOptimizationStatus == (4, 4):
            MainWindow.checkStatus.status2 = "Off"
            MainWindow.status2 = "Off"
        else:
            MainWindow.checkStatus.status2 = "On"
            MainWindow.status2 = "On"
        if waasMedicServiceStatus == (4, 4):
            MainWindow.checkStatus.status3 = "Off"
            MainWindow.status3 = "Off"
        else:
            MainWindow.checkStatus.status3 = "On"
            MainWindow.status3 = "On"
        if usosvcStatus  == (4, 4):
            MainWindow.checkStatus.status4 = "Off"
            MainWindow.status4 = "Off"
        else:
            MainWindow.checkStatus.status4 = "On"
            MainWindow.status4 = "On"

    def updateStatus(self):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", f"{MainWindow.status2}"))
        self.label_5.setText(_translate("MainWindow", f"{MainWindow.status3}"))
        self.label_6.setText(_translate("MainWindow", f"{MainWindow.status4}"))
  

    def enableUsoSvc(self):
        access_registry = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
        access_key = winreg.OpenKeyEx(access_registry, r"SYSTEM\CurrentControlSet\Services\UsoSvc",0,winreg.KEY_WRITE)
        edit_key = winreg.SetValueEx(access_key, "Start", 0, winreg.REG_DWORD, 2)
        self.checkStatus()
        self.updateStatus()  

    def disableUsoSvc(self):
        access_registry = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
        access_key = winreg.OpenKeyEx(access_registry, r"SYSTEM\CurrentControlSet\Services\UsoSvc", 0,winreg.KEY_WRITE)
        edit_key = winreg.SetValueEx(access_key, "Start", 0, winreg.REG_DWORD, 4)
        self.checkStatus()
        self.updateStatus()  
        

    def enableWaasMedicService(self):
        access_registry = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
        access_key = winreg.OpenKeyEx(access_registry, r"SYSTEM\CurrentControlSet\Services\WaasMedicSVC",0,winreg.KEY_WRITE)
        edit_key = winreg.SetValueEx(access_key, "Start", 0, winreg.REG_DWORD, 2)
        self.checkStatus()
        self.updateStatus()  

    def disableWaasMedicService(self):
        access_registry = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
        access_key = winreg.OpenKeyEx(access_registry, r"SYSTEM\CurrentControlSet\Services\WaasMedicSVC",0,winreg.KEY_WRITE)
        edit_key = winreg.SetValueEx(access_key, "Start", 0, winreg.REG_DWORD, 4)
        self.checkStatus()
        self.updateStatus()  

    def enableDeliveryOptimization(self):
        access_registry = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
        access_key = winreg.OpenKeyEx(access_registry, r"SYSTEM\CurrentControlSet\Services\DoSvc",0,winreg.KEY_WRITE)
        edit_key = winreg.SetValueEx(access_key, "Start", 0, winreg.REG_DWORD, 2)
        self.checkStatus()
        self.updateStatus()

    def disableDeliveryOptimization(self):
        access_registry = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
        access_key = winreg.OpenKeyEx(access_registry, r"SYSTEM\CurrentControlSet\Services\DoSvc",0,winreg.KEY_WRITE)
        edit_key = winreg.SetValueEx(access_key, "Start", 0, winreg.REG_DWORD, 4)
        self.checkStatus()
        self.updateStatus()

    def disableAll(self):
        self.disableDeliveryOptimization()
        self.disableUsoSvc()
        self.disableWaasMedicService()
    def enableAll(self):
        self.enableDeliveryOptimization()
        self.enableUsoSvc()
        self.enableWaasMedicService()

app = QtWidgets.QApplication(sys.argv)

MainWindow.checkStatus(self=0)

window = MainWindow()
window.show()
app.exec()