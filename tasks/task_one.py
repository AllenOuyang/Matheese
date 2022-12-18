# find intersection among three functions and then calculate area which they surrround
import numpy as np

from algorithm.algorithm import root, integral
from tasks.task import Task
from stringprocessing.expression import function
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import sympy as sy
from numpy import *


class TaskOne(Task):
    def __init__(self):
        Task.__init__(self)
        self.a1, self.a2, self.a3 = 0, 0, 0
        self.b1, self.b2, self.b3 = 0, 0, 0
        self.f = None
        self.g = None
        self.h = None
        self.proper = True
        self.canvas = None

    def getData(self, f, g, h, a1, b1, a2, b2, a3, b3):
        try:
            self.f = lambda x: eval(f)
            self.g = lambda x: eval(g)
            self.h = lambda x: eval(h)
            self.a1 = float(a1)
            self.b1 = float(b1)
            self.a2 = float(a2)
            self.b2 = float(b2)
            self.a3 = float(a3)
            self.b3 = float(b3)
            x = sy.Symbol('x')
            sy.preview(sy.simplify(f), output='png', viewer='file', filename='formula/task1_fff.png', dvioptions=["-bg", "Transparent"])
            sy.preview(sy.simplify(g), output='png', viewer='file', filename='formula/task1_ggg.png', dvioptions=["-bg", "Transparent"])
            sy.preview(sy.simplify(h), output='png', viewer='file', filename='formula/task1_hhh.png', dvioptions=["-bg", "Transparent"])
        except Exception:
            self.proper = False

    def check(self):
        return self.proper

    def execute(self):
        intersection_fg = root(self.f, self.g, self.a1, self.b1)
        intersection_fh = root(self.f, self.h, self.a2, self.b2)
        intersection_gh = root(self.g, self.h, self.a3, self.b3)
        integral_f = integral(self.f, min(intersection_fg, intersection_fh), max(intersection_fg, intersection_fh))
        integral_g = integral(self.g, min(intersection_fg, intersection_gh), max(intersection_fg, intersection_gh))
        integral_h = integral(self.h, min(intersection_fh, intersection_gh), max(intersection_fh, intersection_gh))
        area = integral_f - integral_g - integral_h
        self.drawFunction(min(self.a1, self.a2, self.a3), max(self.b1, self.b2, self.b3), self.f, self.g, self.h)
        return area


    def drawFunction(self, start, end, *functions):
        fig = Figure(figsize=(10, 8), dpi=100)
        for f in functions:
            x = linspace(start, end, 100)
            y = [f(xi) for xi in x]
            plt.plot(x, y)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
        plt.savefig('resource/task1.png')
        plt.close()