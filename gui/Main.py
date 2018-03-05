import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QToolBar, QFileDialog, QMessageBox, QMainWindow

from PBDD import BDD
from prog.Alphabet import decryptVigenere, encryptVigenere, decryptCaesar, encryptCaesar
from prog.lfsr import LFSR


class Window(QMainWindow):
    # class MainWindow(object):
    def __init__(self):
        # def setupUi(self, Window):
        super(Window, self).__init__()
        self.setFixedSize(500, 400)
        self.setWindowTitle('Шифры')
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

        ########____ВКЛАДКА____
        self.tab2 = QtWidgets.QWidget()
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab2)
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

        self.labelInput = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelInput.setText("<h3>Входной текст:</h3>")
        self.textInput = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.LeftVlLayout.addWidget(self.labelInput)
        self.LeftVlLayout.addWidget(self.textInput)

        self.buttonHLayout = QtWidgets.QHBoxLayout()
        self.encryptButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.encryptButton.setText("Зашифровать")
        self.encryptButton.setStatusTip("Зашифровать")
        self.decryptButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.decryptButton.setText("Расшифровать")
        self.decryptButton.setStatusTip("Расшифровать")
        self.buttonHLayout.addWidget(self.decryptButton)
        self.buttonHLayout.addWidget(self.encryptButton)
        self.decryptButton.clicked.connect(self.Decrypt)
        self.encryptButton.clicked.connect(self.Encrypt)

        self.LeftVlLayout.addLayout(self.buttonHLayout)
        self.labelOutput = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelOutput.setText("<h3>Вывод результата:</h4>")
        self.textOutput = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.LeftVlLayout.addWidget(self.labelOutput)
        self.LeftVlLayout.addWidget(self.textOutput)

        self.MainLayout.addLayout(self.LeftVlLayout)

        self.tabWidget.addTab(self.tab2, "Шифр Виженера и Шифр Цезаря")

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
        reply = QMessageBox.question(self, 'Выход', "Вы действительно хотите нас покинуть?",
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
                          "Шифры простой замены:\n* Шифр Цезаря\n* Шифр Виженера")

    def help(self):
        QMessageBox.information(self, 'Помощь', "??")

    def Encrypt(self):
        key = self.keyLine.text()
        key = key.upper()
        word = str(self.textInput.toPlainText())
        word = word.upper().replace('', '')
        if key.isalpha():
            text = encryptVigenere(key, word)
        elif key.isdigit():
            text = encryptCaesar(key, word)
        self.textOutput.setPlainText(text)

    def Decrypt(self):
        key = self.keyLine.text()
        key = key.upper()
        word = str(self.textInput.toPlainText())
        word = word.upper().replace(' ', '')
        if key.isalpha():
            text = decryptVigenere(key, word)
        elif key.isdigit():
            text = decryptCaesar(key, word)
        self.textOutput.setPlainText(text)


def run():
    app = QtWidgets.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())