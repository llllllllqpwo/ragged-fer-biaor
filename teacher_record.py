import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QHBoxLayout, QLineEdit, QVBoxLayout, QPushButton, QTableWidgetItem, QTableWidget

class Demo(QWidget):

    def __init__(self):
        super().__init__()
        self.exam_label = QLabel('new exam', self)
        self.exam_line = QLineEdit(self)
        self.search_button = QPushButton('Save', self)

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.exam_label)
        self.h_layout.addWidget(self.exam_line)
        self.h_layout.addWidget(self.search_button)

        self.table = Demo_table()
        self.v_layout = QVBoxLayout()
        self.v_layout.addLayout(self.h_layout)
        self.v_layout.addWidget(self.table)

        self.setLayout(self.v_layout)

        

class Demo_table(QTableWidget):
    def __init__(self):
        super().__init__()
        self.rct = 6
        self.setRowCount(self.rct)
        self.setColumnCount(6)
        self.setColumnWidth(0, 30)
        self.setRowHeight(0, 30)
        for i in range(self.rct):
            self.buton = QPushButton('d')
            self.buton.clicked.connect(lambda:self.dlt(i))
            self.setCellWidget(i, 0, self.buton)
        self.setHorizontalHeaderLabels(['delete', 'name', 'code', 'k', 'd', 'a'])
        self.item_1 = QTableWidgetItem('Hi11111111111111111111111111111111111111')
        self.setItem(2, 2, self.item_1)
        # self.removeRow(2)
        # self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    
    def dlt(self, r):
        self.removeRow(r)
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())