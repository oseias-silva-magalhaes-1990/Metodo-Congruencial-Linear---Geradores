import sys
from PyQt5 import QtCore, QtGui, QtWidgets

app = QtWidgets.QApplication(sys.argv)


class GeradorSAS(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Form):

        Form.setObjectName("GeradorSAS")
        Form.setGeometry(QtCore.QRect(800,216,210,296))
        Form.setFixedSize(210, 296)


        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 160, 111, 23))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 210, 111, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.label_erro = QtWidgets.QLabel(Form)
        self.label_erro.setGeometry(QtCore.QRect(148, 120, 60, 16))
        self.label_erro.setVisible(False)

        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)

        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)

        self.campoMultiplicador = QtWidgets.QLineEdit(Form)
        self.campoMultiplicador.setGeometry(QtCore.QRect(70, 60, 71, 20))
        self.campoMultiplicador.setObjectName("campoMultiplicador")
        self.campoMultiplicador.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[1-9][0-9]{8}"), self.campoMultiplicador))

        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(50, 60, 16, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(50, 90, 16, 16))
        self.label_8.setObjectName("label_8")
        self.campoTamanho = QtWidgets.QLineEdit(Form)
        self.campoTamanho.setGeometry(QtCore.QRect(70, 90, 71, 20))
        self.campoTamanho.setObjectName("campoTamanho")
        self.campoTamanho.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]{6}||[1][0]{6}"), self.campoTamanho))

        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(50, 120, 16, 16))
        self.label_9.setObjectName("label_9")
        self.campoPrimo = QtWidgets.QLineEdit(Form)
        self.campoPrimo.setGeometry(QtCore.QRect(70, 120, 71, 20))
        self.campoPrimo.setObjectName("campoPrimo")
        self.campoPrimo.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-1][0-2][0-7]||[0-9][0-9]"), self.campoPrimo))

        self.campoSemente = QtWidgets.QLineEdit(Form)
        self.campoSemente.setGeometry(QtCore.QRect(70, 30, 71, 20))
        self.campoSemente.setObjectName("campoSemente")
        self.campoSemente.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]{4}"), self.campoSemente))

        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(46, 30, 20, 20))
        self.label_10.setObjectName("label_10")

        self.retranslateUi(Form)

        self.pushButton.clicked.connect(self.campoPrimo.copy)
        self.pushButton.clicked.connect(self.campoTamanho.copy)
        self.pushButton.clicked.connect(self.campoMultiplicador.copy)
        self.pushButton.clicked.connect(self.campoSemente.copy)
        self.pushButton_2.clicked.connect(self.campoPrimo.clear)
        self.pushButton_2.clicked.connect(self.campoTamanho.clear)
        self.pushButton_2.clicked.connect(self.campoMultiplicador.clear)
        self.pushButton_2.clicked.connect(self.campoSemente.clear)

        self.pushButton.clicked.connect(self.verificaCampos)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("GeradorSAS", "G_SAS"))
        self.pushButton.setText(_translate("GeradorSAS", "Gerar Valores"))
        self.pushButton_2.setText(_translate("GeradorSAS", "LIMPAR CAMPOS"))
        self.label_erro.setText(_translate("GeradorSAS", "Não é primo"))
        self.campoMultiplicador.setPlaceholderText(_translate("GeradorSAS", "Multiplicador"))
        self.label_7.setText(_translate("GeradorSAS", "a"))
        self.label_8.setText(_translate("GeradorSAS", "n"))
        self.campoTamanho.setPlaceholderText(_translate("GeradorSAS", "Tamanho"))
        self.label_9.setText(_translate("GeradorSAS", "p"))
        self.campoPrimo.setPlaceholderText(_translate("GeradorSAS", "Primo (2^p)-1"))
        self.campoSemente.setPlaceholderText(_translate("GeradorSAS", "Semente"))
        self.label_10.setText(_translate("GeradorSAS", "n0"))

    def executaGerador1(self):
        n0 = int(self.campoSemente.text())#semente
        a = int(self.campoMultiplicador.text())#fator multiplicador
        n = int(self.campoTamanho.text())#quantidade de valores a serem gerados
        p = int(self.campoPrimo.text())#numero primo
        m = (pow(2,p))-1 #numero de mersene
        resultado = [] #vetor para o geração dos valores

        # Cabecalho do Arquivo Texto
        arquivo = open("Gerador SAS\CRIALEO.txt", "w")
        arquivo.write("\n\n***************************************************\n")
        arquivo.write("***************************************************\n")
        arquivo.write("GERADOR SAS")
        arquivo.write("Semente: " + self.campoSemente.text()+"\n")
        arquivo.write("Multiplicador: " + self.campoMultiplicador.text()+"\n")
        arquivo.write("Tamanho: " + self.campoTamanho.text()+"\n")
        arquivo.write("Primo: " + self.campoPrimo.text()+"\n")
        arquivo.write("Mercene: " + str(m)+"\n")
        arquivo.write("***************************************************\n")
        arquivo.write("***************************************************\n\n")

        for i in range(n):#O looping funcinará até que seja satisfeita a quantidade n informada
            if i == 0:#inicializa o arquivo .txt
                resultado.append(n0)#Se estiver vazio atribui a primeira posição a semente
                arquivo.write(str(resultado[i])+"\n")#Escreve no arquivo .txt o valor armazenado no vetor
            else:
                resultado.append(((a * resultado[i - 1]) % m))#Caso o vetor já possua o valor da semente n0 realiza-se o cálculo da MCL Multiplicativa
                arquivo.write(str(resultado[i])+"\n")#escreve o ultimo valor atribuido ao vetor no arquivo .txt

        arquivo.close()

    def verificaPrimo(self):
        n = int(self.campoPrimo.text())
        mult = 0

        for count in range(2, n):#inicializa o contador em um range de 2 até n-ésimo valor informado
            if (n % count == 0):#verifica se o resto da divisão do valor informado n pelo contador cont  é zero
                mult += 1#incrementa a variável de controle mult se o resto da divisão for igual a zero
        if (mult != 0):#Se o resto da divisão for zero então ele não é primo
            self.label_erro.setVisible(True)
        else:#senão incrementar então o valor digitado é primo
            self.executaGerador1()
            self.label_erro.setVisible(False)

    def verificaCampos(self):
        if self.campoPrimo.text() and self.campoSemente.text() and self.campoTamanho.text() and self.campoMultiplicador.text():
            self.verificaPrimo()
        else:
            self.label_erro.setGeometry(QtCore.QRect(40, 10, 250, 16))
            self.label_erro.setText("Preencha todos os campos")
            self.label_erro.setStyleSheet('QLabel {color: red}')
            self.label_erro.setVisible(True)

