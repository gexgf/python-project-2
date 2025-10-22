from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLabel, QLineEdit
from PySide6.QtGui import QCloseEvent, QPixmap

class LoginWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.login_line_edit = None

        self.setup()

    def setup(self):
        width = 400

        pix_label = QLabel(self)
        pixmap = QPixmap("D:\\DONK.png").scaled(150,150)
        pix_label.setPixmap(pixmap)
        pix_label.move((width - 150) /2, 120)

        login_line_edit = QLineEdit("Login", self)
        login_line_edit.setFixedWidth(200)
        login_line_edit.move((width - 250) /2, 350)

        pass_line_edit = QLineEdit("Password", self)
        pass_line_edit.setFixedWidth(200)
        pass_line_edit.move((width - 250) / 2, 380)

        login_btn = QPushButton('LOGUJ', self)
        login_btn.move((width - 250) / 2, 410)

        quit_btn = QPushButton('Quit', self)
        quit_btn.move(320, 570)


        login_btn.clicked.connect(self.submit)
        quit_btn.clicked.connect(QApplication.instance().quit)

        self.setFixedSize(width, 600)
        self.setWindowTitle("Login Window")

        self.show()

    def submit(self):
        print(self.login_line_edit.text())

    def closeEvent(self, event: QCloseEvent):
        should_close = QMessageBox.question(self, 'Close App', 'Do you want to close?',
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if should_close == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()





if __name__ == "__main__":
    app = QApplication([])

    login_window = LoginWindow()

    app.exec()