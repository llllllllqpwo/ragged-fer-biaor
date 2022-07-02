import sys
import hashlib
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout
from security import security


class Demo(QDialog):
    success = pyqtSignal()
    def __init__(self):
        super(Demo, self).__init__()

        self.user_label = QLabel('Usercode:', self)
        self.pwd_label = QLabel('Password:', self)
        self.user_line = QLineEdit(self)
        self.pwd_line = QLineEdit(self)
        self.student_bt = QPushButton('student', self)
        self.teacher_bt = QPushButton('teacher', self)

        self.user_h_layout = QHBoxLayout()                      
        self.pwd_h_layout = QHBoxLayout()                       
        self.button_h_layout = QHBoxLayout()                     
        self.all_v_layout = QVBoxLayout()                        

        self.user_h_layout.addWidget(self.user_label)
        self.user_h_layout.addWidget(self.user_line)
        self.pwd_h_layout.addWidget(self.pwd_label)
        self.pwd_h_layout.addWidget(self.pwd_line)
        self.button_h_layout.addWidget(self.student_bt)
        self.button_h_layout.addWidget(self.teacher_bt)
        self.all_v_layout.addLayout(self.user_h_layout)
        self.all_v_layout.addLayout(self.pwd_h_layout)
        self.all_v_layout.addLayout(self.button_h_layout)

        self.student_bt.clicked.connect(lambda:self.login_func(0))
        self.teacher_bt.clicked.connect(lambda:self.login_func(1))
        
        self.setLayout(self.all_v_layout)
    def login_func(self, iden):
        sc = security()
        user = self.user_line.text()
        if user.isdigit():
            md5pw=hashlib.md5(self.pwd_line.text().encode('utf8')).hexdigest()
            if sc.login(user, md5pw, iden):
                self.identity = (user, iden)
                self.success.emit()
                self.close()
            else:
                QMessageBox.critical(self, 'Wrong', 'Wrong usercode or password')
        else:
            QMessageBox.critical(self, 'Wrong', 'Wrong usercode format')



        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

