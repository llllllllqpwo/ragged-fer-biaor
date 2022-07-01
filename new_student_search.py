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
        self.rct = 7
        self.setRowCount(1)
        self.setColumnCount(6)
        self.setColumnWidth(0, 30)
        self.setRowHeight(0, 30)
        for i in range(self.rct - 1):
            self.new_line()
        self.setHorizontalHeaderLabels(['delete', 'name', 'code', 'k', 'd', 'a'])
        self.nbuton = QPushButton('new line')
        self.nbuton.clicked.connect(self.new_line)
        self.setSpan(self.rowCount()-1, 0, 1, self.columnCount())
        self.setCellWidget(self.rowCount()-1, 0, self.nbuton)

        # self.removeRow(2)
        # self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    def new_line(self):
        self.insertRow(self.rowCount()-1)
        self.dbuton = QPushButton('d')
        self.dbuton.clicked.connect(lambda:self.dlt())
        self.setCellWidget(self.rowCount()-2, 0, self.dbuton)
        
    def dlt(self):
       button = self.sender()
       if button:
            row = self.indexAt(button.pos()).row()
            self.removeRow(row)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())