class GeradorDEC(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("GeradorDEC")
        Form.setGeometry(QtCore.QRect(578, 400, 210, 296))
        Form.setFixedSize(210, 296)

        self.botaoGerarValores = QtWidgets.QPushButton(Form)
        self.botaoGerarValores.setGeometry(QtCore.QRect(40, 200, 111, 23))
        self.botaoGerarValores.setObjectName("botaoGerarValores")

        self.botaoLimparCampos = QtWidgets.QPushButton(Form)
        self.botaoLimparCampos.setGeometry(QtCore.QRect(40, 250, 111, 23))
        self.botaoLimparCampos.setObjectName("botaoLimparCampos")

        self.campoMultiplicador = QtWidgets.QLineEdit(Form)
        self.campoMultiplicador.setGeometry(QtCore.QRect(70, 60, 71, 20))
        self.campoMultiplicador.setObjectName("campoMultiplicador")
        self.campoMultiplicador.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[1-9][0-9]{4}"), self.campoMultiplicador))

        self.label_multiplicador = QtWidgets.QLabel(Form)
        self.label_multiplicador.setGeometry(QtCore.QRect(50, 60, 16, 16))
        self.label_multiplicador.setObjectName("label_multiplicador")

        self.label_tamanho = QtWidgets.QLabel(Form)
        self.label_tamanho.setGeometry(QtCore.QRect(50, 90, 16, 16))
        self.label_tamanho.setObjectName("label_tamanho")

        self.campoTamanho = QtWidgets.QLineEdit(Form)
        self.campoTamanho.setGeometry(QtCore.QRect(70, 90, 71, 20))
        self.campoTamanho.setObjectName("campoTamanho")

        self.label_constante = QtWidgets.QLabel(Form)
        self.label_constante.setGeometry(QtCore.QRect(50, 120, 16, 16))
        self.label_constante.setObjectName("label_constante")

        self.campoConstante = QtWidgets.QLineEdit(Form)
        self.campoConstante.setGeometry(QtCore.QRect(70, 120, 71, 20))
        self.campoConstante.setObjectName("campoConstante")
        self.campoConstante.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[1-9]{4}"), self.campoConstante))

        self.campoSemente = QtWidgets.QLineEdit(Form)
        self.campoSemente.setGeometry(QtCore.QRect(70, 30, 71, 20))
        self.campoSemente.setObjectName("campoSemente")
        self.campoSemente.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]{4}"), self.campoSemente))

        self.label_semente = QtWidgets.QLabel(Form)
        self.label_semente.setGeometry(QtCore.QRect(46, 30, 20, 20))
        self.label_semente.setObjectName("label_semente")

        self.label_potencia = QtWidgets.QLabel(Form)
        self.label_potencia.setGeometry(QtCore.QRect(50, 150, 16, 16))
        self.label_potencia.setObjectName("label_potencia")

        self.campoPotencia = QtWidgets.QLineEdit(Form)
        self.campoPotencia.setGeometry(QtCore.QRect(70, 150, 71, 20))
        self.campoPotencia.setObjectName("campoPotencia")
        self.campoPotencia.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-1][0-2][0-7]||[0-9][0-9]"), self.campoPotencia))

        self.retranslateUi(Form)
        self.botaoGerarValores.clicked.connect(self.campoConstante.copy)
        self.botaoGerarValores.clicked.connect(self.campoMultiplicador.copy)
        self.botaoGerarValores.clicked.connect(self.campoSemente.copy)
        self.botaoLimparCampos.clicked.connect(self.campoConstante.clear)
        self.botaoLimparCampos.clicked.connect(self.campoMultiplicador.clear)
        self.botaoLimparCampos.clicked.connect(self.campoSemente.clear)
        self.botaoLimparCampos.clicked.connect(self.campoTamanho.clear)
        self.botaoGerarValores.clicked.connect(self.campoTamanho.copy)
        self.botaoGerarValores.clicked.connect(self.campoPotencia.copy)
        self.botaoLimparCampos.clicked.connect(self.campoPotencia.clear)

        self.botaoGerarValores.clicked.connect(self.verificaCampos)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("GeradorDEC", "G_DEC"))
        self.botaoGerarValores.setText(_translate("GeradorDEC", "Gerar Valores"))
        self.botaoLimparCampos.setText(_translate("GeradorDEC", "LIMPAR CAMPOS"))
        self.campoMultiplicador.setPlaceholderText(_translate("GeradorDEC", "Multiplicador"))
        self.label_multiplicador.setText(_translate("GeradorDEC", "a"))
        self.label_tamanho.setText(_translate("GeradorDEC", "n"))
        self.campoTamanho.setPlaceholderText(_translate("GeradorDEC", "Tamanho"))
        self.label_constante.setText(_translate("GeradorDEC", "c"))
        self.campoConstante.setPlaceholderText(_translate("GeradorDEC", "Constante"))
        self.campoSemente.setPlaceholderText(_translate("GeradorDEC", "Semente"))
        self.label_semente.setText(_translate("GeradorDEC", "n0"))
        self.label_potencia.setText(_translate("GeradorDEC", "x"))
        self.campoPotencia.setPlaceholderText(_translate("GeradorDEC", "2^x"))

    def verificaCampos(self):
        if self.campoPotencia.text() and self.campoSemente.text() and self.campoTamanho.text() and self.campoMultiplicador.text() and self.campoConstante:
            self.executaGeradorDEC()
        else:
            self.label_erro.setGeometry(QtCore.QRect(40, 10, 250, 16))
            self.label_erro.setText("Preencha todos os campos")
            self.label_erro.setStyleSheet('QLabel {color: red}')
            self.label_erro.setVisible(True)

    def executaGeradorDEC(self):
        n0 = int(self.campoSemente.text())#semente
        a = int(self.campoMultiplicador.text())#fator multiplicador inteiro positivo > 0
        n = int(self.campoTamanho.text())#quantidade de valores a serem gerados
        c = int(self.campoConstante.text())#constante inteira positiva > 0
        x = int(self.campoPotencia.text())#potencia
        m = (pow(2,x))#modulo
        resultado = []#vetor para o geração dos valores

        # Cabecalho do Arquivo Texto
        arquivo = open("Gerador DEC\CRIALEO.txt", "w")
        arquivo.write("\n\n***************************************************\n")
        arquivo.write("***************************************************\n")
        arquivo.write("GERADOR DEC")
        arquivo.write("Semente: " + self.campoSemente.text()+"\n")
        arquivo.write("Multiplicador: " + self.campoMultiplicador.text()+"\n")
        arquivo.write("Tamanho: " + self.campoTamanho.text()+"\n")
        arquivo.write("Constante: " + self.campoConstante.text() + "\n")
        arquivo.write("Potencia: " + self.campoPotencia.text()+"\n")
        arquivo.write("Mercene: " + str(m)+"\n")
        arquivo.write("***************************************************\n")
        arquivo.write("***************************************************\n\n")

        for i in range(n):#O looping funcinará até que seja satisfeita a quantidade n informada
            if i == 0:#inicializa o arquivo .txt
                resultado.append(n0)#Se estiver vazio atribui a primeira posição a semente
                arquivo.write(str(resultado[i])+"\n")#Escreve no arquivo .txt o valor armazenado no vetor
            else:
                resultado.append(((a * resultado[i - 1] + c) % m))#Caso o vetor já possua o valor da semente n0 realiza-se o cálculo da MCL Multiplicativa
                arquivo.write(str(resultado[i])+"\n")#escreve o ultimo valor atribuido ao vetor no arquivo .txt

        arquivo.close()

