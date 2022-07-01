import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QTableWidget, QLineEdit

class Demo(QWidget):

    def __init__(self):
        super().__init__()
        self.exam_label = QLabel('new exam')
        self.exam_line = QLineEdit()
        self.save_button = QPushButton('Save')
        self.delete_button = QPushButton('Delete')

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.exam_label)
        self.h_layout.addWidget(self.exam_line)
        self.h_layout.addWidget(self.delete_button)
        self.h_layout.addWidget(self.save_button)

        self.table = Demo_table()
        self.delete_button.clicked.connect(self.table.dlt)
        self.save_button.clicked.connect(lambda:print('saved'))
        self.v_layout = QVBoxLayout()
        self.v_layout.addLayout(self.h_layout)
        self.v_layout.addWidget(self.table)

        self.setLayout(self.v_layout)

        

class Demo_table(QTableWidget):
    def __init__(self):
        super().__init__()
        self.rct = 7
        self.setRowCount(1)
        self.setColumnCount(5)
        # self.setColumnWidth(0, 30)
        self.setRowHeight(0, 30)
        for i in range(self.rct - 1):
            self.new_line()
        self.setHorizontalHeaderLabels(['name', 'code', 'k', 'd', 'a'])
        self.nbuton = QPushButton('new line')
        self.nbuton.clicked.connect(self.new_line)
        self.setSpan(self.rowCount()-1, 0, 1, self.columnCount())
        self.setCellWidget(self.rowCount()-1, 0, self.nbuton)

        # self.removeRow(2)
        # self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    def new_line(self):
        self.insertRow(self.rowCount()-1)
        # self.check = QTableWidgetItem()
        # self.check.setCheckState(Qt.Unchecked)
        # self.setItem(self.rowCount()-2, 0, self.check)
        # self.dbuton = QPushButton('d')
        # self.dbuton.clicked.connect(lambda:self.dlt())
        # self.setCellWidget(self.rowCount()-2, 0, self.dbuton)
        
    def dlt(self):
        s_items = self.selectedIndexes()
        if s_items:
            selected_rows = []
            for i in s_items:
                row = i.row()
                if row not in selected_rows and row != self.rowCount()-1:
                    selected_rows.append(row)
            for r in range(len(sorted(selected_rows))):
                    self.removeRow(selected_rows[r]-r)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())