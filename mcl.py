import sys
from PyQt5 import QtCore, QtGui, QtWidgets

app = QtWidgets.QApplication(sys.argv)


class MetodoMisto(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("MetodoMisto")
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
        self.campoMultiplicador.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[1-9]{4}"), self.campoMultiplicador))

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

        self.label_primo = QtWidgets.QLabel(Form)
        self.label_primo.setGeometry(QtCore.QRect(50, 150, 16, 16))
        self.label_primo.setObjectName("label_primo")

        self.campoPrimo = QtWidgets.QLineEdit(Form)
        self.campoPrimo.setGeometry(QtCore.QRect(70, 150, 71, 20))
        self.campoPrimo.setObjectName("campoPrimo_2")
        self.campoPrimo.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-1][0-2][0-7]||[0-9][0-9]"), self.campoPrimo))

        self.retranslateUi(Form)
        self.botaoGerarValores.clicked.connect(self.campoConstante.copy)
        self.botaoGerarValores.clicked.connect(self.campoMultiplicador.copy)
        self.botaoGerarValores.clicked.connect(self.campoSemente.copy)
        self.botaoLimparCampos.clicked.connect(self.campoConstante.clear)
        self.botaoLimparCampos.clicked.connect(self.campoMultiplicador.clear)
        self.botaoLimparCampos.clicked.connect(self.campoSemente.clear)
        self.botaoLimparCampos.clicked.connect(self.campoTamanho.clear)
        self.botaoGerarValores.clicked.connect(self.campoTamanho.copy)
        self.botaoGerarValores.clicked.connect(self.campoPrimo.copy)
        self.botaoLimparCampos.clicked.connect(self.campoPrimo.clear)
        self.botaoGerarValores.clicked.connect(self.verificaCampos)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("MetodoMisto", "Misto"))
        self.botaoGerarValores.setText(_translate("MetodoMisto", "Gerar Valores"))
        self.botaoLimparCampos.setText(_translate("MetodoMisto", "LIMPAR CAMPOS"))
        self.campoMultiplicador.setPlaceholderText(_translate("MetodoMisto", "Multiplicador"))
        self.label_multiplicador.setText(_translate("MetodoMisto", "a"))
        self.label_tamanho.setText(_translate("MetodoMisto", "n"))
        self.campoTamanho.setPlaceholderText(_translate("MetodoMisto", "Tamanho"))
        self.label_constante.setText(_translate("MetodoMisto", "c"))
        self.campoConstante.setPlaceholderText(_translate("MetodoMisto", "Constante"))
        self.campoSemente.setPlaceholderText(_translate("MetodoMisto", "Semente"))
        self.label_semente.setText(_translate("MetodoMisto", "n0"))
        self.label_primo.setText(_translate("MetodoMisto", "p"))
        self.campoPrimo.setPlaceholderText(_translate("MetodoMisto", "Primo"))

    def verificaCampos(self):
        if self.campoPrimo.text() and self.campoSemente.text() and self.campoTamanho.text() and self.campoMultiplicador.text() and self.campoConstante:
            self.verificaPrimo()
        else:
            self.label_erro.setGeometry(QtCore.QRect(40, 10, 250, 16))
            self.label_erro.setText("Preencha todos os campos")
            self.label_erro.setStyleSheet('QLabel {color: red}')
            self.label_erro.setVisible(True)

    def verificaPrimo(self):
        n = int(self.campoPrimo.text())
        mult = 0

        for count in range(2, n):#inicializa o contador em um range de 2 até n-ésimo valor informado
            if (n % count == 0):#verifica se o resto da divisão do valor informado n pelo contador cont  é zero
                mult += 1#incrementa a variável de controle mult se o resto da divisão for igual a zero
        if (mult != 0):#Se o resto da divisão for zero então ele não é primo
            self.label_erro.setVisible(True)
        else:#senão incrementar então o valor digitado é primo
            self.executaMetodoMisto()
            self.label_erro.setVisible(False)

    def executaMetodoMisto(self):
        n0 = int(self.campoSemente.text())#semente
        a = int(self.campoMultiplicador.text())#fator multiplicador inteiro positivo > 0
        n = int(self.campoTamanho.text())#quantidade de valores a serem gerados
        c = int(self.campoConstante.text())#constante inteira positiva > 0
        p = int(self.campoPrimo.text())#numero primo
        m = (pow(2,p))-1#numero de mersene
        resultado = []#vetor para o geração dos valores

        # Cabecalho do Arquivo Texto
        arquivo = open("Metodo Misto\ResultadoMisto.txt", "w")
        arquivo.write("\n\n***************************************************\n")
        arquivo.write("***************************************************\n")
        arquivo.write("Semente: " + self.campoSemente.text()+"\n")
        arquivo.write("Multiplicador: " + self.campoMultiplicador.text()+"\n")
        arquivo.write("Tamanho: " + self.campoTamanho.text()+"\n")
        arquivo.write("Constante: " + self.campoConstante.text() + "\n")
        arquivo.write("Primo: " + self.campoPrimo.text()+"\n")
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

