# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculate.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import math


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 400)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 481, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.cb0 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.cb0.setObjectName("cb0")
        import sqlite3
        conn = sqlite3.connect('fantasy.db')
        self.horizontalLayout.addWidget(self.cb0)
        sql="select name from teams"
        cur=conn.execute(sql)
        teams=[]
        for row in cur:
            self.cb0.addItem(row[0])        
        conn.close()
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.cb1 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.cb1.setObjectName("cb1")
        self.cb1.addItem("")
        self.horizontalLayout.addWidget(self.cb1)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 349, 481, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton.setMinimumSize(QtCore.QSize(75, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.calculate)
        self.horizontalLayout_2.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.scoreline = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.scoreline.setObjectName("scoreline")
        self.horizontalLayout_2.addWidget(self.scoreline)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 60, 481, 61))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 120, 481, 231))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lw1 = QtWidgets.QListWidget(self.horizontalLayoutWidget_4)
        self.lw1.setEditTriggers(QtWidgets.QAbstractItemView.EditKeyPressed)
        self.lw1.setObjectName("lw1")
        self.horizontalLayout_4.addWidget(self.lw1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.lw2 = QtWidgets.QListWidget(self.horizontalLayoutWidget_4)
        self.lw2.setObjectName("lw2")
        self.horizontalLayout_4.addWidget(self.lw2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def calculate(self):
        import sqlite3
        conn = sqlite3.connect('fantasy.db')
        team=self.cb0.currentText()
        self.lw1.clear()
        sql1="select players, value from teams where name='"+team+"'"
        cur=conn.execute(sql1)
        row=cur.fetchone()
        selected=row[0].split(',')
        self.lw1.addItems(selected)
        teamttl=0
        self.lw2.clear()
        row = None;
        match=self.cb1.currentText()
        for i in range(self.lw1.count()):
            try:
                ttl, batscore, bowlscore, fieldscore=0,0,0,0
                nm=self.lw1.item(i).text()
                cursor=conn.execute("SELECT * from "+match+" where player='"+nm+"'")
                row=cursor.fetchone()
                row=list(row)
                if row != None:
                    batscore=int(row[1]/2)
                    if batscore>=50:
                        batscore+=5
                    if batscore>=100:
                        batscore+=10
                    if row[1]>0:
                        sr=row[1]/row[2]
                        if sr>=80 and sr<100:
                            batscore+=2
                        if sr>=100:
                            batscore+=4
                    batscore=batscore+row[3]
                    batscore=batscore+2*row[4]
                    bowlscore=row[8]*10
                    if row[8]>=3:
                        bowlscore=bowlscore+5
                        if row[8]>=5:
                            bowlscore=bowlscore+10
                        if row[7]>0:
                            er=6*row[7]/row[5]
                            if er<=2:
                                bowlscore=bowlscore+10
                            if er>2 and er<=3.5:
                                bowlscore=bowlscore+7
                            if er>3.5 and er<=4.5:
                                bowlscore=bowlscore+4
                    fieldscore=(row[9]+row[10]+row[11])*10            
                    ttl=batscore+bowlscore+fieldscore
                    self.lw2.addItem(str(ttl))
                    teamttl=teamttl+ttl
            except TypeError:
                break;
        self.scoreline.setText(str(teamttl))

        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Choose Team"))
        self.label_2.setText(_translate("Dialog", "Choose Match"))
        self.cb1.setItemText(0, _translate("Dialog", "match1"))
        self.pushButton.setText(_translate("Dialog", "Calculate"))
        self.label_4.setText(_translate("Dialog", "Players"))
        self.label_3.setText(_translate("Dialog", "Score"))

        self.scoreline.setText(_translate("Dialog", "00"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
