import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox, QMainWindow

from prog.Alphabet import decryptVigenere, encryptVigenere, decryptCaesar, encryptCaesar


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

        self.option2HLayout = QtWidgets.QHBoxLayout()
        self.labelKeyA = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelKeyA.setText("<h3>A: </h3>")
        self.keyLineA = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.labelKeyB = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelKeyB.setText("<h3>B: </h3>")
        self.keyLineB = QtWidgets.QLineEdit(self.horizontalLayoutWidget)

        self.solveButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.solveButton.setText("Решить")
        self.solveButton.setStatusTip("Посчитать НОД (A,B)")
        self.option2HLayout.addWidget(self.labelKeyA)
        self.option2HLayout.addWidget(self.keyLineA)
        self.option2HLayout.addWidget(self.labelKeyB)
        self.option2HLayout.addWidget(self.keyLineB)
        self.option2HLayout.addWidget(self.solveButton)
        self.solveButton.clicked.connect(self.Egcd)
        self.LeftVlLayout.addLayout(self.option2HLayout)

        self.label3Output = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label3Output.setText("<h3>Вывод результата:</h4>")
        self.text3Output = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.LeftVlLayout.addWidget(self.label3Output)
        self.LeftVlLayout.addWidget(self.text3Output)

        self.MainLayout.addLayout(self.LeftVlLayout)

        self.tabWidget.addTab(self.tab3, "РАЕ")

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
                          "* Шифр Цезаря\n* Шифр Виженера\n* Шифр гаммирования\n* Расширенный алгоритм Евклида")

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
    """

    def EncryptG(self):
        key = self.keyLine.text()
        key = key.upper()
        word = str(self.text2Input.toPlainText())
        #word = word.upper().replace(' ', '')

        from prog.Gamma import encryptGamma
        text= encryptGamma(word,key)
        self.text2Output.setPlainText(text)


    def DecryptG(self):
        key = self.keyLine.text()
        key = key.upper()
        word = str(self.text2Input.toPlainText())
        #word = word.upper().replace(' ', '')

        from prog.Gamma import decryptGamma
        text = decryptGamma(word,key)
        self.text2Output.setPlainText(text)

    def Egcd(self):
        A = int(self.keyLineA.text())
        B = int(self.keyLineB.text())

        from prog.EGCD import egcd
        num = str(egcd(A,B))
        self.text3Output.setPlainText("X, Y, НОД(A,B): "+num)




def run():
    app = QtWidgets.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())