import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt, QLocale, QDateTime
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget):      #DigitalClock prende dalla classe padre QWidget
    def __init__(self):
        super().__init__()
        self.time_label = QLabel( self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(850,450,400,100)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        self.time_label.setStyleSheet("font-size: 150px;"
                                       "color: rgb(64, 242, 5)")
        self.setStyleSheet("background-color: black;")

        font_id = QFontDatabase.addApplicationFont("DS-DIGIT.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 150)
        self.time_label.setFont(my_font)

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()


    def update_time(self):
        QLocale.setDefault(QLocale(QLocale.English, QLocale.UnitedStates))
        formatted_time = QDateTime.currentDateTime().toString("hh:mm:ss ap") #AP, A After Meridium , P Post Meridium {NON CAPISCO PERCHE NON FUNZIONA}
        self.time_label.setText(formatted_time)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
