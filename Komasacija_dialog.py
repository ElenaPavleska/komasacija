# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Komasacija_dialog_base.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import os
from PyQt4 import QtCore, QtGui, uic

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'Komasacija_dialog_base.ui'))

class Ui_Komasacija(QtGui.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(Ui_Komasacija, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, Komasacija):
        Komasacija.setObjectName(_fromUtf8("Komasacija"))
        Komasacija.setEnabled(True)
        Komasacija.resize(583, 462)
        Komasacija.setMinimumSize(QtCore.QSize(583, 462))
        Komasacija.setMaximumSize(QtCore.QSize(583, 462))
        self.label_2 = QtGui.QLabel(Komasacija)
        self.label_2.setGeometry(QtCore.QRect(70, 180, 111, 31))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Komasacija)
        self.label_3.setGeometry(QtCore.QRect(70, 220, 111, 31))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Komasacija)
        self.label_4.setGeometry(QtCore.QRect(290, 180, 111, 31))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_6 = QtGui.QLabel(Komasacija)
        self.label_6.setGeometry(QtCore.QRect(290, 220, 111, 31))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.klasa1 = QtGui.QLineEdit(Komasacija)
        self.klasa1.setGeometry(QtCore.QRect(190, 180, 91, 31))
        self.klasa1.setInputMask(_fromUtf8(""))
        self.klasa1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.klasa1.setObjectName(_fromUtf8("klasa1"))
        self.klasa2 = QtGui.QLineEdit(Komasacija)
        self.klasa2.setGeometry(QtCore.QRect(190, 220, 91, 31))
        self.klasa2.setInputMask(_fromUtf8(""))
        self.klasa2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.klasa2.setObjectName(_fromUtf8("klasa2"))
        self.klasa3 = QtGui.QLineEdit(Komasacija)
        self.klasa3.setGeometry(QtCore.QRect(410, 180, 91, 31))
        self.klasa3.setInputMask(_fromUtf8(""))
        self.klasa3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.klasa3.setObjectName(_fromUtf8("klasa3"))
        self.klasa4 = QtGui.QLineEdit(Komasacija)
        self.klasa4.setGeometry(QtCore.QRect(410, 220, 91, 31))
        self.klasa4.setInputMask(_fromUtf8(""))
        self.klasa4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.klasa4.setObjectName(_fromUtf8("klasa4"))
        self.label_7 = QtGui.QLabel(Komasacija)
        self.label_7.setGeometry(QtCore.QRect(-10, 260, 191, 31))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.btnOdabirLokacijeIzlaznogShp = QtGui.QPushButton(Komasacija)
        self.btnOdabirLokacijeIzlaznogShp.setGeometry(QtCore.QRect(510, 260, 41, 32))
        self.btnOdabirLokacijeIzlaznogShp.setObjectName(_fromUtf8("btnOdabirLokacijeIzlaznogShp"))
        self.lineEdit_7 = QtGui.QLineEdit(Komasacija)
        self.lineEdit_7.setGeometry(QtCore.QRect(190, 260, 311, 31))
        self.lineEdit_7.setInputMask(_fromUtf8(""))
        self.lineEdit_7.setText(_fromUtf8(""))
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.groupBox = QtGui.QGroupBox(Komasacija)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 561, 151))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.shpPlodno = QtGui.QComboBox(self.groupBox)
        self.shpPlodno.setGeometry(QtCore.QRect(180, 21, 361, 31))
        self.shpPlodno.setObjectName(_fromUtf8("shpPlodno"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(0, 20, 171, 31))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(0, 60, 171, 31))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.shpNeplodno = QtGui.QComboBox(self.groupBox)
        self.shpNeplodno.setGeometry(QtCore.QRect(180, 60, 361, 31))
        self.shpNeplodno.setObjectName(_fromUtf8("shpNeplodno"))
        self.shpKlase = QtGui.QComboBox(self.groupBox)
        self.shpKlase.setGeometry(QtCore.QRect(180, 100, 361, 31))
        self.shpKlase.setObjectName(_fromUtf8("shpKlase"))
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(0, 100, 171, 31))
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.groupBox_2 = QtGui.QGroupBox(Komasacija)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 300, 561, 151))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.btnRacunaj = QtGui.QPushButton(self.groupBox_2)
        self.btnRacunaj.setGeometry(QtCore.QRect(180, 20, 251, 41))
        self.btnRacunaj.setObjectName(_fromUtf8("btnRacunaj"))
        self.btnMrezePuteva = QtGui.QPushButton(self.groupBox_2)
        self.btnMrezePuteva.setGeometry(QtCore.QRect(180, 100, 131, 31))
        self.btnMrezePuteva.setObjectName(_fromUtf8("btnMrezePuteva"))
        self.btnPregledKnjigeFonda = QtGui.QPushButton(self.groupBox_2)
        self.btnPregledKnjigeFonda.setGeometry(QtCore.QRect(180, 70, 131, 31))
        self.btnPregledKnjigeFonda.setObjectName(_fromUtf8("btnPregledKnjigeFonda"))
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(0, 70, 171, 31))
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(0, 100, 171, 31))
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))

        self.retranslateUi(Komasacija)
        QtCore.QMetaObject.connectSlotsByName(Komasacija)
        Komasacija.setTabOrder(self.shpPlodno, self.shpNeplodno)
        Komasacija.setTabOrder(self.shpNeplodno, self.shpKlase)
        Komasacija.setTabOrder(self.shpKlase, self.klasa1)
        Komasacija.setTabOrder(self.klasa1, self.klasa3)
        Komasacija.setTabOrder(self.klasa3, self.klasa2)
        Komasacija.setTabOrder(self.klasa2, self.klasa4)
        Komasacija.setTabOrder(self.klasa4, self.lineEdit_7)
        Komasacija.setTabOrder(self.lineEdit_7, self.btnOdabirLokacijeIzlaznogShp)
        Komasacija.setTabOrder(self.btnOdabirLokacijeIzlaznogShp, self.btnRacunaj)
        Komasacija.setTabOrder(self.btnRacunaj, self.btnPregledKnjigeFonda)
        Komasacija.setTabOrder(self.btnPregledKnjigeFonda, self.btnMrezePuteva)

    def retranslateUi(self, Komasacija):
        Komasacija.setWindowTitle(_translate("Komasacija", "Komasacija", None))
        self.label_2.setText(_translate("Komasacija", "Klasa 1 vrednost:", None))
        self.label_3.setText(_translate("Komasacija", "Klasa 2 vrednost:", None))
        self.label_4.setText(_translate("Komasacija", "Klasa 3 vrednost:", None))
        self.label_6.setText(_translate("Komasacija", "Klasa 4 vrednost:", None))
        self.klasa1.setText(_translate("Komasacija", "1", None))
        self.klasa2.setText(_translate("Komasacija", "2", None))
        self.klasa3.setText(_translate("Komasacija", "3", None))
        self.klasa4.setText(_translate("Komasacija", "4", None))
        self.label_7.setText(_translate("Komasacija", "Lokacije Izlazni Shape file:", None))
        self.btnOdabirLokacijeIzlaznogShp.setText(_translate("Komasacija", "...", None))
        self.groupBox.setTitle(_translate("Komasacija", "Ulazni podatci", None))
        self.label.setText(_translate("Komasacija", "Plodno zemljiste Shape file:", None))
        self.label_5.setText(_translate("Komasacija", "Neplodno zemljiste Shape file:", None))
        self.label_11.setText(_translate("Komasacija", "Klase Shape file:", None))
        self.groupBox_2.setTitle(_translate("Komasacija", "Kalkulacii", None))
        self.btnRacunaj.setText(_translate("Komasacija", "Racunaj", None))
        self.btnMrezePuteva.setText(_translate("Komasacija", "Pregled", None))
        self.btnPregledKnjigeFonda.setText(_translate("Komasacija", "Pregled", None))
        self.label_8.setText(_translate("Komasacija", "Knjige fonda komasacione mase:", None))
        self.label_9.setText(_translate("Komasacija", "Projektovanje mreze puteva i tabli:", None))

