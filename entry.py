# importin the necessary modules
from PyQt5 import QtCore, QtGui, QtWidgets  # module for pyQt5 used for designing the window and the widgets
# num2words is used to convert numbers into word string
from num2words import *
# importing the second user interface cheque.py
from cheque import Ui_Cheque
# Random is used to get random numbers
import random
# sql database
import MySQLdb as Mdb
import mysql.connector as mc
from datetime import date


class Ui_DataEntry(object):
    def insertData(self):
        mydb = mc.connect(
            host='localhost',
            user='root',
            password='gt122LEX152',
            database='bank'
        )
        mycursor = mydb.cursor()
        firstName = self.lineEditFirstName.text()
        lastName = self.lineEditLastName.text()
        accountNumber = self.lineEditAccountNumber.text()
        amount = self.lineEditAmount.text()
        today1 = date.today()
        today = f"{today1}"

        sql = "INSERT INTO details(firstName,lastName, accountNumber, amount, date) VALUES (%s,%s,%s,%s,%s)"
        val = (firstName, lastName, accountNumber, amount, today)

        mycursor.execute(sql, val)

        mydb.commit()

    def toCheque(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Cheque()
        self.ui.setupUi(self.window)
        self.window.show()

    def record(self):
        check = random.randint(23456789, 98765432)
        checkno = f"{check}"
        firstname = self.lineEditFirstName.text()
        lastname = self.lineEditLastName.text()
        name = f"{firstname}  {lastname}"
        signature = firstname[0]
        signature2 = lastname[0]
        sign = f"{signature}.{signature2}"
        ksh = self.lineEditAmount.text()
        kesh = int(ksh)
        amountInWords = num2words(kesh)
        self.ui.lblAmountInWOrdsOut.setText(amountInWords)
        acountNo = self.lineEditAccountNumber.text()
        self.ui.lblKshOut.setText(ksh)
        self.ui.lblAcctNoOut.setText(acountNo)
        self.ui.labelPayToOut.setText(name)
        self.ui.lblChequeNoOut.setText(checkno)
        self.ui.lblSignOut.setText(sign)

    def setupUi(self, DataEntry):
        DataEntry.setObjectName("DataEntry")
        DataEntry.resize(800, 576)
        self.centralwidget = QtWidgets.QWidget(DataEntry)
        self.centralwidget.setObjectName("centralwidget")
        self.labelTitle = QtWidgets.QLabel(self.centralwidget)
        self.labelTitle.setGeometry(QtCore.QRect(270, 60, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.labelTitle.setFont(font)
        self.labelTitle.setObjectName("labelTitle")
        self.labelAccountNumber = QtWidgets.QLabel(self.centralwidget)
        self.labelAccountNumber.setGeometry(QtCore.QRect(70, 190, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelAccountNumber.setFont(font)
        self.labelAccountNumber.setObjectName("labelAccountNumber")
        self.labelFirstName = QtWidgets.QLabel(self.centralwidget)
        self.labelFirstName.setGeometry(QtCore.QRect(70, 250, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelFirstName.setFont(font)
        self.labelFirstName.setObjectName("labelFirstName")
        self.labelLastName = QtWidgets.QLabel(self.centralwidget)
        self.labelLastName.setGeometry(QtCore.QRect(70, 310, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelLastName.setFont(font)
        self.labelLastName.setObjectName("labelLastName")
        self.labelAmount = QtWidgets.QLabel(self.centralwidget)
        self.labelAmount.setGeometry(QtCore.QRect(70, 370, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelAmount.setFont(font)
        self.labelAmount.setObjectName("labelAmount")
        self.lineEditFirstName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditFirstName.setGeometry(QtCore.QRect(240, 260, 291, 31))
        self.lineEditFirstName.setObjectName("lineEditFirstName")
        self.lineEditAccountNumber = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditAccountNumber.setGeometry(QtCore.QRect(240, 200, 291, 31))
        self.lineEditAccountNumber.setObjectName("lineEditAccountNumber")
        self.lineEditLastName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditLastName.setGeometry(QtCore.QRect(240, 320, 291, 31))
        self.lineEditLastName.setObjectName("lineEditLastName")
        self.lineEditAmount = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditAmount.setGeometry(QtCore.QRect(240, 370, 291, 31))
        self.lineEditAmount.setObjectName("lineEditAmount")
        self.pushButtonGenerate = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.toCheque())
        self.pushButtonGenerate.setGeometry(QtCore.QRect(610, 470, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonGenerate.setFont(font)
        self.pushButtonGenerate.setObjectName("pushButtonGenerate")
        # self.pushButtonGenerate.clicked.connect(DataEntry.close)
        self.pushButtonInsert = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonInsert.setGeometry(QtCore.QRect(130, 470, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonInsert.setFont(font)
        self.pushButtonInsert.setObjectName("pushButtonInsert")
        self.pushButtonInsert.clicked.connect(self.insertData)
        self.pushButtonRefresh = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.record())
        self.pushButtonRefresh.setGeometry(QtCore.QRect(380, 470, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonRefresh.setFont(font)
        self.pushButtonRefresh.setObjectName("pushButtonRefresh")
        DataEntry.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DataEntry)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        DataEntry.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DataEntry)
        self.statusbar.setObjectName("statusbar")
        DataEntry.setStatusBar(self.statusbar)

        self.retranslateUi(DataEntry)
        QtCore.QMetaObject.connectSlotsByName(DataEntry)

    def retranslateUi(self, DataEntry):
        _translate = QtCore.QCoreApplication.translate
        DataEntry.setWindowTitle(_translate("DataEntry", "MainWindow"))
        self.labelTitle.setText(_translate("DataEntry", "MONEY BANK"))
        self.labelAccountNumber.setText(_translate("DataEntry", "Account number:"))
        self.labelFirstName.setText(_translate("DataEntry", "First Name:"))
        self.labelLastName.setText(_translate("DataEntry", "Last Name:"))
        self.labelAmount.setText(_translate("DataEntry", "Amount:"))
        self.pushButtonGenerate.setText(_translate("DataEntry", "Generate"))
        self.pushButtonInsert.setText(_translate("DataEntry", "Insert"))
        self.pushButtonRefresh.setText(_translate("DataEntry", "Print"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    DataEntry = QtWidgets.QMainWindow()
    ui = Ui_DataEntry()
    ui.setupUi(DataEntry)
    DataEntry.show()
    sys.exit(app.exec_())
