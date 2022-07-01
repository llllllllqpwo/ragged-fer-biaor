import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QTableWidget, QCheckBox, QComboBox

class Demo(QWidget):

    def __init__(self):
        super().__init__()
        self.exam_label = QLabel('choice exam')
        self.subj_label = QLabel('choice subject')
        self.show_class_check = QCheckBox('show class')
        self.show_rank_check = QCheckBox('show rank')
        self.exam_combo = QComboBox()
        self.subj_combo = QComboBox()
        self.search_button = QPushButton('Start', )
        self.delete_button = QPushButton('Delete')

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.exam_label)
        self.h_layout.addWidget(self.exam_combo)
        self.h_layout.addWidget(self.subj_label)
        self.h_layout.addWidget(self.subj_combo)
        self.h_layout.addWidget(self.show_class_check)
        self.h_layout.addWidget(self.show_rank_check)
        self.h_layout.addWidget(self.search_button) 
        self.h_layout.addWidget(self.delete_button)

        self.table = Demo_table()
        self.delete_button.clicked.connect(self.table.dlt)
        self.search_button.clicked.connect(lambda:print('saved'))
        self.v_layout = QVBoxLayout()
        self.v_layout.addLayout(self.h_layout)
        self.v_layout.addWidget(self.table)

        self.setLayout(self.v_layout)

        

class Demo_table(QTableWidget):
    def __init__(self):
        super().__init__()
        self.rct = 7
        self.setRowCount(0)
        self.setColumnCount(5)
        self.setRowHeight(0, 30)
        self.setHorizontalHeaderLabels(['rank', 'sum', 'k', 'd', 'a'])

        
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