'''Задание 1 используя PyQT написать оконное приложение. В котором будет одна кнопка (“выход”).
То есть при запуске программы должно открываться окно с одной кнопкой при нажатии которой окно должно закрываться
а приложение останавливать работу.'''


import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Выход")
        button.setCheckable(True)
        button.clicked.connect(self.myexit)

        # Устанавливаем центральный виджет Window.
        self.setCentralWidget(button)

    def myexit(self):
        exit(0)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()