class Gerador1(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Form):

        Form.setObjectName("Gerador1")
        Form.setGeometry(QtCore.QRect(355, 216, 210, 296))
        Form.setFixedSize(210, 296)


        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 160, 111, 23))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 210, 111, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.label_erro = QtWidgets.QLabel(Form)
        self.label_erro.setGeometry(QtCore.QRect(148, 120, 60, 16))
        self.label_erro.setVisible(False)

        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)

        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)

        self.campoMultiplicador = QtWidgets.QLineEdit(Form)
        self.campoMultiplicador.setGeometry(QtCore.QRect(70, 60, 71, 20))
        self.campoMultiplicador.setObjectName("campoMultiplicador")
        self.campoMultiplicador.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[1-9][0-9]{4}"), self.campoMultiplicador))

        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(50, 60, 16, 16))
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(50, 90, 16, 16))
        self.label_8.setObjectName("label_8")

        self.campoTamanho = QtWidgets.QLineEdit(Form)
        self.campoTamanho.setGeometry(QtCore.QRect(70, 90, 71, 20))
        self.campoTamanho.setObjectName("campoTamanho")
        self.campoTamanho.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]{6}||[1][0]{6}"), self.campoTamanho))

        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(50, 120, 16, 16))
        self.label_9.setObjectName("label_9")

        self.campoPrimo = QtWidgets.QLineEdit(Form)
        self.campoPrimo.setGeometry(QtCore.QRect(70, 120, 71, 20))
        self.campoPrimo.setObjectName("campoPrimo")
        self.campoPrimo.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-1][0-2][0-7]||[0-9][0-9]"), self.campoPrimo))

        self.campoSemente = QtWidgets.QLineEdit(Form)
        self.campoSemente.setGeometry(QtCore.QRect(70, 30, 71, 20))
        self.campoSemente.setObjectName("campoSemente")
        self.campoSemente.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]{4}"), self.campoSemente))

        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(46, 30, 20, 20))
        self.label_10.setObjectName("label_10")

        self.retranslateUi(Form)

        self.pushButton.clicked.connect(self.campoPrimo.copy)
        self.pushButton.clicked.connect(self.campoTamanho.copy)
        self.pushButton.clicked.connect(self.campoMultiplicador.copy)
        self.pushButton.clicked.connect(self.campoSemente.copy)
        self.pushButton_2.clicked.connect(self.campoPrimo.clear)
        self.pushButton_2.clicked.connect(self.campoTamanho.clear)
        self.pushButton_2.clicked.connect(self.campoMultiplicador.clear)
        self.pushButton_2.clicked.connect(self.campoSemente.clear)

        self.pushButton.clicked.connect(self.verificaCampos)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Gerador1", "G_1"))
        self.pushButton.setText(_translate("Gerador1", "Gerar Valores"))
        self.pushButton_2.setText(_translate("Gerador1", "LIMPAR CAMPOS"))
        self.label_erro.setText(_translate("Gerador1", "Não é primo"))
        self.campoMultiplicador.setPlaceholderText(_translate("Gerador1", "Multiplicador"))
        self.label_7.setText(_translate("Gerador1", "a"))
        self.label_8.setText(_translate("Gerador1", "n"))
        self.campoTamanho.setPlaceholderText(_translate("Gerador1", "Tamanho"))
        self.label_9.setText(_translate("Gerador1", "p"))
        self.campoPrimo.setPlaceholderText(_translate("Gerador1", "Primo (2^p)-1"))
        self.campoSemente.setPlaceholderText(_translate("Gerador1", "Semente"))
        self.label_10.setText(_translate("Gerador1", "n0"))

    def executaGerador1(self):
        n0 = int(self.campoSemente.text())#semente
        a = int(self.campoMultiplicador.text())#fator multiplicador
        n = int(self.campoTamanho.text())#quantidade de valores a serem gerados
        p = int(self.campoPrimo.text())#numero primo
        m = (pow(2,p))-1 #numero de mersene
        resultado = [] #vetor para o geração dos valores

        # Cabecalho do Arquivo Texto
        arquivo = open("Gerador 1\CRIALEO.txt", "w")
        arquivo.write("\n\n***************************************************\n")
        arquivo.write("***************************************************\n")
        arquivo.write("GERADOR 1")
        arquivo.write("Semente: " + self.campoSemente.text()+"\n")
        arquivo.write("Multiplicador: " + self.campoMultiplicador.text()+"\n")
        arquivo.write("Tamanho: " + self.campoTamanho.text()+"\n")
        arquivo.write("Primo: " + self.campoPrimo.text()+"\n")
        arquivo.write("Mercene: " + str(m)+"\n")
        arquivo.write("***************************************************\n")
        arquivo.write("***************************************************\n\n")

        for i in range(n):#O looping funcinará até que seja satisfeita a quantidade n informada
            if i == 0:#inicializa o arquivo .txt
                resultado.append(n0)#Se estiver vazio atribui a primeira posição a semente
                arquivo.write(str(resultado[i])+"\n")#Escreve no arquivo .txt o valor armazenado no vetor
            else:
                resultado.append(((a * resultado[i - 1]) % m))#Caso o vetor já possua o valor da semente n0 realiza-se o cálculo da MCL Multiplicativa
                arquivo.write(str(resultado[i])+"\n")#escreve o ultimo valor atribuido ao vetor no arquivo .txt

        arquivo.close()

    def verificaPrimo(self):
        n = int(self.campoPrimo.text())
        mult = 0

        for count in range(2, n):#inicializa o contador em um range de 2 até n-ésimo valor informado
            if (n % count == 0):#verifica se o resto da divisão do valor informado n pelo contador cont  é zero
                mult += 1#incrementa a variável de controle mult se o resto da divisão for igual a zero
        if (mult != 0):#Se o resto da divisão for zero então ele não é primo
            self.label_erro.setVisible(True)
        else:#senão incrementar então o valor digitado é primo
            self.executaGerador1()
            self.label_erro.setVisible(False)

    def verificaCampos(self):
        if self.campoPrimo.text() and self.campoSemente.text() and self.campoTamanho.text() and self.campoMultiplicador.text():
            self.verificaPrimo()
        else:
            self.label_erro.setGeometry(QtCore.QRect(40, 10, 250, 16))
            self.label_erro.setText("Preencha todos os campos")
            self.label_erro.setStyleSheet('QLabel {color: red}')
            self.label_erro.setVisible(True)

