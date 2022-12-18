from tasks.task import Task
from stringprocessing.expression import function
from numpy import *
import sympy as sy
from algorithm.algorithm import *
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt
import pandas as pd

class TaskThree(Task):
    def __init__(self):
        Task.__init__(self)
        self.f = None
        self.K = None
        self.interval = [0, 0]
        self.protype = 1 
        self.proper = True
        self.writer = pd.ExcelWriter('resource/task3.xlsx')
        self.kernels2 = ['1 / (pi * (1 + (x - s) ** 2))', '(x-s)', 'abs(x-s)', 'exp(x-s)', 
                            '1 / (pi * (1 + (x - s) ** 2))', '0.1 / (0.1**2 + (x - s) ** 2)']
        self.kernels1 = ['0.1 / (0.1**2 + (x - s) ** 2)', '(x-s)', 'abs(x-s)', 'exp(x-s)', 
                            '1 / (pi * (1 + (x - s) ** 2))', '0.1 / (0.1**2 + (x - s) ** 2)']
        

    def getData(self, f, interval, protype, i):
        try:
            self.f = lambda x: eval(f)
            self.interval = eval(interval)
            self.protype = protype
            if self.protype == 1:
                self.K = lambda x, s: eval(self.kernels1[i])
                K = self.kernels1[i]
            elif self.protype == 2:
                self.K = lambda x, s: eval(self.kernels2[i])
                K = self.kernels2[i]
            x = sy.Symbol('x')
            s = sy.Symbol('s')
            sy.preview(sy.simplify(f), output='png', viewer='file', filename='formula/task3_rhs.png', dvioptions=["-bg", "Transparent"])
            sy.preview(sy.simplify(K), output='png', viewer='file', filename='formula/task3_KKK.png', dvioptions=["-bg", "Transparent"])
            
        except Exception:
            self.proper = False

    def check(self):
        return self.proper

    def execute(self):
        if self.protype == 1:
            self.execute1()
        elif self.protype == 2:
            self.execute2()
        else:
            pass
    
    def execute1(self):
        a, b = self.interval[0], self.interval[1]
        n = 100
        h = (b - a) / n
        x = linspace(a + h / 2, b - h / 2, n)
        erList = [1.0e-3, 1.0e-5, 1.0e-10]
        sgList = ['-', '--', ':']
        for kk in range(len(erList)):
            er = erList[kk]
            y, iter = fredholm1(self.K, self.f, a, b, n, tol=er)
            sl = 'tolerance = ' + str(er)
            sg = sgList[kk]
            plt.plot(x, y, sg, label=sl)
            df = pd.DataFrame([x, y])
            df.to_excel(self.writer, 'sheet' + str(kk), float_format='%.2f', header=False, index=False)
        self.writer.close()
        plt.legend(loc=8)
        plt.savefig('resource/task3.png')
        plt.close()

    def execute2(self):
        a, b = self.interval[0], self.interval[1]
        nList = [5, 10, 50]
        sglist = ['-', '--', ':']
        for kk in range(len(nList)):
            n = nList[kk]
            x = linspace(a, b, n + 1)
            y = fredholm(self.K, self.f, a, b, n)
            sl = 'n=' + str(n+1)
            sg = sglist[kk]
            plt.plot(x, y, sg, label=sl)
            df = pd.DataFrame([x, y])
            df.to_excel(self.writer, 'sheet' + str(kk), float_format='%.2f', header=False, index=False)
        self.writer.close()
        plt.legend(loc=0)
        plt.savefig('resource/task3.png')
        plt.close()