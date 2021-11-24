import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QAbstractItemView
from PyQt5.QtWidgets import QWidget, QTableWidgetItem


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setWindowTitle("Эспрессо")
        self.connection = sqlite3.connect("coffee.sqlite")
        self.pushButton.clicked.connect(self.show_data)

    def show_data(self):
        res = self.connection.cursor().execute("""SELECT * FROM Coffee""").fetchall()
        colcount = 0
        for i in res:
            colcount = len(i)
        self.tableWidget.setColumnCount(colcount)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.pushButton.setEnabled(False)

    def closeEvent(self, event):
        self.connection.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
