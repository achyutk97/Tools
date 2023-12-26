import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import config

app = QtWidgets.QApplication(sys.argv)

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(" ")
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()

        self.setWindowOpacity(0.3)

        QtWidgets.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        print("Capture the screen...")

        self.showFullScreen()

    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        qp.setPen(QtGui.QPen(QtGui.QColor("black"), 3))
        qp.setBrush(QtGui.QColor(128, 128, 255, 128))
        qp.drawRect(QtCore.QRect(self.begin, self.end))

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.begin = event.pos()
        self.end = self.begin
        self.update()

    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)
        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        self.close()
        QtCore.QTimer.singleShot(1000, self.screenshot)

    def screenshot(self):
        global app
        screen = QtGui.QGuiApplication.primaryScreen()
        window = self.windowHandle()
        if window is not None:
            screen = window.screen()
        if screen is None:
            print("failed")
            return

        original_pixmap = screen.grabWindow(0)
        output_pixmap = original_pixmap.copy(
            QtCore.QRect(self.begin, self.end).normalized()
        )
 
        output_pixmap.save(config.SAVE_IMAGE_PATH)

        self.label = QtWidgets.QLabel(pixmap=output_pixmap)
        self.label.show()
        app.setQuitOnLastWindowClosed(True)


def lunch_Snipping_tool():
    window = MyWidget()
    window.show()
    app.aboutToQuit.connect(app.deleteLater)
    app.setQuitOnLastWindowClosed(False)
    app.exec_()