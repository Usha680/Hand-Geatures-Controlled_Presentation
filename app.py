import sys
import subprocess
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QVBoxLayout
)
from PyQt5.QtGui import QIcon


class GestureApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle(
            "Hand Gesture Controlled Presentation"
        )

        #self.setWindowIcon(QIcon("icon.png"))

        self.startButton = QPushButton(
            "Start Presentation",
            self
        )

        self.startButton.clicked.connect(
            self.startPresentation
        )

        layout = QVBoxLayout()

        layout.addWidget(self.startButton)

        self.setLayout(layout)

        self.setGeometry(
            300,
            300,
            350,
            150
        )

    def startPresentation(self):

        subprocess.Popen(
            ["python", "main.py"]
        )


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = GestureApp()

    window.show()

    sys.exit(app.exec_())