class MetodoAditivo(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)


    def setupUi(self, Form):
        Form.setObjectName("Método Aditivo")
        Form.setGeometry(QtCore.QRect(355, 216, 210, 296))
        Form.setFixedSize(210, 296)

        self.botaoGerarValores = QtWidgets.QPushButton(Form)
        self.botaoGerarValores.setGeometry(QtCore.QRect(40, 160, 111, 23))
        self.botaoGerarValores.setObjectName("botaoGerarValores")

        self.botaoLimpar = QtWidgets.QPushButton(Form)
        self.botaoLimpar.setGeometry(QtCore.QRect(40, 210, 111, 23))
        self.botaoLimpar.setObjectName("botaoLimpar")

        self.campoInteiroP = QtWidgets.QLineEdit(Form)
        self.campoInteiroP.setGeometry(QtCore.QRect(70, 90, 71, 20))
        self.campoInteiroP.setObjectName("campoInteiroP")
        self.campoInteiroP.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]{4}"), self.campoInteiroP))

        self.label_erro = QtWidgets.QLabel(Form)
        self.label_erro.setGeometry(QtCore.QRect(148, 120, 60, 16))
        self.label_erro.setVisible(False)

        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(50, 90, 16, 16))
        self.label_7.setObjectName("label_7")

        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(50, 120, 16, 16))
        self.label_9.setObjectName("label_9")

        self.campoTamanho = QtWidgets.QLineEdit(Form)
        self.campoTamanho.setGeometry(QtCore.QRect(70, 60, 71, 20))
        self.campoTamanho.setObjectName("campoTamanho")
        self.campoTamanho.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]{6}||[1][0]{6}"), self.campoTamanho))

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

        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(46, 60, 20, 20))
        self.label_11.setObjectName("label_11")

        self.retranslateUi(Form)
        self.botaoGerarValores.clicked.connect(self.campoPrimo.copy)
        self.botaoGerarValores.clicked.connect(self.campoInteiroP.copy)
        self.botaoGerarValores.clicked.connect(self.campoSemente.copy)
        self.botaoGerarValores.clicked.connect(self.campoTamanho.copy)

        self.botaoLimpar.clicked.connect(self.campoPrimo.clear)
        self.botaoLimpar.clicked.connect(self.campoInteiroP.clear)
        self.botaoLimpar.clicked.connect(self.campoSemente.clear)
        self.botaoLimpar.clicked.connect(self.campoTamanho.clear)
        self.botaoGerarValores.clicked.connect(self.verificaCampos)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Aditivo"))
        self.botaoGerarValores.setText(_translate("Form", "Gerar Valores"))
        self.botaoLimpar.setText(_translate("Form", "LIMPAR CAMPOS"))
        self.campoInteiroP.setPlaceholderText(_translate("Form", "Inteiro"))
        self.label_erro.setText(_translate("MetodoAditivo", "Não é primo"))
        self.label_7.setText(_translate("Form", "k"))
        self.label_9.setText(_translate("Form", "p"))
        self.campoTamanho.setPlaceholderText(_translate("Form", "Tamanho"))
        self.campoPrimo.setPlaceholderText(_translate("Form", "Primo"))
        self.campoSemente.setPlaceholderText(_translate("Form", "Semente"))
        self.label_10.setText(_translate("Form", "n0"))
        self.label_11.setText(_translate("Form", "n"))

    def verificaPrimo(self):
        n = int(self.campoPrimo.text())
        mult = 0

        for count in range(2, n):#inicializa o contador em um range de 2 até n-ésimo valor informado
            if (n % count == 0):#verifica se o resto da divisão do valor informado n pelo contador cont  é zero
                mult += 1#incrementa a variável de controle mult se o resto da divisão for igual a zero
        if (mult != 0):#Se o resto da divisão for zero então ele não é primo
            self.label_erro.setVisible(True)
        else:#senão incrementar então o valor digitado é primo
            self.executaMetodoAditivo()
            self.label_erro.setVisible(False)


    def executaMetodoAditivo(self):
        n0 = int(self.campoSemente.text())#semente
        k = int(self.campoInteiroP.text())#inteiro positivo
        p = int(self.campoPrimo.text())#numero primo
        n = int(self.campoTamanho.text())#Quantidade de valores a serem gerados
        m = (pow(2, p)) - 1#valor de mersene
        resultado = []  # vetor para o geração dos valores

        #Cabecalho do Arquivo Texto
        arquivo = open("Metodo Aditivo\ResultadoAdt.txt", "w")
        arquivo.write("\n\n***************************************************\n")
        arquivo.write("***************************************************\n")
        arquivo.write("Semente n0: " + self.campoSemente.text() + "\n")
        arquivo.write("Inteiro Positivo k: " + self.campoInteiroP.text() + "\n")
        arquivo.write("Tamanho n: " + self.campoTamanho.text() + "\n")
        arquivo.write("Primo p: " + self.campoPrimo.text() + "\n")
        arquivo.write("Mercene m: " + str(m) + "\n")
        arquivo.write("***************************************************\n")
        arquivo.write("***************************************************\n\n")

        for i in range(n):
            if i == 0:#verifica se o vetor está vazio
                resultado.append(n0)#insere a semente n0
                arquivo.write(str(resultado[i]) + "\n")#escreve no arquivo .txt
            else:
                if i >= k:#verifica se o indice i é maior ou igual a k para evitar o conflito de casa vazia
                    resultado.append((resultado[i-1] + resultado[i-k]) % m)#atribui ao vetor o resultado do calculo para MCL Aditiva
                    arquivo.write(str(resultado[i]) + "\n")#Escreve o valor armazenado no arquivo .txt
                else:
                    resultado.append(n0)#caso o indice seja menor que o inteiro k atribui para as casas vazias o mesmo valor semente n0

        arquivo.close()

    def verificaCampos(self):
        if self.campoPrimo.text() and self.campoSemente.text() and self.campoTamanho.text() and self.campoInteiroP.text():
            self.verificaPrimo()
        else:
            self.label_erro.setGeometry(QtCore.QRect(40, 10, 250, 16))
            self.label_erro.setText("Preencha todos os campos")
            self.label_erro.setStyleSheet('QLabel {color: red}')
            self.label_erro.setVisible(True)

