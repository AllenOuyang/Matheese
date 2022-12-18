from time import sleep
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader
from tasks.task_factory import TaskFactory
import sympy as sy
from PySide6.QtWidgets import QWidget, QVBoxLayout, QComboBox
from PySide6.QtGui import QPixmap, QIcon


class Matheese:

    def __init__(self):
        # load ui file
        self.ui = QUiLoader().load('userinterfaces/mainwin.ui')
        self.ui.button.clicked.connect(self.go_calculate)
        self.window_task1 = None
        self.window_task2 = None
        self.window_task3 = None
        self.solver = None

    @Slot()
    def go_calculate(self):
        tab_name = self.ui.tabWidget.currentWidget().objectName()
        self.solver = TaskFactory().generate_task(tab_name)
        if tab_name == 'Task1':
            self.Task1()
        elif tab_name == 'Task2':
            self.Task2()
        elif tab_name == 'Task3':
            self.Task3()

    def Task1(self):
        f = self.ui.function1.text().replace('^', '**')
        g = self.ui.function2.text().replace('^', '**')
        h = self.ui.function3.text().replace('^', '**')
        a1 = self.ui.arange1.text()
        b1 = self.ui.brange1.text()
        a2 = self.ui.arange2.text()
        b2 = self.ui.brange2.text()
        a3 = self.ui.arange3.text()
        b3 = self.ui.brange3.text()
        self.solver.getData(f, g, h, a1, b1, a2, b2, a3, b3)
        if self.solver.check():
            res = self.solver.execute()
            self.window_task1 = QUiLoader().load('userinterfaces/task1.ui')
            pixmap = QPixmap("resource/task1.png")
            pixmap1 = QPixmap("formula/task1_fff.png")
            pixmap2 = QPixmap("formula/task1_ggg.png")
            pixmap3 = QPixmap("formula/task1_hhh.png")
            self.window_task1.fff.setPixmap(pixmap1)
            self.window_task1.ggg.setPixmap(pixmap2)
            self.window_task1.hhh.setPixmap(pixmap3)
            self.window_task1.label.setPixmap(pixmap)
            self.window_task1.show()
        else:
            QMessageBox.about(self.ui, 'result', 'error')
        QMessageBox.about(self.ui, 'result', 'The area is ' + str(res))

    def Task2(self):
        func = self.ui.function2d.text().replace('^', '**')
        grx, gry = self.ui.grx.text().replace('^', '**'), self.ui.gry.text().replace('^', '**')
        start = self.ui.startpoint.text()
        xx = self.ui.xx.text()
        yy = self.ui.yy.text()
        self.solver.getData(func, grx, gry, start, xx, yy)
        if self.solver.check():
            res = self.solver.execute()
            self.window_task2 = QUiLoader().load('userinterfaces/task2.ui')
            pixmap = QPixmap("resource/task2.png")
            pixmap1 = QPixmap("formula/task2_fxy.png")
            self.window_task2.fxy.setPixmap(pixmap1)
            self.window_task2.label.setPixmap(pixmap)
            self.window_task2.show()
        else:
            QMessageBox.about(self.ui, 'result', 'error')
        QMessageBox.about(self.ui, 'result', 'Minimum: ' + str(res))

    def Task3(self):
        name_tab = self.ui.TypeTab.currentWidget().objectName()
        if name_tab == 'Type1':
            f = self.ui.rightpart1.text().replace('^', '**')
            interval = self.ui.interval1.text()
            i = self.ui.comboBox1.currentIndex()
            self.solver.getData(f, interval, 1, i)
            if self.solver.check():
                res = self.solver.execute()
                self.window_task3 = QUiLoader().load('userinterfaces/task3.ui')
                pixmap = QPixmap("resource/task3.png")
                pixmap1 = QPixmap("formula/task3_rhs.png")
                pixmap2 = QPixmap("formula/task3_KKK.png")
                self.window_task3.rhs.setPixmap(pixmap1)
                self.window_task3.KKK.setPixmap(pixmap2)
                self.window_task3.label.setPixmap(pixmap)
                self.window_task3.show()
            else:
                QMessageBox.about(self.ui, 'result', 'error')
        elif name_tab == 'Type2':
            f = self.ui.rightpart2.text()
            interval = self.ui.interval2.text()
            i = self.ui.comboBox2.currentIndex()
            self.solver.getData(f, interval, 2, i)
            if self.solver.check():
                res = self.solver.execute()
                self.window_task3 = QUiLoader().load('userinterfaces/task3.ui')
                pixmap = QPixmap("resource/task3.png")
                pixmap1 = QPixmap("formula/task3_rhs.png")
                pixmap2 = QPixmap("formula/task3_KKK.png")
                self.window_task3.rhs.setPixmap(pixmap1)
                self.window_task3.KKK.setPixmap(pixmap2)
                self.window_task3.label.setPixmap(pixmap)
                self.window_task3.show()
            else:
                QMessageBox.about(self.ui, 'result', 'error')
        else:
            pass
        
    # @Slot()
    # def index_changed1(self, i):
    #     self.i = i
    #     print(i)

    # @Slot()
    # def index_changed2(self, i):
    #     self.i = i
    #     print(i)