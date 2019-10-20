# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/nraikman2022/PycharmProjects/ProtechGunDefense/ProtechDashboard.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import threading
import random
import serial
import time  # imports time library
# Get values from server and change the below

r = requests.get("http://34.201.116.202/checkStatus")
schoolName = "Sharon High School"
danger = False
aggressorFound = False
disabled = False
officerLastName = "HI"
officerFirstName = ""


class Ui_MainWindow(object):
    i = 1500

    def setupUi(self, MainWindow):
        QtWidgets.QApplication.processEvents()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(742, 525)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titleFrame = QtWidgets.QFrame(self.centralwidget)
        self.titleFrame.setGeometry(QtCore.QRect(0, 0, 741, 51))
        self.titleFrame.setStyleSheet("background-color: rgb(141, 148, 208)")
        self.titleFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.titleFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.titleFrame.setObjectName("titleFrame")
        self.protech = QtWidgets.QLabel(self.titleFrame)
        self.protech.setGeometry(QtCore.QRect(10, 10, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Avenir Next Condensed")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.protech.setFont(font)
        self.protech.setStyleSheet("color: rgb(238, 254, 230);")
        self.protech.setObjectName("protech")
        self.schoolName = QtWidgets.QLabel(self.titleFrame)
        self.schoolName.setGeometry(QtCore.QRect(380, 10, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Avenir Next")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.schoolName.setFont(font)
        self.schoolName.setStyleSheet("\n"
"color: rgb(237, 255, 233);")
        self.schoolName.setObjectName("schoolName")
        self.dangerFrame = QtWidgets.QFrame(self.centralwidget)
        self.dangerFrame.setGeometry(QtCore.QRect(10, 70, 151, 151))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.dangerFrame.setFont(font)
        self.dangerFrame.setStyleSheet("  border-style: solid;\n"
"  border-width: 2px;\n"
"")
        self.dangerFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dangerFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dangerFrame.setLineWidth(4)
        self.dangerFrame.setMidLineWidth(0)
        self.dangerFrame.setObjectName("dangerFrame")
        self.danger = QtWidgets.QLabel(self.dangerFrame)
        self.danger.setGeometry(QtCore.QRect(0, 10, 150, 130))
        self.danger.setStyleSheet("border-width: 0px;")
        self.danger.setObjectName("danger")
        self.safe = QtWidgets.QLabel(self.dangerFrame)
        self.safe.setGeometry(QtCore.QRect(10, 10, 131, 131))
        self.safe.setStyleSheet("border: 0px;")
        self.safe.setObjectName("safe")

        self.aggressorsFound = QtWidgets.QLabel(self.centralwidget)
        self.noAggressors = QtWidgets.QLabel(self.centralwidget)
        self.aggressorsFound.setGeometry(QtCore.QRect(210, 100, 451, 81))
        self.aggressorsFound.setObjectName("aggressorsFound")
        self.noAggressors.setGeometry(QtCore.QRect(210, 100, 451, 81))
        self.noAggressors.setObjectName("noAggressors")

        self.notDisabled = QtWidgets.QLabel(self.centralwidget)
        self.disabled = QtWidgets.QLabel(self.centralwidget)
        self.notDisabled.setGeometry(QtCore.QRect(320, 190, 241, 31))
        self.notDisabled.setObjectName("notDisabled")
        self.disabled.setGeometry(QtCore.QRect(320, 190, 241, 31))
        self.disabled.setObjectName("disabled")

        self.safteyOfficerFrame = QtWidgets.QFrame(self.centralwidget)
        self.safteyOfficerFrame.setGeometry(QtCore.QRect(0, 250, 741, 231))
        self.safteyOfficerFrame.setStyleSheet("border-style: solid;\n"
"border-width: 4px;")
        self.safteyOfficerFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.safteyOfficerFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.safteyOfficerFrame.setObjectName("safteyOfficerFrame")
        self.officerImage = QtWidgets.QLabel(self.safteyOfficerFrame)
        self.officerImage.setGeometry(QtCore.QRect(20, 30, 171, 171))
        font = QtGui.QFont()
        font.setPointSize(23)
        self.officerImage.setFont(font)
        self.officerImage.setStyleSheet("border-width: 0px;")
        self.officerImage.setObjectName("officerImage")
        self.officerDescription = QtWidgets.QLabel(self.safteyOfficerFrame)
        self.officerDescription.setGeometry(QtCore.QRect(220, 20, 161, 191))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.officerDescription.setFont(font)
        self.officerDescription.setStyleSheet("border-width: 0px;")
        self.officerDescription.setObjectName("officerDescription")
        self.frame = QtWidgets.QFrame(self.safteyOfficerFrame)
        self.frame.setGeometry(QtCore.QRect(450, 10, 261, 211))
        self.frame.setStyleSheet("border-width: 0px;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.floorMap = QtWidgets.QLabel(self.frame)
        self.floorMap.setGeometry(QtCore.QRect(-120, -320, 381, 541))
        self.floorMap.setObjectName("floorMap")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 742, 22))
        self.menubar.setObjectName("menubar")
        self.ProtechWindow = QtWidgets.QMenu(self.menubar)
        self.ProtechWindow.setObjectName("ProtechWindow")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.ProtechWindow.menuAction())
        QtWidgets.QApplication.processEvents()
        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def crap(self):
        print("crap" + str(random.randint(0, 100)))
        self.retranslateUi(MainWindow)
        self.i += 1000
        sys.setrecursionlimit(self.i)

    def retranslateUi(self, MainWindow):
        self.i += 1
        if self.i % 20 == 0:
            self.crap()
        QtWidgets.QApplication.processEvents()

        ser = serial.Serial("/dev/ttyACM0", 115200)
        rl = ser.readline()

        d = requests.get("http://34.201.116.202/checkStatus")
        if rl == 1:
            self.officerImage.show()
            officerLastName = "Barkingson"
            officerFirstName = "Mr. George"
        else:
            self.officerImage.hide()
            officerLastName = ""
            officerFirstName = ""
        if d.text != "False":
            danger = True
            aggressorFound = True
            disabled = False

            self.noAggressors.hide()
            self.aggressorsFound.show()
            self.danger.show()
            self.safe.hide()

        else:
            danger = False
            # print("sad gal")
            aggressorFound = False
            disabled = False

            self.noAggressors.show()
            self.aggressorsFound.hide()
            self.danger.hide()
            self.safe.show()

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.protech.setText(_translate("MainWindow", "Protech"))
        self.schoolName.setText(_translate("MainWindow", schoolName))
        self.schoolName.adjustSize()
        if danger:
            self.danger.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/underDanger/1200px-Achtung.svg.png\" height=\"130\"></p></body></html>"))
        else:
            self.safe.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/safe/1-14062_green-check-png-green-circle-check-mark.png\" width=\"130\"/></p></body></html>"))

        if aggressorFound:
            self.aggressorsFound.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:64pt; color:#9b0002;\">Aggressors Found</span></p></body></html>"))
        else:
            self.noAggressors.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:64pt; color:#009b08;\">No Aggressors</span></p></body></html>"))

        if not disabled:
            self.notDisabled.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#009b44;\">System is enabled</span></p></body></html>"))
        else:
            self.disabled.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#9b0000;\">System is disabled</span></p></body></html>"))
        if officerFirstName != "":
            self.officerImage.setText(_translate("MainWindow",
                                                 "<html><head/><body><p><img src=\":/Mr. George Barkingson/george.jpg\" width=\"300\"/></p></body></html>"))
            self.officerDescription.setText(_translate("MainWindow", f"<html><head/><body><p>Name: {officerFirstName}</p> <p>{officerLastName}</p></body></html>"))
            self.officerDescription.adjustSize()
        else:
            self.officerDescription.setText(_translate("MainWindow", "<html><head/><body><p>No</p> <p>Resource</p><p>Officer</p><p>Avaliable</p></body></html>"))
            self.officerDescription.adjustSize()
        self.floorMap.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/floor/floorxs.png\" width=\"100px\"/></p></body></html>"))
        self.ProtechWindow.setTitle(_translate("MainWindow", "NoAggressor"))
        QtWidgets.QApplication.processEvents()
        MainWindow.show()
        self.timer = QtCore.QTimer.singleShot(0, self.retranslateUi(MainWindow))





import Protech_rc
import ResourceOfficerImages_rc

if __name__ == "__main__":
    import sys
    import requests

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())


