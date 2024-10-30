import re
import sys

import bcrypt
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLineEdit,
                             QPushButton, QLabel, QMessageBox)

users_db = {}


def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'

    if re.match(pattern, password) is None:
        return False

    return True


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Вход")

        layout = QVBoxLayout()

        self.login_input = QLineEdit(self)
        self.login_input.setPlaceholderText("Логин")
        layout.addWidget(self.login_input)

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Пароль")
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        self.login_button = QPushButton("Войти", self)
        self.login_button.clicked.connect(self.login)
        layout.addWidget(self.login_button)

        self.register_button = QPushButton("Зарегистрироваться", self)
        self.register_button.clicked.connect(self.open_register_window)
        layout.addWidget(self.register_button)

        self.setLayout(layout)

    def login(self):
        username = self.login_input.text()
        password = self.password_input.text().encode("utf-8")

        if username in users_db:
            hashed = users_db[username]
            if bcrypt.checkpw(password, hashed):
                self.open_image_window()
            else:
                QMessageBox.warning(self, "Ошибка", "Неверный пароль!")
        else:
            QMessageBox.warning(self, "Ошибка", "Пользователь не найден!")

    def open_register_window(self):
        self.register_window = RegisterWindow()
        self.register_window.show()

    def open_image_window(self):
        self.image_window = ImageWindow()
        self.image_window.show()
        self.close()


class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Регистрация")

        layout = QVBoxLayout()

        self.login_input = QLineEdit(self)
        self.login_input.setPlaceholderText("Логин")
        layout.addWidget(self.login_input)

        self.password_input1 = QLineEdit(self)
        self.password_input1.setPlaceholderText("Пароль")
        self.password_input1.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input1)

        self.password_input2 = QLineEdit(self)
        self.password_input2.setPlaceholderText("Подтвердите пароль")
        self.password_input2.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input2)

        self.register_button = QPushButton("Готово", self)
        self.register_button.clicked.connect(self.register)
        layout.addWidget(self.register_button)

        self.setLayout(layout)

    def register(self):
        username = self.login_input.text()
        password1 = self.password_input1.text().encode("utf-8")
        password2 = self.password_input2.text().encode("utf-8")

        if password1 != password2:
            QMessageBox.warning(self, "Ошибка", "Пароли не совпадают!")
            return

        if not validate_password(password1):
            QMessageBox.warning(self, "Ошибка", "Пароль слишком легкий!")
            return

        if username in users_db:
            QMessageBox.warning(self, "Ошибка", "Пользователь уже существует!")
            return

        hashed = bcrypt.hashpw(password1, bcrypt.gensalt())
        users_db[username] = hashed

        QMessageBox.information(self, "Успех", "Пользователь зарегистрирован!")
        self.open_image_window()

    def open_image_window(self):
        self.image_window = ImageWindow()
        self.image_window.show()
        self.close()


class ImageWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Тут другое окошечко")

        layout = QVBoxLayout()

        label = QLabel("Добро пожаловать! Здесь будет какая-нибудь информация в будущем.")
        layout.addWidget(label)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