class MenuPrincipal(QtWidgets.QWidget):
    switch_window_1 = QtCore.pyqtSignal()
    switch_window_2 = QtCore.pyqtSignal()
    switch_window_3 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
    
    def setupUi(self, Form):
        Form.setObjectName("MainWindow")
        Form.setFixedSize(210,296)

        self.botaoGeradorDEC = QtWidgets.QPushButton(Form)
        self.botaoGeradorDEC.setGeometry(QtCore.QRect(50, 80, 111, 23))
        self.botaoGeradorDEC.setObjectName("botaoGeradorDEC")

        self.botaoGerador1 = QtWidgets.QPushButton(Form)
        self.botaoGerador1.setGeometry(QtCore.QRect(50, 50, 111, 23))
        self.botaoGerador1.setObjectName("botaoGerador1")

        self.botaoMclMisto = QtWidgets.QPushButton(Form)
        self.botaoMclMisto.setGeometry(QtCore.QRect(50, 110, 111, 23))
        self.botaoMclMisto.setObjectName("botaoMclMisto")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 191, 20))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 170, 41, 16))

        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 210, 101, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 190, 91, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 250, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(20, 270, 121, 16))
        self.label_6.setObjectName("label_6")

        self.botaoGeradorDEC.clicked.connect(self.telaGeradorDEC)
        self.botaoGerador1.clicked.connect(self.telaGerador1)
        self.botaoMclMisto.clicked.connect(self.telaMclMisto)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def telaGeradorDEC(self):
        self.switch_window_1.emit()

    def telaGerador1(self):
        self.switch_window_2.emit()

    def telaMclMisto(self):
        self.switch_window_3.emit()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("MainWindow", "Menu"))
        self.botaoGeradorDEC.setText(_translate("MainWindow", "Gerador DEC"))
        self.botaoGerador1.setText(_translate("MainWindow", "Gerador 1"))
        self.botaoMclMisto.setText(_translate("MainWindow", "Gerador SAS"))
        self.label.setText(_translate("MainWindow", "MÉTODOS CONGRUENCIAIS LINEARES"))
        self.label_2.setText(_translate("MainWindow", "Alunos: "))
        self.label_3.setText(_translate("MainWindow", "Guilherme Camargo"))
        self.label_4.setText(_translate("MainWindow", "Oséias Magalhães"))
        self.label_5.setText(_translate("MainWindow", "Disciplina:"))
        self.label_6.setText(_translate("MainWindow", "Modelagem e Simulação"))


class Controller:

    def __init__(self):
        pass

    def show_menu(self):
        self.menu = MenuPrincipal()
        self.menu.switch_window_1.connect(self.show_mclGeradorDEC)
        self.menu.switch_window_2.connect(self.show_mclGerador1)
        self.menu.switch_window_3.connect(self.show_mclGeradorSAS)
        self.menu.show()

    def show_mclGerador1(self):
        self.gerador1 = Gerador1()
        self.gerador1.show()

    def show_mclGeradorDEC(self):
        self.geradorDEC = GeradorDEC()
        self.geradorDEC.show()

    def show_mclGeradorSAS(self):
        self.geradorSAS = GeradorSAS()
        self.geradorSAS.show()

def main():
    #app = QtWidgets.QApplication(sys.argv)
    controller = Controller()

    controller.show_menu()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()