import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QCheckBox, QComboBox, QAbstractItemView
from dbctl import dbrqt
from pyqtgraph import PlotWidget
class Demo(QWidget):

    def __init__(self):
        super().__init__()
        self.code = 123
        self.exam_label = QLabel('choice exam')
        self.subj_label = QLabel('choice subject')
        self.show_class_check = QCheckBox('inrank')
        self.show_rank_check = QCheckBox('outrank')
        self.exam_combo = QComboBox()
        self.subj_combo = QComboBox()
        self.search_button = QPushButton('Join')
        self.delete_button = QPushButton('Delete')
        self.graph_button = QPushButton('graph')

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.exam_label)
        self.h_layout.addWidget(self.exam_combo)
        self.h_layout.addWidget(self.subj_label)
        self.h_layout.addWidget(self.subj_combo)
        self.h_layout.addWidget(self.show_class_check)
        self.h_layout.addWidget(self.show_rank_check)
        self.h_layout.addWidget(self.search_button) 
        self.h_layout.addWidget(self.delete_button)
        self.h_layout.addWidget(self.graph_button)

        self.table = Demo_table()
        self.dbrqt = dbrqt()
        self.show_class_check.stateChanged.connect(lambda:self.table.setColumnHidden(1, 2-self.show_class_check.checkState()))
        self.show_rank_check.stateChanged.connect(lambda:self.table.setColumnHidden(2, 2-self.show_rank_check.checkState()))
        self.subj_combo.currentIndexChanged.connect(self.on_combobox_func)
        self.exam_combo.addItems(self.dbrqt.exams)
        self.subj_combo.addItems(['total', 'k', 'd', 'a'])
        self.delete_button.clicked.connect(self.table.dlt)
        self.search_button.clicked.connect(lambda:self.join(self.exam_combo.currentText(), self.code))
        self.graph_button.clicked.connect(self.table.graph)
        self.v_layout = QVBoxLayout()
        self.v_layout.addLayout(self.h_layout)
        self.v_layout.addWidget(self.table)

        self.setLayout(self.v_layout)
    def on_combobox_func(self):
        state = self.subj_combo.currentIndex()
        for i in range(4):
            if i == state:
                self.table.setColumnHidden(i+3, False)
            else:
                self.table.setColumnHidden(i+3, True)

    def join(self, exam, code):
        li = self.dbrqt.search(exam, code)[0]
        self.table.insertRow(0)
        for i in range(7):
            c = 0
            if i == 0:
                c = exam
            else:
                c = li[i-1]
            self.table.setItem(0, i, QTableWidgetItem(str(c)))

        

class Demo_table(QTableWidget):
    def __init__(self):
        super().__init__()
        self.rct = 7
        self.setRowCount(0)
        self.setColumnCount(7)
        self.setRowHeight(0, 30)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setHorizontalHeaderLabels(['exam', 'inrank', 'outrank', 'sum', 'k', 'd', 'a'])
        self.setColumnHidden(1,True)
        self.setColumnHidden(2,True)

    def graph(self):
        self.values = []
        self.col = self.currentColumn()
        for i in range(self.rowCount()):
            self.values.append(int(self.item(i, self.col).text()))
        print(self.values)
        self.plotw = PlotWidget()
        self.plotw.plot(self.values, pen='r', symbol='o')
        self.plotw.show()

        

    def dlt(self):
        s_items = self.selectedIndexes()
        if s_items:
            selected_rows = []
            for i in s_items:
                row = i.row()
                if row not in selected_rows:
                    selected_rows.append(row)
            for r in range(len(sorted(selected_rows))):
                    self.removeRow(selected_rows[r]-r)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())