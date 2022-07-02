import pyqtgraph
import sys
from PyQt5.QtWidgets import QApplication
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = pyqtgraph.PlotWidget()
    demo.plot([1, 2, 3, 4, 5], pen='r', symbol='o')
    demo.show()
    sys.exit(app.exec_())