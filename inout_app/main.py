import sys

import PyQt5.QtCore
import PyQt5.QtWidgets
import PyQt5.uic


class MainWindow(PyQt5.QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        PyQt5.uic.loadUi("forms/main.ui", self)
        self.btn_functions()
        self.show()

    def btn_functions(self):
        self.pushButton.clicked.connect(self.ready)
        self.pushButton_2.clicked.connect(self.clear_data)

    def ready(self):
        self.plainText2.setPlainText("")
        text = self.plainText1.toPlainText()
        if len(text) > 0:
            self.plainText2.setPlainText(text)
            self.infoLabel.setText("")
        else:
            self.infoLabel.setText("Введите что-нибудь:)")

    def clear_data(self):
        self.plainText2.setPlainText("")
        self.plainText1.setPlainText("")
        self.infoLabel.setText("Данные очищены!")


app = PyQt5.QtWidgets.QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())
