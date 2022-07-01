import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QHBoxLayout, QCheckBox, QComboBox, QVBoxLayout, QPushButton, QTableWidgetItem, QTableWidget, QHeaderView

class Demo(QWidget):

    def __init__(self):
        super().__init__()
        self.exam_label = QLabel('choice exam', self)
        self.subj_label = QLabel('choice subject', self)
        self.show_class_check = QCheckBox('show class', self)
        self.show_rank_check = QCheckBox('show rank', self)
        #these two lines will be enough? in chap.7
        self.exam_combo = QComboBox(self)
        self.subj_combo = QComboBox(self)
        self.search_button = QPushButton('Start', self)

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.exam_label)
        self.h_layout.addWidget(self.exam_combo)
        self.h_layout.addWidget(self.subj_label)
        self.h_layout.addWidget(self.subj_combo)
        self.h_layout.addWidget(self.show_class_check)
        self.h_layout.addWidget(self.show_rank_check)
        self.h_layout.addWidget(self.search_button)

        self.table = Demo_table()
        self.v_layout = QVBoxLayout()
        self.v_layout.addLayout(self.h_layout)
        self.v_layout.addWidget(self.table)

        self.setLayout(self.v_layout)

        

class Demo_table(QTableWidget):
    def __init__(self):
        super().__init__()
        self.setRowCount(6)
        self.setColumnCount(6)
        self.setColumnWidth(0, 30)
        self.setRowHeight(0, 30)
        self.setHorizontalHeaderLabels(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        self.item_1 = QTableWidgetItem('Hi11111111111111111111111111111111111111')
        self.setItem(0, 0, self.item_1)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())