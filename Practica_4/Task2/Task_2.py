'''Задание 2 используя PyQT написать оконное приложение. состоящее из 2х окон. При запуске приложения открывается первое
окно с двумя кнопками (открыть второе окно и выход), при нажатии на “открыть второе окно” первое окно должно быть закрыто/скрыто,
 а второе открыто. Во втором окне также 2 кнопки (открыть первое окно и выход). При нажатии на “открыть первое окно” второе окно должно
 быть скрыто/закрыто, а первое открыто. При нажатии кнопки выход, не зависимо от окна , программа должна прекращать работу '''

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        button = QPushButton("Выход")
        button2 = QPushButton("Открыть второе окно")
        button2.setCheckable(True)
        button.setCheckable(True)
        button2.clicked.connect(self.myexit())
        button.clicked.connect(self.myexit)

        # Устанавливаем центральный виджет Window.
        self.setCentralWidget(button2)

    def myexit(self):
        exit(0)

def application():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

