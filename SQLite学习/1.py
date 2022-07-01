import sys
from PyQt5.QtWidgets import QMainWindow,QWidget,QApplication,QMessageBox,QTableView,QHBoxLayout
from PyQt5.QtSql import QSqlDatabase,QSqlQuery,QSqlTableModel
 
class sqlDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('demo')
        self.resize(600,600)
        self.layout=QHBoxLayout()
        self.setLayout(self.layout)
 
        #------数据库操作------
        #1连接数据库
        self.connect_db()
        #操作数据库
        self.opreate_db()
        #关闭数据库
        self.close_db()
       
 
 
    def connect_db(self):
        self.db=QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('./test.db')
        # d=self.db.open()
        # print(d)       #显示True 表示连接成功
        if not self.db.open():
            QMessageBox.critical(self,'database error',self.db.lastError.text(),QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
 
    
    def opreate_db(self):
        query=QSqlQuery()
        #【建立表】
        query.exec_("create table test(ID int primary key,name varchar(20),url varchar(100))")
        #【插入数据】
        query.exec_("insert into test values(1000,'tom','http://www.xx.com')")
        query.exec_("insert into test values(1001,'marray','http://www.xx.com')")
        query.exec_("insert into test values(1002,'jack','http://www.xx.com')")
        #【查询数据】
        query.exec_("select * from test ")
        #备注：在执行exec_()查询时指针会放在记录集中第一个记录之上所以需要调用next（）
        while query.next():
            id=query.value(0)
            name=query.value(1)
            url=query.value(2)
            print('id:'+str(id)+'----name:'+name+'---url:'+url)
        # #【删除数据】
        value=query.exec_("delete from test where ID=1001")
        # print(value) #为true表示删除成功
        if value:
            QMessageBox.information(self,'delet data','删除成功',QMessageBox.Ok|QMessageBox.No,QMessageBox.Ok)
        else:
             QMessageBox.information(self,'delet data','删除失败',QMessageBox.Ok|QMessageBox.No,QMessageBox.Ok)
        
        # #【修改数据】
        query.exec_("update test set name='bbb' where id=1002")
        
  
 
    #关闭数据库
    def close_db(self):
        self.db.close()
 
 
if __name__=='__main__':
    app=QApplication(sys.argv)
    demo=sqlDemo()
    demo.show()
    sys.exit(app.exec_())