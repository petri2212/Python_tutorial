#433dfcfc75fcfe59d67f0146fa66e297

import sys
import requests  #for the requests do to an api
from PyQt5.QtWidgets import QApplication, QWidget,QLabel, QLineEdit, QPushButton, QVBoxLayout

from PyQt5.QtCore import Qt #for the alling

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app= WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())