# find intersection among three functions and then calculate area which they surrround
import numpy as np

from algorithm.algorithm import root, integral
from tasks.task import Task
from scipy.interpolate import CubicSpline
from stringprocessing.expression import function
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import sympy as sy
from numpy import *
import pandas as pd


class TaskFour(Task):
    def __init__(self):
        Task.__init__(self)
        self.inputFlie_name = ""
        self.dfin = None
        self.dfout = None
        self.x = []
        self.y = []
        self.writer = pd.ExcelWriter('resource/task4out.xlsx')
        self.proper = True


    def getData(self, s):
        try:
            self.inputFlie_name = s
            self.dfin = pd.read_excel(self.inputFlie_name)
            tmp = array(self.dfin)
            self.x = tmp[:, 0]
            self.y = tmp[:, 1]

        except Exception:
            self.proper = False

    def check(self):
        return self.proper

    def execute(self):
        f = CubicSpline(self.x, self.y, bc_type='natural')
        x_new = np.linspace(min(self.x), max(self.x), 100)
        y_new = f(x_new)
        plt.plot(x_new, y_new, 'b')
        plt.plot(self.x, self.y, 'ro')
        plt.title('Cubic Spline')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.savefig('resource/task4.png')
        self.dfout = pd.DataFrame(f.c)
        self.dfout.to_excel(self.writer)
        self.writer.close()
        
