import sys
from PyQt5.QtWidgets import QLabel, QApplication, QMainWindow, QAction, QMessageBox
from login import Demo as ddd
from student_search import Demo as ss
from teacher_record import Demo as tr
from output_xls import Demo as ox

class Demo(QMainWindow):
    def __init__(self):
        super(Demo, self).__init__()
        self.account_menu = self.menuBar().addMenu('Account')
        self.search_menu = self.menuBar().addMenu('Search')
        self.record_menu = self.menuBar().addMenu('Record')
        
        self.login_action = QAction('Login')
        self.xls_action = QAction('output a xls')
        self.search_action = QAction('Search your score')
        self.record_action = QAction('record a exam')
        self.sp = ddd()
        self.iden = (-1, -1)
        self.resize(450, 600)
        self.menu_init()
        self.action_init()

        

    def menu_init(self):
        self.account_menu.addAction(self.login_action)
        self.search_menu.addAction(self.search_action)
        self.search_menu.addAction(self.xls_action)
        self.record_menu.addAction(self.record_action)


    def action_init(self):
        self.login_action.triggered.connect(self.new_func)
        self.search_action.triggered.connect(self.search_func)
        self.xls_action.triggered.connect(self.xls_func)
        self.record_action.triggered.connect(self.record_func)
        self.sp.success.connect(self.logwin)

    def xls_func(self):
        self.ox_ = ox()
        self.setCentralWidget(self.ox_)

    def record_func(self):
        if self.iden[1]==1:
            self.tr_ = tr()
            self.setCentralWidget(self.tr_)
        else:
            QMessageBox.warning(self, 'dame', 'Login first!')
    def search_func(self):
        if self.iden[1]==0:
            self.ss_ = ss()
            self.ss_.code = self.iden[0]
            self.setCentralWidget(self.ss_)
        else:
            QMessageBox.warning(self, 'dame', 'Login first!')
    
    def logwin(self):
        self.iden = self.sp.identity
        self.statusBar().addWidget(QLabel('logged in as {},a {}'.format(self.iden[0], 'teacher' if self.iden[1] else 'student')))
        
    def new_func(self):
        self.sp.exec_()
        




if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())