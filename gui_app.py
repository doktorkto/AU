from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
import sys
import os

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('first_try.ui', self)
        
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(20)
        self.tableWidget.setHorizontalHeaderLabels(('Word','Gender','Plural form', 'Translation'))
        
        self.pushButton_2.clicked.connect(self.clear)
        self.tableWidget.setSortingEnabled(True)
        
        row = 0
        for item in range(0, 20):
            cellinfo = QTableWidgetItem(item)
 
            combo = QtWidgets.QComboBox()
            combo.addItem("masculine")
            combo.addItem("feminine")
 
            self.tableWidget.setItem(row, 0, cellinfo)
            self.tableWidget.setCellWidget(row, 1, combo)
            row += 1
        
        raw = 0
        for item in range(0, 20):
            cellinfo = QTableWidgetItem(item)
 
            combo = QtWidgets.QComboBox()
            combo.addItem("-")
            combo.addItem("-ies")
            combo.addItem("-s")
 
            self.tableWidget.setItem(raw, 1, cellinfo)
            self.tableWidget.setCellWidget(raw, 2, combo)
            raw += 1

    def clear(self):
        self.tableWidget.clear()

def main():
    app = QtWidgets.QApplication(sys.argv) 
    window = MainWindow()
    window.show() 
    app.exec_()
    
if __name__ == '__main__': 
    main()
