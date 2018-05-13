import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox, QMainWindow


class Window(QMainWindow):
    # class MainWindow(object):
    def __init__(self):
        # def setupUi(self, Window):
        super(Window, self).__init__()
        self.setFixedSize(500, 400)
        self.setWindowTitle('Безопасность вычислительных систем')
        self.setWindowIcon(QIcon('icons/public.png'))

        self.init_Action()
        self.init_Content()
        self.init_StatusBar()
        self.init_Menu()
        self.set_Actions2Menu()
        self.set_Actions2StatusBar()
        self.set_Triggers2Actions()
        self.show()

    def init_Content(self):
        self.centralwidget = QtWidgets.QWidget(self)

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(5, 5, 490, 355))
        self.tabWidget.setStyleSheet("")

        """
        ########____ВКЛАДКА__1__
        self.tab1 = QtWidgets.QWidget()
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab1)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(5, 5, 475, 320))

        self.MainLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.MainLayout.setContentsMargins(0, 0, 0, 0)

        self.LeftVlLayout = QtWidgets.QVBoxLayout()

        self.option1HLayout = QtWidgets.QHBoxLayout()
        self.labelKey = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelKey.setText("<h3>Ключ: </h3>")
        self.keyLine = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.option1HLayout.addWidget(self.labelKey)
        self.option1HLayout.addWidget(self.keyLine)
        self.LeftVlLayout.addLayout(self.option1HLayout)

        self.label1Input = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label1Input.setText("<h3>Входной текст:</h3>")
        self.text1Input = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.LeftVlLayout.addWidget(self.label1Input)
        self.LeftVlLayout.addWidget(self.text1Input)

        self.buttonHLayout = QtWidgets.QHBoxLayout()
        self.encryptButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.encryptButton.setText("Зашифровать")
        self.encryptButton.setStatusTip("Зашифровать")
        self.decryptButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.decryptButton.setText("Расшифровать")
        self.decryptButton.setStatusTip("Расшифровать")
        self.buttonHLayout.addWidget(self.decryptButton)
        self.buttonHLayout.addWidget(self.encryptButton)
        self.decryptButton.clicked.connect(self.DecryptCV)
        self.encryptButton.clicked.connect(self.EncryptCV)

        self.LeftVlLayout.addLayout(self.buttonHLayout)
        self.label1Output = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label1Output.setText("<h3>Вывод результата:</h4>")
        self.text1Output = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.LeftVlLayout.addWidget(self.label1Output)
        self.LeftVlLayout.addWidget(self.text1Output)

        self.MainLayout.addLayout(self.LeftVlLayout)

        self.tabWidget.addTab(self.tab1, "Шифр Виженера и Шифр Цезаря")
        """
        """
        ########____ВКЛАДКА__2__
        self.tab2 = QtWidgets.QWidget()
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(5, 5, 475, 320))

        self.MainLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.MainLayout.setContentsMargins(0, 0, 0, 0)

        self.LeftVlLayout = QtWidgets.QVBoxLayout()

        self.option2HLayout = QtWidgets.QHBoxLayout()
        self.labelKey = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelKey.setText("<h3>Ключ: </h3>")
        self.keyLine = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        #self.generationButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        #self.generationButton.setText("Генерировать")
        #self.generationButton.setStatusTip("Генерировать")
        self.option2HLayout.addWidget(self.labelKey)
        self.option2HLayout.addWidget(self.keyLine)
        #self.option2HLayout.addWidget(self.generationButton)
        self.LeftVlLayout.addLayout(self.option2HLayout)

        self.label2Input = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label2Input.setText("<h3>Входной текст:</h3>")
        self.text2Input = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.LeftVlLayout.addWidget(self.label2Input)
        self.LeftVlLayout.addWidget(self.text2Input)

        self.buttonHLayout = QtWidgets.QHBoxLayout()
        self.encryptButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.encryptButton.setText("Зашифровать")
        self.encryptButton.setStatusTip("Зашифровать")
        self.decryptButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.decryptButton.setText("Расшифровать")
        self.decryptButton.setStatusTip("Расшифровать")
        self.buttonHLayout.addWidget(self.decryptButton)
        self.buttonHLayout.addWidget(self.encryptButton)
        self.decryptButton.clicked.connect(self.DecryptG)
        self.encryptButton.clicked.connect(self.EncryptG)

        self.LeftVlLayout.addLayout(self.buttonHLayout)
        self.label2Output = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label2Output.setText("<h3>Вывод результата:</h4>")
        self.text2Output = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.LeftVlLayout.addWidget(self.label2Output)
        self.LeftVlLayout.addWidget(self.text2Output)

        self.MainLayout.addLayout(self.LeftVlLayout)

        self.tabWidget.addTab(self.tab2, "Шифр Гаммирования")

        
        ########____ВКЛАДКА__3__
        self.tab3 = QtWidgets.QWidget()
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab3)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(5, 5, 475, 320))

        self.MainLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.MainLayout.setContentsMargins(0, 0, 0, 0)

        self.LeftVlLayout = QtWidgets.QVBoxLayout()

        self.option3HLayout = QtWidgets.QHBoxLayout()
        self.labelKeyA3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelKeyA3.setText("<h3>A: </h3>")
        self.keyLineA3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.labelKeyB3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelKeyB3.setText("<h3>B: </h3>")
        self.keyLineB3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)

        self.solveButton3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.solveButton3.setText("Решить")
        self.solveButton3.setStatusTip("Посчитать НОД (A,B)")
        self.option3HLayout.addWidget(self.labelKeyA3)
        self.option3HLayout.addWidget(self.keyLineA3)
        self.option3HLayout.addWidget(self.labelKeyB3)
        self.option3HLayout.addWidget(self.keyLineB3)
        self.option3HLayout.addWidget(self.solveButton3)
        self.solveButton3.clicked.connect(self.Egcd)
        self.LeftVlLayout.addLayout(self.option3HLayout)

        self.label3Output = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label3Output.setText("<h3>Вывод результата:</h4>")
        self.text3Output = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.LeftVlLayout.addWidget(self.label3Output)
        self.LeftVlLayout.addWidget(self.text3Output)

        self.MainLayout.addLayout(self.LeftVlLayout)

        self.tabWidget.addTab(self.tab3, "Расширенный алгоритм Евклида")

        ########____ВКЛАДКА__4__
        self.tab4 = QtWidgets.QWidget()
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab4)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(5, 5, 475, 320))

        self.MainLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.MainLayout.setContentsMargins(0, 0, 0, 0)

        self.LeftVlLayout = QtWidgets.QVBoxLayout()

        self.option4HLayout = QtWidgets.QHBoxLayout()
        self.labelKeyA4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelKeyA4.setText("<h3>a: </h3>")
        self.keyLineA4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.labelKeyB4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelKeyB4.setText("<h3>b: </h3>")
        self.keyLineB4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.labelKeyM4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelKeyM4.setText("<h3>mod: </h3>")
        self.keyLineM4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)

        self.solveButton4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.solveButton4.setText("Решить")
        self.solveButton4.setStatusTip("Возвести в степень")
        self.option4HLayout.addWidget(self.labelKeyA4)
        self.option4HLayout.addWidget(self.keyLineA4)
        self.option4HLayout.addWidget(self.labelKeyB4)
        self.option4HLayout.addWidget(self.keyLineB4)
        self.option4HLayout.addWidget(self.labelKeyM4)
        self.option4HLayout.addWidget(self.keyLineM4)
        self.option4HLayout.addWidget(self.solveButton4)
        self.solveButton4.clicked.connect(self.PowMod)
        self.LeftVlLayout.addLayout(self.option4HLayout)

        self.label4Output = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label4Output.setText("<h3>Вывод результата:</h4>")
        self.text4Output = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.LeftVlLayout.addWidget(self.label4Output)
        self.LeftVlLayout.addWidget(self.text4Output)

        self.MainLayout.addLayout(self.LeftVlLayout)

        self.tabWidget.addTab(self.tab4, "Быстрое возведение в степень")

        ########____ВКЛАДКА__5__
        self.tab5 = QtWidgets.QWidget()
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab5)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(5, 5, 475, 320))

        self.MainLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.MainLayout.setContentsMargins(0, 0, 0, 0)

        self.LeftVlLayout = QtWidgets.QVBoxLayout()

        self.option5HLayout = QtWidgets.QHBoxLayout()
        self.labelKeyA5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelKeyA5.setText("<h3>n: </h3>")
        self.keyLineA5 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)

        self.solveButton5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.solveButton5.setText("Решить")
        self.solveButton5.setStatusTip("Проверить")
        self.option5HLayout.addWidget(self.labelKeyA5)
        self.option5HLayout.addWidget(self.keyLineA5)
        self.option5HLayout.addWidget(self.solveButton5)
        self.solveButton5.clicked.connect(self.MR)
        self.LeftVlLayout.addLayout(self.option5HLayout)

        self.label5Output = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label5Output.setText("<h3>Вывод результата:</h4>")
        self.text5Output = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.LeftVlLayout.addWidget(self.label5Output)
        self.LeftVlLayout.addWidget(self.text5Output)

        self.MainLayout.addLayout(self.LeftVlLayout)

        self.tabWidget.addTab(self.tab5, "Миллер-Рабин")
        
        """
        ########____ВКЛАДКА__6__
        self.tab6 = QtWidgets.QWidget()
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab6)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(5, 5, 475, 320))

        self.MainLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.MainLayout.setContentsMargins(0, 0, 0, 0)

        self.LeftVlLayout = QtWidgets.QVBoxLayout()

        self.option6HLayout = QtWidgets.QHBoxLayout()
        self.option61HLayout = QtWidgets.QHBoxLayout()
        self.option62HLayout = QtWidgets.QHBoxLayout()
        self.labelKeyA6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelKeyA6.setText("<h3>Исходное: </h3>")
        self.keyLineA6 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.labelKeyB6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelKeyB6.setText("<h3>Зашифрованное: </h3>")
        self.keyLineB6 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)

        self.labelKeyN6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelKeyN6.setText("<h3>N: </h3>")
        self.keyLineN6 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.labelKeyE6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelKeyE6.setText("<h3>E: </h3>")
        self.keyLineE6 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.labelKeyD6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelKeyD6.setText("<h3>D: </h3>")
        self.keyLineD6 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)


        self.enButton6 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.enButton6.setText("Зашифровать")
        self.enButton6.setStatusTip("Зашифровать")
        self.decButton6 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.decButton6.setText("Расшифровать")
        self.decButton6.setStatusTip("Расшифровать")

        self.option6HLayout.addWidget(self.labelKeyA6)
        self.option6HLayout.addWidget(self.keyLineA6)
        self.option6HLayout.addWidget(self.enButton6)
        self.option61HLayout.addWidget(self.labelKeyB6)
        self.option61HLayout.addWidget(self.keyLineB6)
        self.option61HLayout.addWidget(self.decButton6)
        self.option62HLayout.addWidget(self.labelKeyN6)
        self.option62HLayout.addWidget(self.keyLineN6)
        self.option62HLayout.addWidget(self.labelKeyE6)
        self.option62HLayout.addWidget(self.keyLineE6)
        self.option62HLayout.addWidget(self.labelKeyD6)
        self.option62HLayout.addWidget(self.keyLineD6)

        self.enButton6.clicked.connect(self.RSAe)
        self.decButton6.clicked.connect(self.RSAd)
        self.LeftVlLayout.addLayout(self.option6HLayout)
        self.LeftVlLayout.addLayout(self.option61HLayout)
        self.LeftVlLayout.addLayout(self.option62HLayout)

        self.label6Output = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label6Output.setText("<h3>Вывод результата:</h4>")
        self.text6Output = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.LeftVlLayout.addWidget(self.label6Output)
        self.LeftVlLayout.addWidget(self.text6Output)

        self.MainLayout.addLayout(self.LeftVlLayout)

        self.tabWidget.addTab(self.tab6, "RSA")

        self.setCentralWidget(self.centralwidget)
        self.tabWidget.setCurrentIndex(0)

    def init_StatusBar(self):
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setSizeGripEnabled(True)
        self.setStatusBar(self.statusbar)

    def init_Action(self):
        self.ExitAction = QtWidgets.QAction(QIcon('icons/exit.png'), "Выход", self)
        self.HelpAction = QtWidgets.QAction(QIcon('icons/question.png'), "Помощь", self)
        self.AboutAction = QtWidgets.QAction(QIcon('icons/about.png'), "О программе", self)

        self.ExitAction.setShortcut('Ctrl+Q')
        self.HelpAction.setShortcut('Ctrl+H')
        self.AboutAction.setShortcut('Ctrl+I')

    def set_Actions2StatusBar(self):

        self.ExitAction.setStatusTip('Выход')
        self.HelpAction.setStatusTip('Помощь')
        self.AboutAction.setStatusTip('О программе')

    def set_Triggers2Actions(self):
        self.ExitAction.triggered.connect(self.close)
        self.HelpAction.triggered.connect(self.help)
        self.AboutAction.triggered.connect(self.about)

    def init_Menu(self):
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 20))
        self.fileMenu = QtWidgets.QMenu(self.menubar)
        self.helpMenu = QtWidgets.QMenu(self.menubar)
        self.fileMenu.setTitle("Файл ")
        self.helpMenu.setTitle("Справка")
        self.menubar.addAction(self.fileMenu.menuAction())
        self.menubar.addAction(self.helpMenu.menuAction())
        self.setMenuBar(self.menubar)

    def set_Actions2Menu(self):

        self.fileMenu.addAction(self.ExitAction)
        self.helpMenu.addAction(self.HelpAction)
        self.helpMenu.addAction(self.AboutAction)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Выход', "Вы действительно хотите покинуть программу?",
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:

            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def about(self):
        QMessageBox.about(self, 'О программе',
                          "* Шифр Цезаря\n* Шифр Виженера\n* Шифр гаммирования\n* Расширенный алгоритм Евклида\n* Быстрое возведение в степень\n"
                          "* Тест Миллера-Рабина\n* RSA\n* ")

    def help(self):
        QMessageBox.information(self, 'Помощь', "??")

    """
    def EncryptCV(self):
        key = self.keyLine.text()
        key = key.upper()
        word = str(self.textInput.toPlainText())
        word = word.upper().replace('', '')
        if key.isalpha():
            text = encryptVigenere(key, word)
        elif key.isdigit():
            text = encryptCaesar(key, word)
        self.textOutput.setPlainText(text)

    def DecryptCV(self):
        key = self.keyLine.text()
        key = key.upper()
        word = str(self.textInput.toPlainText())
        word = word.upper().replace(' ', '')
        if key.isalpha():
            text = decryptVigenere(key, word)
        elif key.isdigit():
            text = decryptCaesar(key, word)
        self.textOutput.setPlainText(text)
    

    def EncryptG(self):
        key = self.keyLine.text()
        key = key.upper()
        word = str(self.text2Input.toPlainText())

        from prog.Gamma import encryptGamma
        text = encryptGamma(word, key)
        self.text2Output.setPlainText(text)

    def DecryptG(self):
        key = self.keyLine.text()
        key = key.upper()
        word = str(self.text2Input.toPlainText())

        from prog.Gamma import decryptGamma
        text = decryptGamma(word, key)
        self.text2Output.setPlainText(text)
    """

    def Egcd(self):
        A = int(self.keyLineA3.text())
        B = int(self.keyLineB3.text())

        from prog.EGCD import egcd
        num = str(egcd(A, B))
        self.text3Output.setPlainText("НОД(A,B), X, Y: " + num)

    def PowMod(self):
        a = int(self.keyLineA4.text())
        b = int(self.keyLineB4.text())
        n = int(self.keyLineM4.text())

        from prog.PowMod import powmod
        bbin, ar, res = powmod(a, b, n)
        self.text4Output.setPlainText(
            "b:  " + str(bbin) + "\n" + "ar: " + str(ar) + "\n\n" + str(a) + "^" + str(b) + " mod " + str(
                n) + " = " + str(res))

    def MR(self):
        a = int(self.keyLineA5.text())
        from prog.MRPT import MillerRabin
        result = MillerRabin(a)
        self.text5Output.setPlainText(str(result))

    def RSAe(self):
        m = self.keyLineA6.text()

        from prog.RSA import encoding
        result, e, n, d = encoding(m)
        print(result, type(result))
        self.keyLineB6.setText(str(result))
        self.keyLineN6.setText(str(n))
        self.keyLineE6.setText(str(e))
        self.keyLineD6.setText(str(d))

    def RSAd(self):
        m_cod = self.keyLineB6.text()
        n=int(self.keyLineN6.text())
        d=int(self.keyLineD6.text())

        from prog.RSA import decoding
        result = decoding(m_cod, n, d)
        self.text6Output.setPlainText(str(result))


def run():
    app = QtWidgets.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())