class MetodoMultiplicativo(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Form):

        Form.setObjectName("MetodoMultiplicativo")
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
        self.campoMultiplicador.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]{4}"), self.campoMultiplicador))

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
        Form.setWindowTitle(_translate("MetodoMultiplicativo", "Multiplicativo"))
        self.pushButton.setText(_translate("MetodoMultiplicativo", "Gerar Valores"))
        self.pushButton_2.setText(_translate("MetodoMultiplicativo", "LIMPAR CAMPOS"))
        self.label_erro.setText(_translate("MetodoMultiplicativo", "Não é primo"))
        self.campoMultiplicador.setPlaceholderText(_translate("MetodoMultiplicativo", "Multiplicador"))
        self.label_7.setText(_translate("MetodoMultiplicativo", "a"))
        self.label_8.setText(_translate("MetodoMultiplicativo", "n"))
        self.campoTamanho.setPlaceholderText(_translate("MetodoMultiplicativo", "Tamanho"))
        self.label_9.setText(_translate("MetodoMultiplicativo", "p"))
        self.campoPrimo.setPlaceholderText(_translate("MetodoMultiplicativo", "Primo"))
        self.campoSemente.setPlaceholderText(_translate("MetodoMultiplicativo", "Semente"))
        self.label_10.setText(_translate("MetodoMultiplicativo", "n0"))

    def executaMetodoMultiplicativo(self):
        n0 = int(self.campoSemente.text())#semente
        a = int(self.campoMultiplicador.text())#fator multiplicador
        n = int(self.campoTamanho.text())#quantidade de valores a serem gerados
        p = int(self.campoPrimo.text())#numero primo
        m = (pow(2,p))-1#numero de mersene
        resultado = []#vetor para o geração dos valores

        # Cabecalho do Arquivo Texto
        arquivo = open("Metodo Multiplicativo\ResultadoMult.txt", "w")
        arquivo.write("\n\n***************************************************\n")
        arquivo.write("***************************************************\n")
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
            self.executaMetodoMultiplicativo()
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

        self.botaoMclAditivo = QtWidgets.QPushButton(Form)
        self.botaoMclAditivo.setGeometry(QtCore.QRect(50, 50, 111, 23))
        self.botaoMclAditivo.setObjectName("botaoMclAditivo")

        self.botaoMclMultiplicativo = QtWidgets.QPushButton(Form)
        self.botaoMclMultiplicativo.setGeometry(QtCore.QRect(50, 80, 111, 23))
        self.botaoMclMultiplicativo.setObjectName("botaoMclMultiplicativo")

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

        self.botaoMclAditivo.clicked.connect(self.telaMclAditivo)
        self.botaoMclMultiplicativo.clicked.connect(self.telaMclMultiplicativo)
        self.botaoMclMisto.clicked.connect(self.telaMclMisto)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def telaMclAditivo(self):
        self.switch_window_1.emit()

    def telaMclMultiplicativo(self):
        self.switch_window_2.emit()

    def telaMclMisto(self):
        self.switch_window_3.emit()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("MainWindow", "Menu"))
        self.botaoMclAditivo.setText(_translate("MainWindow", "MCL - Aditivo"))
        self.botaoMclMultiplicativo.setText(_translate("MainWindow", "MCL - Multiplicativo"))
        self.botaoMclMisto.setText(_translate("MainWindow", "MCL - Misto"))
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
        self.menu.switch_window_1.connect(self.show_mclAditivo)
        self.menu.switch_window_2.connect(self.show_mclMultiplicativo)
        self.menu.switch_window_3.connect(self.show_mclMisto)
        self.menu.show()

    def show_mclMultiplicativo(self):
        self.multiplicativo = MetodoMultiplicativo()
        self.multiplicativo.show()

    def show_mclAditivo(self):
        self.aditivo = MetodoAditivo()
        self.aditivo.show()

    def show_mclMisto(self):
        self.misto = MetodoMisto()
        self.misto.show()

def main():
    #app = QtWidgets.QApplication(sys.argv)
    controller = Controller()

    controller.show_menu()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()