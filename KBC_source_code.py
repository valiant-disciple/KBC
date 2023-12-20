# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 21:24:53 2023

@author: Asus
"""

#Importing Required Modules
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import random

#Setting up Global Variables
f1=open("KBC.txt","r") #txt file is used to store the questions
L=f1.readlines()
random.shuffle(L) #Shuffles order of questions
Correct=""
linenum=0 #This variable helps update the question
score=0 
scorelabels=[] #This variable helps the dynamic scoreboard to function

#Main class that handles all the functionalities
class Ui_Play_KBC(object):

#Self - object that act as instance of our class
#setupUi() sets up our user Interface
    def setupUi(self, Play_KBC):        
        Play_KBC.setObjectName("Play_KBC")
        Play_KBC.resize(800, 408)
        Play_KBC.setStyleSheet("background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.505682, radius:0.706, fx:0.5, fy:0.5, stop:0 rgba(33, 160, 194, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(Play_KBC)
        self.centralwidget.setObjectName("centralwidget")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(160, 10, 451, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setStyleSheet("background-color:rgb(0, 255, 255)")
        self.label1.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.935, fx:0.528, fy:0.455, stop:0 rgba(239, 219, 58, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 140, 681, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("\n"
"background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.505682, radius:0.706, fx:0.5, fy:0.5, stop:0 rgba(204, 166, 208, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 290, 681, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("\n"
"background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.505682, radius:0.706, fx:0.5, fy:0.5, stop:0 rgba(204, 166, 208, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 200, 681, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("\n"
"background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.505682, radius:0.706, fx:0.5, fy:0.5, stop:0 rgba(204, 166, 208, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(50, 260, 681, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("\n"
"background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.505682, radius:0.706, fx:0.5, fy:0.5, stop:0 rgba(204, 166, 208, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(50, 230, 681, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("\n"
"background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.505682, radius:0.706, fx:0.5, fy:0.5, stop:0 rgba(204, 166, 208, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(50, 170, 681, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("\n"
"background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.505682, radius:0.706, fx:0.5, fy:0.5, stop:0 rgba(204, 166, 208, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_10.setObjectName("label_10")
        self.okButton = QtWidgets.QPushButton(self.centralwidget)
        self.okButton.setGeometry(QtCore.QRect(650, 320, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.okButton.setFont(font)
        self.okButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(107, 255, 90);")
        self.okButton.setObjectName("pushButton")
        self.okButton.clicked.connect(self.OkButton_Clicked)
        
        Play_KBC.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Play_KBC)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Play_KBC.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Play_KBC)
        self.statusbar.setObjectName("statusbar")
        Play_KBC.setStatusBar(self.statusbar)

        self.option_A = QtWidgets.QPushButton(self.centralwidget)
        self.option_A.setGeometry(QtCore.QRect(50, 270, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.option_A.setFont(font)
        self.option_A.setStyleSheet("background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.935, fx:0.528, fy:0.455, stop:0 rgba(239, 234, 58, 255), stop:1 rgba(255, 255, 255, 255));")
        self.option_A.setText("")
        self.option_A.setObjectName("option_A")
        self.option_A.setEnabled(False)
        self.option_A.hide()
        self.option_A.clicked.connect(self.Option_A_Clicked)
              
        self.option_B = QtWidgets.QPushButton(self.centralwidget)
        self.option_B.setGeometry(QtCore.QRect(350, 270, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.option_B.setFont(font)
        self.option_B.setStyleSheet("background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.935, fx:0.528, fy:0.455, stop:0 rgba(239, 234, 58, 255), stop:1 rgba(255, 255, 255, 255));")
        self.option_B.setText("")
        self.option_B.setObjectName("optionB")
        self.option_B.setEnabled(False)
        self.option_B.hide()
        self.option_B.clicked.connect(self.Option_B_Clicked)
        
        
        self.option_C = QtWidgets.QPushButton(self.centralwidget)
        self.option_C.setGeometry(QtCore.QRect(50, 340, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.option_C.setFont(font)
        self.option_C.setStyleSheet("background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.935, fx:0.528, fy:0.455, stop:0 rgba(239, 234, 58, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.option_C.setText("")
        self.option_C.setObjectName("option_C")
        self.option_C.setEnabled(False)
        self.option_C.hide()
        self.option_C.clicked.connect(self.Option_C_Clicked)
        
        self.option_D = QtWidgets.QPushButton(self.centralwidget)
        self.option_D.setGeometry(QtCore.QRect(350, 340, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.option_D.setFont(font)
        self.option_D.setStyleSheet("background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.935, fx:0.528, fy:0.455, stop:0 rgba(239, 234, 58, 255), stop:1 rgba(255, 255, 255, 255));")
        self.option_D.setText("")
        self.option_D.setObjectName("option_D")
        self.option_D.setEnabled(False)
        self.option_D.hide()
        self.option_D.clicked.connect(self.Option_D_Clicked)
        
        self.question = QtWidgets.QLabel(self.centralwidget)
        self.question.setGeometry(QtCore.QRect(40, 110, 521, 131))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.question.setFont(font)
        self.question.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.question.setObjectName("question")
        
        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setGeometry(QtCore.QRect(260, 390, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.next.setFont(font)
        self.next.setStyleSheet("background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.935, fx:0.528, fy:0.455, stop:0 rgba(137, 239, 58, 255), stop:1 rgba(255, 255, 255, 255));")
        self.next.setObjectName("next")
        self.next.setEnabled(False)
        self.next.hide()
        self.next.clicked.connect(self.Next_Clicked)
        
        self.score12 = QtWidgets.QLabel(self.centralwidget)
        self.score12.setGeometry(QtCore.QRect(710, 120, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.score12.setFont(font)
        self.score12.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.7, fx:0.528, fy:0.455, stop:0 rgba(239, 196, 58, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.score12.setScaledContents(False)
        self.score12.setObjectName("score12")
        self.score11 = QtWidgets.QLabel(self.centralwidget)
        self.score11.setGeometry(QtCore.QRect(710, 150, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.score11.setFont(font)
        self.score11.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.7, fx:0.528, fy:0.455, stop:0 rgba(239, 196, 58, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"")
        self.score11.setScaledContents(False)
        self.score11.setObjectName("score11")
        self.score10 = QtWidgets.QLabel(self.centralwidget)
        self.score10.setGeometry(QtCore.QRect(710, 180, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.score10.setFont(font)
        self.score10.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.7, fx:0.528, fy:0.455, stop:0 rgba(239, 196, 58, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.score10.setScaledContents(False)
        self.score10.setObjectName("score10")
        self.score9 = QtWidgets.QLabel(self.centralwidget)
        self.score9.setGeometry(QtCore.QRect(710, 210, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.score9.setFont(font)
        self.score9.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.7, fx:0.528, fy:0.455, stop:0 rgba(239, 196, 58, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.score9.setScaledContents(False)
        self.score9.setObjectName("score9")
        self.score8 = QtWidgets.QLabel(self.centralwidget)
        self.score8.setGeometry(QtCore.QRect(710, 240, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.score8.setFont(font)
        self.score8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.7, fx:0.528, fy:0.455, stop:0 rgba(239, 196, 58, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.score8.setScaledContents(False)
        self.score8.setObjectName("score8")
        self.score7 = QtWidgets.QLabel(self.centralwidget)
        self.score7.setGeometry(QtCore.QRect(710, 270, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.score7.setFont(font)
        self.score7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.7, fx:0.528, fy:0.455, stop:0 rgba(239, 196, 58, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"")
        self.score7.setScaledContents(False)
        self.score7.setObjectName("score7")
        self.score6 = QtWidgets.QLabel(self.centralwidget)
        self.score6.setGeometry(QtCore.QRect(710, 300, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.score6.setFont(font)
        self.score6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.7, fx:0.528, fy:0.455, stop:0 rgba(239, 196, 58, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.score6.setScaledContents(False)
        self.score6.setObjectName("score6")
        self.score5 = QtWidgets.QLabel(self.centralwidget)
        self.score5.setGeometry(QtCore.QRect(710, 330, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.score5.setFont(font)
        self.score5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.7, fx:0.528, fy:0.455, stop:0 rgba(239, 196, 58, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.score5.setScaledContents(False)
        self.score5.setObjectName("score5")
        self.score4 = QtWidgets.QLabel(self.centralwidget)
        self.score4.setGeometry(QtCore.QRect(710, 360, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.score4.setFont(font)
        self.score4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.7, fx:0.528, fy:0.455, stop:0 rgba(239, 196, 58, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.score4.setScaledContents(False)
        self.score4.setObjectName("score4")
        self.score3 = QtWidgets.QLabel(self.centralwidget)
        self.score3.setGeometry(QtCore.QRect(710, 390, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.score3.setFont(font)
        self.score3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.7, fx:0.528, fy:0.455, stop:0 rgba(239, 196, 58, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.score3.setScaledContents(False)
        self.score3.setObjectName("score3")
        self.score2 = QtWidgets.QLabel(self.centralwidget)
        self.score2.setGeometry(QtCore.QRect(710, 420, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.score2.setFont(font)
        self.score2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.7, fx:0.528, fy:0.455, stop:0 rgba(239, 196, 58, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.score2.setScaledContents(False)
        self.score2.setObjectName("score2")
        self.score1 = QtWidgets.QLabel(self.centralwidget)
        self.score1.setGeometry(QtCore.QRect(710, 450, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.score1.setFont(font)
        self.score1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.7, fx:0.528, fy:0.455, stop:0 rgba(239, 196, 58, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.score1.setScaledContents(False)
        self.score1.setObjectName("score1")
        self.score = QtWidgets.QLabel(self.centralwidget)
        self.score.setGeometry(QtCore.QRect(710, 80, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.score.setFont(font)
        self.score.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.7, fx:0.528, fy:0.455, stop:0 rgba(239, 196, 58, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"")
        self.score.setScaledContents(False)
        self.score.setObjectName("score")
        
        self.quit = QtWidgets.QPushButton(self.centralwidget)
        self.quit.setGeometry(QtCore.QRect(260, 430, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.quit.setFont(font)
        self.quit.setStyleSheet("background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.935, fx:0.528, fy:0.455, stop:0 rgba(137, 239, 58, 255), stop:1 rgba(255, 255, 255, 255));")
        self.quit.setObjectName("quit")
        
        self.quit.setEnabled(False)
        self.quit.hide()
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 951, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:rgb(0, 255, 255)")
        self.label.setObjectName("label")
        Play_KBC.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Play_KBC)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 978, 21))
        self.menubar.setObjectName("menubar")
        Play_KBC.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Play_KBC)
        self.statusbar.setObjectName("statusbar")
        Play_KBC.setStatusBar(self.statusbar)
        
        self.score.hide()
        self.score1.hide()
        self.score2.hide()
        self.score3.hide()
        self.score4.hide()
        self.score5.hide()
        self.score6.hide()
        self.score7.hide()
        self.score8.hide()
        self.score9.hide()
        self.score10.hide()
        self.score11.hide()
        self.score12.hide()
        self.question.hide()
        self.label.hide()
        
        #Scorelabels update to give our dynamic scoreboard
        global scorelabels
        scorelabels=[self.score1,self.score2,self.score3,self.score4,self.score5,self.score6,self.score7,self.score8,self.score9,self.score10,self.score11,self.score12]

        self.retranslateUi(Play_KBC)
        QtCore.QMetaObject.connectSlotsByName(Play_KBC)    
        
    #This function sets up all the texts visible to user
    def retranslateUi(self, Play_KBC):
        _translate = QtCore.QCoreApplication.translate
        
        Play_KBC.setWindowTitle(_translate("Play_KBC", "Play_KBC"))
        self.label1.setText(_translate("Play_KBC", "KAUN BANEGA pointCROREPATI"))
        self.label_2.setText(_translate("Play_KBC", "RULES :"))
        self.label_3.setText(_translate("Play_KBC", "1) This game comprises of a maximum of 12 Questions. Each correct question increases your final points. "))
        self.label_6.setText(_translate("Play_KBC", "6) Good Luck and Enjoy !!"))
        self.label_7.setText(_translate("Play_KBC", "3) A player can quit at any point in the game. Player will recieve the points of the last correct question as the final points."))
        self.label_8.setText(_translate("Play_KBC", "5) The Correct Question column at the right side of the screen tells the amount of points the current question will give."))
        self.label_9.setText(_translate("Play_KBC", "4) Press next to go to the next question / final reward."))
        self.label_10.setText(_translate("Play_KBC", "2) The player has only one chance for each question--- getting a question wrong will directly eliminate the player."))
        self.okButton.setText(_translate("Play_KBC", "OK"))
    
        Play_KBC.setWindowTitle(_translate("Play_KBC", "Play_KBC"))
        self.score12.setText(_translate("Play_KBC", "7 Crore Points"))
        self.score11.setText(_translate("Play_KBC", "5 Crore Points"))
        self.score10.setText(_translate("Play_KBC", "1 Crore Points"))
        self.score9.setText(_translate("Play_KBC", "50,00,000 Points"))
        self.score8.setText(_translate("Play_KBC", "25,00,000 Points"))
        self.score7.setText(_translate("Play_KBC", "12,00,000 Points"))
        self.score6.setText(_translate("Play_KBC", "6,40,000 Points"))
        self.score5.setText(_translate("Play_KBC", "3,20,000 Points "))
        self.score4.setText(_translate("Play_KBC", "1,60,000 Points"))
        self.score3.setText(_translate("Play_KBC", "50,000 Points"))
        self.score2.setText(_translate("Play_KBC", "20,000 Points"))
        self.score1.setText(_translate("Play_KBC", "10,000 Points"))
        self.score.setText(_translate("Play_KBC", "Current Question"))
        self.next.setText(_translate("Play_KBC", "Next"))
        self.quit.setText(_translate("Play_KBC", "Quit"))
        self.label.setText(_translate("Play_KBC", "KAUN BANEGA pointCROREPATI"))
        
    #The following functions are to setup the functionality of each button
    #Message Boxes are setup to show final result.
    def Option_A_Clicked(self):
        global Correct,linenum,score,scorelabels
        if self.option_A.text()==Correct:
            self.option_A.setStyleSheet("background-color : green")
            self.option_A.setEnabled(False)
            self.option_B.setEnabled(False)
            self.option_C.setEnabled(False)
            self.option_D.setEnabled(False)
            self.next.setEnabled(True)
            linenum=linenum+1
            score=score+1            
            
        else:
            Play_KBC.close()
            finalmsg= QMessageBox()
        
            Play_KBC.close()
           
            finalmsg.setWindowTitle("Game Over!")
            finalmsg.setText("Better Luck Next Time!")
            correctdisplay="Correct Answer: "+Correct
            finalmsg.setInformativeText(correctdisplay)
            finalmsg.setIcon(QMessageBox.Critical)
            finalmsg.setStandardButtons(QMessageBox.Ok)
            finalmsg.setDefaultButton(QMessageBox.Ok)
                
            x=finalmsg.exec_()
                           
    def Option_B_Clicked(self):
        global Correct,linenum,score,scorelabels
        if self.option_B.text()==Correct:
            self.option_B.setStyleSheet("background-color : green")
            self.option_A.setEnabled(False)
            self.option_B.setEnabled(False)
            self.option_C.setEnabled(False)
            self.option_D.setEnabled(False)
            self.next.setEnabled(True)
                
            linenum=linenum+1 
            score=score+1
                
        else:
            Play_KBC.close()
            finalmsg= QMessageBox()
        
            Play_KBC.close()
         
            finalmsg.setWindowTitle("Game Over!")
            finalmsg.setText("Better Luck Next Time!")
            correctdisplay="Correct Answer: "+Correct
            finalmsg.setInformativeText(correctdisplay)
            finalmsg.setIcon(QMessageBox.Critical)
            finalmsg.setStandardButtons(QMessageBox.Ok)
            finalmsg.setDefaultButton(QMessageBox.Ok)
                
            x=finalmsg.exec_()
                
                
    def Option_C_Clicked(self):
        global Correct,linenum,score,scorelabels
        if self.option_C.text()==Correct:
            self.option_C.setStyleSheet("background-color : green")
            self.option_A.setEnabled(False)
            self.option_B.setEnabled(False)
            self.option_C.setEnabled(False)
            self.option_D.setEnabled(False)
            self.next.setEnabled(True)
            
            score=score+1
            linenum=linenum+1
                
        else:
            Play_KBC.close()
            finalmsg= QMessageBox()
        
            Play_KBC.close()
           
            finalmsg.setWindowTitle("Game Over!")
            finalmsg.setText("Better Luck Next Time!")
            correctdisplay="Correct Answer: "+Correct
            finalmsg.setInformativeText(correctdisplay)
            finalmsg.setIcon(QMessageBox.Critical)
            finalmsg.setStandardButtons(QMessageBox.Ok)
            finalmsg.setDefaultButton(QMessageBox.Ok)
                
            x=finalmsg.exec_()
                
                
    def Option_D_Clicked(self):
        global Correct,linenum,score,scorelabels
        
        if self.option_D.text()==Correct:
            self.option_D.setStyleSheet("background-color : green")
            self.option_B.setEnabled(False)
            self.option_D.setEnabled(False)
            self.option_C.setEnabled(False)
            self.option_A.setEnabled(False)
            self.next.setEnabled(True)
                
            linenum=linenum+1
            score=score+1
                
        else:
            Play_KBC.close()
            finalmsg= QMessageBox()
        
            Play_KBC.close()
          
            finalmsg.setWindowTitle("Game Over!")
            finalmsg.setText("Better Luck Next Time!")
            correctdisplay="Correct Answer: "+Correct
            finalmsg.setInformativeText(correctdisplay)
            finalmsg.setIcon(QMessageBox.Critical)
            finalmsg.setStandardButtons(QMessageBox.Ok)
            finalmsg.setDefaultButton(QMessageBox.Ok)
                
            x=finalmsg.exec_()               
    
    def Next_Clicked(self):
        global Correct,score
        if score<12:
            self.option_A.setEnabled(True)
            self.option_B.setEnabled(True)
            self.option_C.setEnabled(True)
            self.option_D.setEnabled(True)
            self.next.setEnabled(False)
            self.option_A.setStyleSheet("background-color : qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.935, fx:0.528, fy:0.455, stop:0 rgba(137, 239, 58, 255), stop:1 rgba(255, 255, 255, 255));")
            self.option_B.setStyleSheet("background-color : qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.935, fx:0.528, fy:0.455, stop:0 rgba(137, 239, 58, 255), stop:1 rgba(255, 255, 255, 255));")
            self.option_C.setStyleSheet("background-color : qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.935, fx:0.528, fy:0.455, stop:0 rgba(137, 239, 58, 255), stop:1 rgba(255, 255, 255, 255));")
            self.option_D.setStyleSheet("background-color : qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.935, fx:0.528, fy:0.455, stop:0 rgba(137, 239, 58, 255), stop:1 rgba(255, 255, 255, 255));")
            
            self.score1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
    "background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.7, fx:0.528, fy:0.455, stop:0 rgba(239, 196, 58, 255), stop:1 rgba(255, 255, 255, 255));\n"
    "")
            scorelabels[score].setStyleSheet("background-color : green")
            scorelabels[score-1].setStyleSheet("background-color: rgb(255, 255, 255);\n"
    "background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.7, fx:0.528, fy:0.455, stop:0 rgba(239, 196, 58, 255), stop:1 rgba(255, 255, 255, 255));\n"
    "")
            
            #Setting up options, randomising.
            x=L[linenum]
            line=x.split(",")
            Correct=line[1]
            self.question.setText(line[0])
            self.question.adjustSize()
            line.pop(0)
        
            random.shuffle(line)
            self.option_A.setText(line[0])
            self.option_B.setText(line[1])
            self.option_C.setText(line[2])
            self.option_D.setText(line[3])
            
        else:
            finalmsg= QMessageBox()
            Play_KBC.close()
            finalmsg.setAutoFillBackground(False)
            displaystr="GRAND WINNER!!! You won "+scorelabels[score-1].text()
            finalmsg.setStyleSheet("background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.505682, radius:0.706, fx:0.5, fy:0.5, stop:0 rgba(33, 160, 194, 255), stop:1 rgba(255, 255, 255, 255));\n" "\n"
                                   "\n"
                                   "\n"
                                   "") 
            finalmsg.setWindowTitle("Game Over!")
            finalmsg.setText(displaystr)
            finalmsg.setIcon(QMessageBox.Information)
            finalmsg.setStandardButtons(QMessageBox.Ok)
            finalmsg.setDefaultButton(QMessageBox.Ok)
            
            x=finalmsg.exec_()
        
        
    def QuitClicked(self):
        global score,scorelabels
        finalmsg= QMessageBox()
        
        if score==0:
            Play_KBC.close()
        
        else:
            Play_KBC.close()
            finalmsg.setAutoFillBackground(False)
            displaystr="Congrats! You won "+scorelabels[score-1].text()
            finalmsg.setStyleSheet("background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.505682, radius:0.706, fx:0.5, fy:0.5, stop:0 rgba(33, 160, 194, 255), stop:1 rgba(255, 255, 255, 255));\n"
    "\n"
    "\n"
    "\n"
    "")
            
            finalmsg.setWindowTitle("Game Over!")
            finalmsg.setText(displaystr)
            finalmsg.setIcon(QMessageBox.Information)
            finalmsg.setStandardButtons(QMessageBox.Ok)
            finalmsg.setDefaultButton(QMessageBox.Ok)
            
            
            x=finalmsg.exec_()
            
    #This function transitions from welcone screen to play area
    def OkButton_Clicked(self):
        self.okButton.setEnabled(False)
        self.okButton.hide()
        self.label1.hide()
        self.label_2.hide()
        self.label_3.hide()
        self.label_6.hide()
        self.label_7.hide()
        self.label_8.hide()
        self.label_9.hide()
        self.label_10.hide()
        self.score.show()
        self.score1.show()
        self.score2.show()
        self.score3.show()
        self.score4.show()
        self.score5.show()
        self.score6.show()
        self.score7.show()
        self.score8.show()
        self.score9.show()
        self.score10.show()
        self.score11.show()
        self.score12.show()
        self.question.show()
        self.label.show()
        self.option_A.setEnabled(True)
        self.option_A.show()
        self.option_B.setEnabled(True)
        self.option_B.show()
        self.option_C.setEnabled(True)
        self.option_C.show()
        self.option_D.setEnabled(True)
        self.option_D.show()
        self.next.setEnabled(True)
        self.next.show()
        self.quit.setEnabled(True)
        self.quit.show()
        self.score1.setStyleSheet("background-color : green")
        
        x=L[linenum]
        line=x.split(",")
        global Correct
        Correct=line[1]
        self.question.setText(line[0])
        self.question.adjustSize()
        line.pop(0)
        
        random.shuffle(line)
        self.option_A.setText(line[0])
        self.option_B.setText(line[1])
        self.option_C.setText(line[2])
        self.option_D.setText(line[3])
        
        self.quit.clicked.connect(self.QuitClicked)
        
        self.retranslateUi(Play_KBC)
        QtCore.QMetaObject.connectSlotsByName(Play_KBC)
        
#Statements to invoke the class Ui_Play_KBC() to start running the game window.        
import sys
app = QtWidgets.QApplication(sys.argv)
Play_KBC = QtWidgets.QMainWindow()
ui = Ui_Play_KBC()
ui.setupUi(Play_KBC)
Play_KBC.show()
sys.exit(app.exec_())
