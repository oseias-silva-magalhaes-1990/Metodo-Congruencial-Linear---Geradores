from PyQt5 import QtCore, QtGui, QtWidgets
import time
import math

class Ui_MCL(object):
    def setupUi(self, MCL):
        MCL.setObjectName("MCL")
        MCL.setFixedSize(810, 279)
        self.centralwidget = QtWidgets.QWidget(MCL)
        self.centralwidget.setObjectName("centralwidget")
        self.BoxTR = QtWidgets.QGroupBox(self.centralwidget)
        self.BoxTR.setGeometry(QtCore.QRect(10, 10, 191, 261))
        self.BoxTR.setObjectName("BoxTR")
        self.botaoLimparTR = QtWidgets.QPushButton(self.BoxTR)
        self.botaoLimparTR.setGeometry(QtCore.QRect(50, 220, 75, 23))
        self.botaoLimparTR.setObjectName("botaoLimparTR")
        self.botaoGerarTR = QtWidgets.QPushButton(self.BoxTR)
        self.botaoGerarTR.setGeometry(QtCore.QRect(50, 190, 75, 23))
        self.botaoGerarTR.setObjectName("botaoGerarTR")
        self.campoSemTR = QtWidgets.QLineEdit(self.BoxTR)
        self.campoSemTR.setGeometry(QtCore.QRect(30, 40, 113, 20))
        self.campoSemTR.setObjectName("campoSemTR")
        self.campoMultTR = QtWidgets.QLineEdit(self.BoxTR)
        self.campoMultTR.setGeometry(QtCore.QRect(30, 70, 113, 20))
        self.campoMultTR.setObjectName("campoMultTR")
        self.campoTamTR = QtWidgets.QLineEdit(self.BoxTR)
        self.campoTamTR.setGeometry(QtCore.QRect(30, 100, 113, 20))
        self.campoTamTR.setObjectName("campoTamTR")
        self.campoPriTR = QtWidgets.QLineEdit(self.BoxTR)
        self.campoPriTR.setGeometry(QtCore.QRect(30, 160, 113, 20))
        self.campoPriTR.setObjectName("campoPriTR")
        self.label_n0TR = QtWidgets.QLabel(self.BoxTR)
        self.label_n0TR.setGeometry(QtCore.QRect(10, 40, 16, 16))
        self.label_n0TR.setObjectName("label_n0TR")
        self.label_aTR = QtWidgets.QLabel(self.BoxTR)
        self.label_aTR.setGeometry(QtCore.QRect(10, 70, 16, 16))
        self.label_aTR.setObjectName("label_aTR")
        self.label_iTR = QtWidgets.QLabel(self.BoxTR)
        self.label_iTR.setGeometry(QtCore.QRect(10, 100, 16, 16))
        self.label_iTR.setObjectName("label_iTR")
        self.label_pTR = QtWidgets.QLabel(self.BoxTR)
        self.label_pTR.setGeometry(QtCore.QRect(10, 160, 16, 16))
        self.label_pTR.setObjectName("label_pTR")
        self.label_erroTR = QtWidgets.QLabel(self.BoxTR)
        self.label_erroTR.setGeometry(QtCore.QRect(8, 20, 180, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_erroTR.setFont(font)
        self.label_erroTR.setAlignment(QtCore.Qt.AlignCenter)
        self.label_erroTR.setObjectName("label_erroTR")
        self.campoConstTR = QtWidgets.QLineEdit(self.BoxTR)
        self.campoConstTR.setGeometry(QtCore.QRect(30, 130, 113, 20))
        self.campoConstTR.setObjectName("campoConstTR")
        self.label = QtWidgets.QLabel(self.BoxTR)
        self.label.setGeometry(QtCore.QRect(10, 130, 16, 16))
        self.label.setObjectName("label")
        self.BoxG1 = QtWidgets.QGroupBox(self.centralwidget)
        self.BoxG1.setGeometry(QtCore.QRect(210, 10, 191, 261))
        self.BoxG1.setObjectName("BoxG1")
        self.botaoLimparG1 = QtWidgets.QPushButton(self.BoxG1)
        self.botaoLimparG1.setGeometry(QtCore.QRect(50, 220, 75, 23))
        self.botaoLimparG1.setObjectName("botaoLimparG1")
        self.botaoGerarG1 = QtWidgets.QPushButton(self.BoxG1)
        self.botaoGerarG1.setGeometry(QtCore.QRect(50, 190, 75, 23))
        self.botaoGerarG1.setObjectName("botaoGerarG1")
        self.campoSemG1 = QtWidgets.QLineEdit(self.BoxG1)
        self.campoSemG1.setGeometry(QtCore.QRect(30, 40, 113, 20))
        self.campoSemG1.setObjectName("campoSemG1")
        self.campoMultG1 = QtWidgets.QLineEdit(self.BoxG1)
        self.campoMultG1.setGeometry(QtCore.QRect(30, 70, 113, 20))
        self.campoMultG1.setObjectName("campoMultG1")
        self.campoTamG1 = QtWidgets.QLineEdit(self.BoxG1)
        self.campoTamG1.setGeometry(QtCore.QRect(30, 100, 113, 20))
        self.campoTamG1.setObjectName("campoTamG1")
        self.campoPrimoG1 = QtWidgets.QLineEdit(self.BoxG1)
        self.campoPrimoG1.setGeometry(QtCore.QRect(30, 130, 113, 20))
        self.campoPrimoG1.setObjectName("campoPrimoG1")
        self.label_n0G1 = QtWidgets.QLabel(self.BoxG1)
        self.label_n0G1.setGeometry(QtCore.QRect(10, 40, 16, 16))
        self.label_n0G1.setObjectName("label_n0G1")
        self.label_aG1 = QtWidgets.QLabel(self.BoxG1)
        self.label_aG1.setGeometry(QtCore.QRect(10, 70, 16, 16))
        self.label_aG1.setObjectName("label_aG1")
        self.label_iG1 = QtWidgets.QLabel(self.BoxG1)
        self.label_iG1.setGeometry(QtCore.QRect(10, 100, 16, 16))
        self.label_iG1.setObjectName("label_iG1")
        self.label_pG1 = QtWidgets.QLabel(self.BoxG1)
        self.label_pG1.setGeometry(QtCore.QRect(10, 130, 16, 16))
        self.label_pG1.setObjectName("label_pG1")
        self.label_erroG1 = QtWidgets.QLabel(self.BoxG1)
        self.label_erroG1.setGeometry(QtCore.QRect(8, 20, 180, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_erroG1.setFont(font)
        self.label_erroG1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_erroG1.setObjectName("label_erroG1")
        self.BoxDEC = QtWidgets.QGroupBox(self.centralwidget)
        self.BoxDEC.setGeometry(QtCore.QRect(410, 10, 191, 261))
        self.BoxDEC.setObjectName("BoxDEC")
        self.botaoLimparDEC = QtWidgets.QPushButton(self.BoxDEC)
        self.botaoLimparDEC.setGeometry(QtCore.QRect(50, 220, 75, 23))
        self.botaoLimparDEC.setObjectName("botaoLimparDEC")
        self.botaoGerarDEC = QtWidgets.QPushButton(self.BoxDEC)
        self.botaoGerarDEC.setGeometry(QtCore.QRect(50, 190, 75, 23))
        self.botaoGerarDEC.setObjectName("botaoGerarDEC")
        self.campoSemDEC = QtWidgets.QLineEdit(self.BoxDEC)
        self.campoSemDEC.setGeometry(QtCore.QRect(30, 40, 113, 20))
        self.campoSemDEC.setObjectName("campoSemDEC")
        self.campoMultDEC = QtWidgets.QLineEdit(self.BoxDEC)
        self.campoMultDEC.setGeometry(QtCore.QRect(30, 70, 113, 20))
        self.campoMultDEC.setObjectName("campoMultDEC")
        self.campoTamDEC = QtWidgets.QLineEdit(self.BoxDEC)
        self.campoTamDEC.setGeometry(QtCore.QRect(30, 100, 113, 20))
        self.campoTamDEC.setObjectName("campoTamDEC")
        self.campoPotDEC = QtWidgets.QLineEdit(self.BoxDEC)
        self.campoPotDEC.setGeometry(QtCore.QRect(30, 160, 113, 20))
        self.campoPotDEC.setObjectName("campoPotDEC")
        self.label_n0DEC = QtWidgets.QLabel(self.BoxDEC)
        self.label_n0DEC.setGeometry(QtCore.QRect(10, 40, 16, 16))
        self.label_n0DEC.setObjectName("label_n0DEC")
        self.label_aDEC = QtWidgets.QLabel(self.BoxDEC)
        self.label_aDEC.setGeometry(QtCore.QRect(10, 70, 16, 16))
        self.label_aDEC.setObjectName("label_aDEC")
        self.label_iDEC = QtWidgets.QLabel(self.BoxDEC)
        self.label_iDEC.setGeometry(QtCore.QRect(10, 100, 16, 16))
        self.label_iDEC.setObjectName("label_iDEC")
        self.label_xDEC = QtWidgets.QLabel(self.BoxDEC)
        self.label_xDEC.setGeometry(QtCore.QRect(10, 160, 16, 16))
        self.label_xDEC.setObjectName("label_xDEC")
        self.label_erroDEC = QtWidgets.QLabel(self.BoxDEC)
        self.label_erroDEC.setGeometry(QtCore.QRect(8, 20, 180, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_erroDEC.setFont(font)
        self.label_erroDEC.setAlignment(QtCore.Qt.AlignCenter)
        self.label_erroDEC.setObjectName("label_erroDEC")
        self.campoConstDEC = QtWidgets.QLineEdit(self.BoxDEC)
        self.campoConstDEC.setGeometry(QtCore.QRect(30, 130, 113, 20))
        self.campoConstDEC.setObjectName("campoConstDEC")
        self.label_cDEC = QtWidgets.QLabel(self.BoxDEC)
        self.label_cDEC.setGeometry(QtCore.QRect(10, 130, 16, 16))
        self.label_cDEC.setObjectName("label_cDEC")
        self.BoxSAS = QtWidgets.QGroupBox(self.centralwidget)
        self.BoxSAS.setGeometry(QtCore.QRect(610, 10, 191, 261))
        self.BoxSAS.setObjectName("BoxSAS")
        self.botaoLimparSAS = QtWidgets.QPushButton(self.BoxSAS)
        self.botaoLimparSAS.setGeometry(QtCore.QRect(50, 220, 75, 23))
        self.botaoLimparSAS.setObjectName("botaoLimparSAS")
        self.botaoGerarSAS = QtWidgets.QPushButton(self.BoxSAS)
        self.botaoGerarSAS.setGeometry(QtCore.QRect(50, 190, 75, 23))
        self.botaoGerarSAS.setObjectName("botaoGerarSAS")
        self.campoSemSAS = QtWidgets.QLineEdit(self.BoxSAS)
        self.campoSemSAS.setGeometry(QtCore.QRect(30, 40, 113, 20))
        self.campoSemSAS.setObjectName("campoSemSAS")
        self.campoMultSAS = QtWidgets.QLineEdit(self.BoxSAS)
        self.campoMultSAS.setGeometry(QtCore.QRect(30, 70, 113, 20))
        self.campoMultSAS.setObjectName("campoMultSAS")
        self.campoTamSAS = QtWidgets.QLineEdit(self.BoxSAS)
        self.campoTamSAS.setGeometry(QtCore.QRect(30, 100, 113, 20))
        self.campoTamSAS.setObjectName("campoTamSAS")
        self.campoPrimoSAS = QtWidgets.QLineEdit(self.BoxSAS)
        self.campoPrimoSAS.setGeometry(QtCore.QRect(30, 130, 113, 20))
        self.campoPrimoSAS.setObjectName("campoPrimoSAS")
        self.label_n0SAS = QtWidgets.QLabel(self.BoxSAS)
        self.label_n0SAS.setGeometry(QtCore.QRect(10, 40, 16, 16))
        self.label_n0SAS.setObjectName("label_n0SAS")
        self.label_aSAS = QtWidgets.QLabel(self.BoxSAS)
        self.label_aSAS.setGeometry(QtCore.QRect(10, 70, 16, 16))
        self.label_aSAS.setObjectName("label_aSAS")
        self.label_iSAS = QtWidgets.QLabel(self.BoxSAS)
        self.label_iSAS.setGeometry(QtCore.QRect(10, 100, 16, 16))
        self.label_iSAS.setObjectName("label_iSAS")
        self.label_pSAS = QtWidgets.QLabel(self.BoxSAS)
        self.label_pSAS.setGeometry(QtCore.QRect(10, 130, 16, 16))
        self.label_pSAS.setObjectName("label_pSAS")
        self.label_erroSAS = QtWidgets.QLabel(self.BoxSAS)
        self.label_erroSAS.setGeometry(QtCore.QRect(8, 20, 180, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_erroSAS.setFont(font)
        self.label_erroSAS.setAlignment(QtCore.Qt.AlignCenter)
        self.label_erroSAS.setObjectName("label_erroSAS")
        MCL.setCentralWidget(self.centralwidget)

        self.retranslateUi(MCL)
        self.botaoGerarTR.clicked.connect(self.campoPriTR.copy)
        self.botaoGerarTR.clicked.connect(self.campoTamTR.copy)
        self.botaoGerarTR.clicked.connect(self.campoMultTR.copy)
        self.botaoGerarTR.clicked.connect(self.campoSemTR.copy)
        self.botaoLimparTR.clicked.connect(self.campoPriTR.clear)
        self.botaoLimparTR.clicked.connect(self.campoTamTR.clear)
        self.botaoLimparTR.clicked.connect(self.campoMultTR.clear)
        self.botaoLimparTR.clicked.connect(self.campoSemTR.clear)
        self.botaoGerarG1.clicked.connect(self.campoPrimoG1.copy)
        self.botaoGerarG1.clicked.connect(self.campoTamG1.copy)
        self.botaoGerarG1.clicked.connect(self.campoMultG1.copy)
        self.botaoGerarG1.clicked.connect(self.campoSemG1.copy)
        self.botaoLimparG1.clicked.connect(self.campoPrimoG1.clear)
        self.botaoLimparG1.clicked.connect(self.campoTamG1.clear)
        self.botaoLimparG1.clicked.connect(self.campoMultG1.clear)
        self.botaoLimparG1.clicked.connect(self.campoSemG1.clear)
        self.botaoGerarDEC.clicked.connect(self.campoPotDEC.copy)
        self.botaoGerarDEC.clicked.connect(self.campoConstDEC.copy)
        self.botaoGerarDEC.clicked.connect(self.campoTamDEC.copy)
        self.botaoGerarDEC.clicked.connect(self.campoMultDEC.copy)
        self.botaoGerarDEC.clicked.connect(self.campoSemDEC.copy)
        self.botaoLimparDEC.clicked.connect(self.campoPotDEC.clear)
        self.botaoLimparDEC.clicked.connect(self.campoConstDEC.clear)
        self.botaoLimparDEC.clicked.connect(self.campoTamDEC.clear)
        self.botaoLimparDEC.clicked.connect(self.campoMultDEC.clear)
        self.botaoLimparDEC.clicked.connect(self.campoSemDEC.clear)
        self.botaoGerarSAS.clicked.connect(self.campoPrimoSAS.copy)
        self.botaoGerarSAS.clicked.connect(self.campoTamSAS.copy)
        self.botaoGerarSAS.clicked.connect(self.campoMultSAS.copy)
        self.botaoGerarSAS.clicked.connect(self.campoSemSAS.copy)
        self.botaoLimparSAS.clicked.connect(self.campoPrimoSAS.clear)
        self.botaoLimparSAS.clicked.connect(self.campoTamSAS.clear)
        self.botaoLimparSAS.clicked.connect(self.campoMultSAS.clear)
        self.botaoLimparSAS.clicked.connect(self.campoSemSAS.clear)
        self.botaoLimparTR.clicked.connect(self.campoConstTR.clear)
        self.botaoGerarTR.clicked.connect(self.campoConstTR.copy)

        self.label_erroTR.setVisible(False)
        self.label_erroG1.setVisible(False)
        self.label_erroDEC.setVisible(False)
        self.label_erroSAS.setVisible(False)

        self.botaoGerarTR.clicked.connect(self.verificaCamposTR)
        self.botaoGerarG1.clicked.connect(self.verificaCamposG1)
        self.botaoGerarDEC.clicked.connect(self.verificaCamposDEC)
        self.botaoGerarSAS.clicked.connect(self.verificaCamposSAS)

        self.botaoLimparTR.clicked.connect(self.label_erroTR.clear)
        self.botaoLimparG1.clicked.connect(self.label_erroG1.clear)
        self.botaoLimparDEC.clicked.connect(self.label_erroDEC.clear)
        self.botaoLimparSAS.clicked.connect(self.label_erroSAS.clear)

        #expressões regulares Trabalho
        self.campoMultTR.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[1-9][0-9]{8}"), self.campoMultTR))
        self.campoPriTR.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-1][0-2][0-7]||[0-9][0-9]"), self.campoPriTR))
        self.campoSemTR.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[1-9][0-9]{3}"), self.campoSemTR))
        self.campoConstTR.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[1-9][0-9]{3}"), self.campoTamTR))
        self.campoTamTR.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]{6}||[1][0]{6}"), self.campoTamTR))

        # expressões regulares Gerador 1
        self.campoMultG1.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[1-9][0-9]{4}"), self.campoMultG1))
        self.campoPrimoG1.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-1][0-2][0-7]||[0-9][0-9]"), self.campoPrimoG1))
        self.campoSemG1.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[1-9][0-9]{3}"), self.campoSemG1))
        self.campoTamG1.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]{6}||[1][0]{6}"), self.campoTamG1))

        # expressões regulares Gerador DEC
        self.campoMultDEC.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[1-9][0-9]{4}"), self.campoMultDEC))
        self.campoPotDEC.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[1-9][0-9]"), self.campoPotDEC))
        self.campoSemDEC.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[1-9][0-9]{3}"), self.campoSemDEC))
        self.campoTamDEC.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]{6}||[1][0]{6}"), self.campoTamDEC))
        self.campoConstDEC.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[1-9][0-9]{3}"), self.campoConstDEC))

        # expressões regulares Gerador SAS
        self.campoMultSAS.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[1-9][0-9]{8}"), self.campoMultSAS))
        self.campoPrimoSAS.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-1][0-2][0-7]||[0-9][0-9]"), self.campoPrimoSAS))
        self.campoSemSAS.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[1-9][0-9]{3}"), self.campoSemSAS))
        self.campoTamSAS.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]{6}||[1][0]{6}"), self.campoTamSAS))

        QtCore.QMetaObject.connectSlotsByName(MCL)

    def retranslateUi(self, MCL):
        _translate = QtCore.QCoreApplication.translate
        MCL.setWindowTitle(_translate("MCL", "MCL Geradores"))
        self.BoxTR.setTitle(_translate("MCL", "Gerador TR"))
        self.botaoLimparTR.setText(_translate("MCL", "Limpar"))
        self.botaoGerarTR.setText(_translate("MCL", "Gerar Valores"))
        self.campoSemTR.setPlaceholderText(_translate("MCL", "Semente"))
        self.campoMultTR.setPlaceholderText(_translate("MCL", "Multiplicador"))
        self.campoTamTR.setPlaceholderText(_translate("MCL", "Tamanho"))
        self.campoPriTR.setPlaceholderText(_translate("MCL", "Primo (2^p)-1"))
        self.label_n0TR.setText(_translate("MCL", "n0"))
        self.label_aTR.setText(_translate("MCL", "a"))
        self.label_iTR.setText(_translate("MCL", "i"))
        self.label_pTR.setText(_translate("MCL", "p"))
        self.label_erroTR.setText(_translate("MCL", "Label Erro"))
        self.campoConstTR.setPlaceholderText(_translate("MCL", "Constante"))
        self.label.setText(_translate("MCL", "c"))
        self.BoxG1.setTitle(_translate("MCL", "Gerador 1"))
        self.botaoLimparG1.setText(_translate("MCL", "Limpar"))
        self.botaoGerarG1.setText(_translate("MCL", "Gerar Valores"))
        self.campoSemG1.setPlaceholderText(_translate("MCL", "Semente"))
        self.campoMultG1.setPlaceholderText(_translate("MCL", "Multiplicador"))
        self.campoTamG1.setPlaceholderText(_translate("MCL", "Tamanho"))
        self.campoPrimoG1.setPlaceholderText(_translate("MCL", "Primo (2^p)-1"))
        self.label_n0G1.setText(_translate("MCL", "n0"))
        self.label_aG1.setText(_translate("MCL", "a"))
        self.label_iG1.setText(_translate("MCL", "i"))
        self.label_pG1.setText(_translate("MCL", "p"))
        self.label_erroG1.setText(_translate("MCL", "Label Erro"))
        self.BoxDEC.setTitle(_translate("MCL", "Gerador DEC"))
        self.botaoLimparDEC.setText(_translate("MCL", "Limpar"))
        self.botaoGerarDEC.setText(_translate("MCL", "Gerar Valores"))
        self.campoSemDEC.setPlaceholderText(_translate("MCL", "Semente"))
        self.campoMultDEC.setPlaceholderText(_translate("MCL", "Multiplicador"))
        self.campoTamDEC.setPlaceholderText(_translate("MCL", "Tamanho"))
        self.campoPotDEC.setPlaceholderText(_translate("MCL", "2^x"))
        self.label_n0DEC.setText(_translate("MCL", "n0"))
        self.label_aDEC.setText(_translate("MCL", "a"))
        self.label_iDEC.setText(_translate("MCL", "i"))
        self.label_xDEC.setText(_translate("MCL", "x"))
        self.label_erroDEC.setText(_translate("MCL", "Label Erro"))
        self.campoConstDEC.setPlaceholderText(_translate("MCL", "Constante"))
        self.label_cDEC.setText(_translate("MCL", "c"))
        self.BoxSAS.setTitle(_translate("MCL", "Gerador SAS"))
        self.botaoLimparSAS.setText(_translate("MCL", "Limpar"))
        self.botaoGerarSAS.setText(_translate("MCL", "Gerar Valores"))
        self.campoSemSAS.setPlaceholderText(_translate("MCL", "Semente"))
        self.campoMultSAS.setPlaceholderText(_translate("MCL", "Multiplicador"))
        self.campoTamSAS.setPlaceholderText(_translate("MCL", "Tamanho"))
        self.campoPrimoSAS.setPlaceholderText(_translate("MCL", "Primo (2^p)-1"))
        self.label_n0SAS.setText(_translate("MCL", "n0"))
        self.label_aSAS.setText(_translate("MCL", "a"))
        self.label_iSAS.setText(_translate("MCL", "i"))
        self.label_pSAS.setText(_translate("MCL", "p"))
        self.label_erroSAS.setText(_translate("MCL", "Label Erro"))

    def verificaCamposTR(self):
        if self.campoMultTR.text() and self.campoConstTR.text() and self.campoPriTR.text() and self.campoSemTR.text() and self.campoTamTR:
            self.verificaPrimo(self.campoPriTR.text())
            if self.verificaPrimo(self.campoPriTR.text()):
                self.executaGeradorTR()
            else:
                self.label_erroTR.clear()
                self.label_erroTR.setText("Não é Primo")
                self.label_erroTR.setStyleSheet('QLabel {color: red}')
                self.label_erroTR.setVisible(True)
        else:
            self.label_erroTR.clear()
            self.label_erroTR.setText("Preencha todos os campos")
            self.label_erroTR.setStyleSheet('QLabel {color: red}')
            self.label_erroTR.setVisible(True)

    def verificaCamposG1(self):
        if self.campoMultG1.text() and self.campoPrimoG1.text() and self.campoSemG1.text() and self.campoTamG1:
            if self.verificaPrimo(self.campoPrimoG1.text()):
                self.executaGerador1()
            else:
                self.label_erroG1.clear()
                self.label_erroG1.setText("Não é Primo")
                self.label_erroG1.setStyleSheet('QLabel {color: red}')
                self.label_erroG1.setVisible(True)
        else:
            self.label_erroG1.clear()
            self.label_erroG1.setText("Preencha todos os campos")
            self.label_erroG1.setStyleSheet('QLabel {color: red}')
            self.label_erroG1.setVisible(True)

    def verificaCamposDEC(self):
        if self.campoMultDEC.text() and self.campoConstDEC.text() and self.campoPotDEC.text() and self.campoSemDEC.text() and self.campoTamDEC:
            self.executaGeradorDEC()
        else:
            self.label_erroDEC.clear()
            self.label_erroDEC.setText("Preencha todos os campos")
            self.label_erroDEC.setStyleSheet('QLabel {color: red}')
            self.label_erroDEC.setVisible(True)

    def verificaCamposSAS(self):
        if self.campoMultSAS.text() and self.campoPrimoSAS.text() and self.campoSemSAS.text() and self.campoTamSAS:
            if self.verificaPrimo(self.campoPrimoSAS.text()):
                self.executaGeradorSAS()
            else:
                self.label_erroSAS.clear()
                self.label_erroSAS.setText("Não é Primo")
                self.label_erroSAS.setStyleSheet('QLabel {color: red}')
                self.label_erroSAS.setVisible(True)
        else:
            self.label_erroSAS.clear()
            self.label_erroSAS.setText("Preencha todos os campos")
            self.label_erroSAS.setStyleSheet('QLabel {color: red}')
            self.label_erroSAS.setVisible(True)

    def verificaPrimo(self, primo):
        n = int(primo)
        mult = 0

        for count in range(2, n):#inicializa o contador em um range de 2 até n-ésimo valor informado
            if (n % count == 0):#verifica se o resto da divisão do valor informado n pelo contador cont  é zero
                mult += 1#incrementa a variável de controle mult se o resto da divisão for igual a zero
        if (mult != 0):#Se o resto da divisão for zero então ele não é primo
            return False
        else:#senão incrementar então o valor digitado é primo
            return True

    def executaGeradorTR(self):
        self.label_erroTR.clear()
        n0 = int(self.campoSemTR.text())  # semente
        a = int(self.campoMultTR.text())  # fator multiplicador inteiro positivo > 0
        n = int(self.campoTamTR.text())  # quantidade de valores a serem gerados
        c = int(self.campoConstTR.text())  # constante inteira positiva > 0
        p = int(self.campoPriTR.text())  # primo
        m = (pow(2, p)-1)  # modulo
        resultado = []  # vetor para o geração dos valores

        inicioTR = time.time()
        # execução
        for i in range(n):  # O looping funcinará até que seja satisfeita a quantidade n informada
            if i == 0:  # inicializa o arquivo .txt
                resultado.append((a * n0 + c) % m)  # Se estiver vazio atribui a primeira posição
            else:
                resultado.append((a * resultado[i - 1] + c) % m)  # Caso o vetor já possua o valor da semente n0 realiza-se o cálculo da MCL
        fimTR = time.time()
        self.label_erroTR.setText("Tempo: {0:.4f}".format(fimTR-inicioTR))
        self.label_erroTR.setStyleSheet('QLabel {color: black}')
        self.label_erroTR.setVisible(True)

        # Gravação do arquivo CRIALEO.txt Gerador Trabalho
        arquivo = open("Gerador TR\CRIALEO.txt", "w")
        arquivo.write("***************************************************\n")  # Cabecalho do Arquivo Texto
        arquivo.write("***************************************************\n")
        arquivo.write("GERADOR TR\n")
        arquivo.write("Semente: " + self.campoSemTR.text() + "\n")
        arquivo.write("Multiplicador: " + self.campoMultTR.text() + "\n")
        arquivo.write("Tamanho: " + self.campoTamTR.text() + "\n")
        arquivo.write("Constante: " + self.campoConstTR.text() + "\n")
        arquivo.write("Primo: " + self.campoPriTR.text() + "\n")
        arquivo.write("Mercene: " + str(m) + "\n")
        arquivo.write("Tempo de execucao: {0:.4f}".format(fimTR - inicioTR) + "\n")
        arquivo.write("***************************************************\n")
        arquivo.write("***************************************************\n\n")

        for i in range(n):
            arquivo.write(str(resultado[i]/m) + "\n")  #Escreve no arquivo .txt o valor armazenado no vetor em formato decimal

        arquivo.close()

    def executaGerador1(self):
        self.label_erroG1.clear()
        n0 = int(self.campoSemG1.text())#semente
        a = int(self.campoMultG1.text())#fator multiplicador
        n = int(self.campoTamG1.text())#quantidade de valores a serem gerados
        p = int(self.campoPrimoG1.text())#numero primo
        m = (pow(2,p))-1 #numero de mersene
        resultado = [] #vetor para o geração dos valores

        inicioG1 = time.time()
        #execução
        for i in range(n):#O looping funcinará até que seja satisfeita a quantidade n informada
            if i == 0:#inicializa o arquivo .txt
                resultado.append((a * n0) % m)#Se estiver vazio atribui a primeira posição a semente
            else:
                resultado.append((a * resultado[i - 1]) % m)#Caso o vetor já possua o valor da semente n0 realiza-se o cálculo da MCL Multiplicativa
        fimG1 = time.time()
        self.label_erroG1.setText("Tempo: {0:.4f}".format(fimG1-inicioG1))
        self.label_erroG1.setStyleSheet('QLabel {color: black}')
        self.label_erroG1.setVisible(True)

        #Gravação do arquivo CRIALEO.txt GERADOR 1
        arquivo = open("Gerador 1\CRIALEO.txt", "w")# Cabecalho do Arquivo Texto
        arquivo.write("***************************************************\n")
        arquivo.write("***************************************************\n")
        arquivo.write("GERADOR 1\n")
        arquivo.write("Semente: " + self.campoSemG1.text()+"\n")
        arquivo.write("Multiplicador: " + self.campoMultG1.text()+"\n")
        arquivo.write("Tamanho: " + self.campoTamG1.text()+"\n")
        arquivo.write("Primo: " + self.campoPrimoG1.text()+"\n")
        arquivo.write("Mercene: " + str(m)+"\n")
        arquivo.write("Tempo de execucao: {0:.4f}".format(fimG1 - inicioG1) + "\n")
        arquivo.write("***************************************************\n")
        arquivo.write("***************************************************\n\n")

        for i in range(n):
            arquivo.write(str(resultado[i]/m) + "\n")  #Escreve no arquivo .txt o valor armazenado no vetor em formato decimal
        arquivo.close()

    def executaGeradorDEC(self):
        self.label_erroDEC.clear()
        n0 = int(self.campoSemDEC.text())#semente
        a = int(self.campoMultDEC.text())#fator multiplicador inteiro positivo > 0
        n = int(self.campoTamDEC.text())#quantidade de valores a serem gerados
        c = int(self.campoConstDEC.text())#constante inteira positiva > 0
        x = int(self.campoPotDEC.text())#potencia
        m = (pow(2,x))#modulo
        resultado = []#vetor para o geração dos valores

        inicioDEC = time.time()
        #execução
        for i in range(n):#O looping funcinará até que seja satisfeita a quantidade n informada
            if i == 0:#inicializa o arquivo .txt
                resultado.append((a * n0 + c) % m)#Se estiver vazio atribui a primeira posição a semente
            else:
                resultado.append(((a * resultado[i - 1] + c) % m))#Caso o vetor já possua o valor da semente n0 realiza-se o cálculo da MCL Multiplicativa
        fimDEC = time.time()
        self.label_erroDEC.setText("Tempo: {0:.4f}".format(fimDEC-inicioDEC))
        self.label_erroDEC.setStyleSheet('QLabel {color: black}')
        self.label_erroDEC.setVisible(True)

        #Gravação do arquivo CRIALEO.txt
        arquivo = open("Gerador DEC\CRIALEO.txt", "w")
        arquivo.write("***************************************************\n")# Cabecalho do Arquivo Texto
        arquivo.write("***************************************************\n")
        arquivo.write("GERADOR DEC\n")
        arquivo.write("Semente: " + self.campoSemDEC.text() + "\n")
        arquivo.write("Multiplicador: " + self.campoMultDEC.text() + "\n")
        arquivo.write("Tamanho: " + self.campoTamDEC.text() + "\n")
        arquivo.write("Constante: " + self.campoConstDEC.text() + "\n")
        arquivo.write("Potência: " + self.campoPotDEC.text() + "\n")
        arquivo.write("Módulo: " + str(m) + "\n")
        arquivo.write("Tempo de execucaoo: {0:.4f}".format(fimDEC - inicioDEC) + "\n")
        arquivo.write("***************************************************\n")
        arquivo.write("***************************************************\n\n")

        for i in range(n):
            arquivo.write(str(resultado[i]/m) + "\n") #Escreve no arquivo .txt o valor armazenado no vetor em formato decimal
        arquivo.close()

    def executaGeradorSAS(self):
        self.label_erroSAS.clear()

        n0 = int(self.campoSemSAS.text())#semente
        a = int(self.campoMultSAS.text())#fator multiplicador
        n = int(self.campoTamSAS.text())#quantidade de valores a serem gerados
        p = int(self.campoPrimoSAS.text())#numero primo
        m = (pow(2,p))-1 #numero de mersene
        resultado = [] #vetor para o geração dos valores

        inicioSAS = time.time()
        #gerador
        for i in range(n):#O looping funcinará até que seja satisfeita a quantidade n informada
            if i == 0:#inicializa o arquivo .txt
                resultado.append((a * n0) % m)#Se estiver vazio atribui a primeira posição a semente
            else:
                resultado.append((a * resultado[i - 1]) % m)#Caso o vetor já possua o valor da semente n0 realiza-se o cálculo da MCL Multiplicativa
        fimSAS = time.time()
        self.label_erroSAS.setText("Tempo: {0:.4f}".format(fimSAS-inicioSAS))
        self.label_erroSAS.setStyleSheet('QLabel {color: black}')
        self.label_erroSAS.setVisible(True)

        #Gravação do arquivo CRIALEO.txt
        arquivo = open("Gerador SAS\CRIALEO.txt", "w")# Cabecalho do Arquivo Texto
        arquivo.write("***************************************************\n")
        arquivo.write("***************************************************\n")
        arquivo.write("GERADOR SAS\n")
        arquivo.write("Semente: " + self.campoSemSAS.text()+"\n")
        arquivo.write("Multiplicador: " + self.campoMultSAS.text()+"\n")
        arquivo.write("Tamanho: " + self.campoTamSAS.text()+"\n")
        arquivo.write("Primo: " + self.campoPrimoSAS.text()+"\n")
        arquivo.write("Mercene: " + str(m)+"\n")
        arquivo.write("Tempo de execucao: {0:.4f}".format(fimSAS-inicioSAS)+"\n")
        arquivo.write("***************************************************\n")
        arquivo.write("***************************************************\n\n")

        for i in range(n):
            arquivo.write(str(resultado[i]/m) + "\n")  # Escreve no arquivo .txt o valor armazenado no vetor em formato decimal
        arquivo.close()

        self.testeDeUniformidade(resultado)

    def testeDeUniformidade(self, valores):
        freq = []#frquencias
        tam = len(valores)

        for i in range(10):
            qtd=0
            for j in range(tam):
                a = (str(valores[j]))[0]
                if i == int(a):
                    qtd = qtd +1
            freq.append(qtd)
        print(freq)
        print(valores)

    def testeDasFilas(self, valores):
        print("Fazer")

    def testeDasPermutacoes(self, valores):
        print("Fazer")
        #se T não for multiplo de n fazer n-1

    def menorValor(self, valores):
        n = len(valores)
        menor = 0

        for i in range(n):
            if i==0:
                menor = valores[i]
            if valores[i] < menor:
                    menor = valores[i]
        return menor

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MCL = QtWidgets.QMainWindow()
    ui = Ui_MCL()
    ui.setupUi(MCL)
    MCL.show()
    sys.exit(app.exec_())