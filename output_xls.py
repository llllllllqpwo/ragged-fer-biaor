import sqlite3
from PyQt5.QtWidgets import QComboBox, QPushButton, QHBoxLayout, QWidget
from dbctl import dbrqt
from xlsxwriter.workbook import Workbook
class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.conn = sqlite3.connect('test.db')
        self.c = self.conn.cursor()
        self.dbrqt = dbrqt()
        self.exam_combo = QComboBox()
        self.exam_combo.addItems(self.dbrqt.exams)
        self.buton = QPushButton('Go')
        self.buton.clicked.connect(self.xls)
        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.exam_combo)
        self.h_layout.addWidget(self.buton)
        self.setLayout(self.h_layout)

    def xls(self):
        sheetname = self.exam_combo.currentText()
        workbook = Workbook('{}.xlsx'.format(sheetname))
        worksheet = workbook.add_worksheet()
        mysel = self.c.execute('select * from {}'.format(sheetname))
        for i, row in enumerate(mysel):
            for j, value in enumerate(row):
                worksheet.write(i, j, value)
        workbook.close()