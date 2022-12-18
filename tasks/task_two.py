from matplotlib import pyplot as plt
import sympy as sy
from tasks.task import Task
from stringprocessing.expression import function, function2D
from algorithm.algorithm import grad, golden
from numpy import *
import re


class TaskTwo(Task):
    def __init__(self):
        Task.__init__(self)
        self.F = None
        self.GradF = []
        self.start = [0, 0]
        self.xinterval = [0, 0]
        self.yinterval = [0, 0]
        self.proper = True

    def getData(self, f, grx, gry, start, xx, yy):
        try:
            self.F = f
            self.GradF = [grx, gry]
            self.start = eval(start)
            self.xinterval = eval(xx)
            self.yinterval = eval(yy)
            x = sy.Symbol('x')
            y = sy.Symbol('y')
            sy.preview(sy.simplify(f), output='png', viewer='file', filename='formula/task2_fxy.png', dvioptions=["-bg", "Transparent"])
        except Exception:
            self.proper = False

    def check(self):
        return self.proper

    def execute(self):
        def F(X):
            x = X[0]
            y = X[1]
            return eval(self.F)

        def GradF(X):
            x = X[0]
            y = X[1]
            gr = zeros((2), 'float')
            gr[0] = eval(self.GradF[0])
            gr[1] = eval(self.GradF[1])
            return gr
        x = linspace(self.xinterval[0], self.xinterval[1], 101)
        y = linspace(self.yinterval[0], self.yinterval[1], 101)
        X, Y = meshgrid(x, y)
        z = F([X, Y])
        v = linspace(0., 10., 21)
        plt.contour(x, y, z, v, cmap=plt.cm.rainbow)
        plt.colorbar()
        plt.savefig('resource/task2.png')
        plt.close()
        # plt.show()
        # minumum function
        x0 = array(self.start)
        xMin, nIt = grad(F, GradF, x0)
        return xMin
        # print('xMin:', xMin)
        # print('Number of iterations = ', nIt)
