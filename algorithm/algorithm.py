import numpy as np
from math import *
from matplotlib import pyplot as plt
from scipy.misc import derivative


def root(f, g, a, b, eps=10 ** -4):
    def target(x): return f(x) - g(x)
    def target1(x): return derivative(
        f, x, dx=1e-6) - derivative(g, x, dx=1e-6)
    while abs(b - a) > eps:
        if target(a) < 0:
            a = a + (b - a) / (target(a) - target(b)) * target(a)
            b = b - target(b) / target1(b)
        elif target(a) > 0:
            a = a - target(a) / target1(a)
            b = b + (b - a) / (target(b) - target(a)) * target(b)
        else:
            return a
    return float((a + b) / 2)


def integral(f, a, b, eps=10 ** -4):
    width = b - a
    sumNew = width * (f(a) + f(b)) / 2
    sumOld, n = 0, 1
    while abs(sumNew - sumOld) >= eps:
        sumOld = sumNew
        sumNew = 0
        for i in range(n):
            sumNew += f(a + width * (i + 0.5) / n)
        sumNew *= width / n
        n *= 2
    return sumNew

# def drawFunction(start, end, *functions):
#     for f in functions:
#         x = np.linspace(start, end, 100)
#         y = [f(xi) for xi in x]
#         plt.plot(x, y)
#     plt.xlabel("x")
#     plt.ylabel("y")
#     plt.legend()
#     plt.savefig('../resource/tmp.png', transparent=True)


def golden(f, a, b, tol=1.0e-10):
    """
    Golden section method for determing x
    that minimizes the scalar funvtion f(x)
    The minimum must be bracketed in (a, b)
    """
    c1 = (sqrt(5.) - 1.) / 2.
    c2 = 1. - c1
    nIt = int(ceil(log(tol / abs(b-a)) / log(c1)))
    # First step
    x1 = c1 * a + c2 * b
    x2 = c2 * a + c1 * b
    f1 = f(x1)
    f2 = f(x2)
    # Iteration
    for i in range(nIt):
        if f1 > f2:
            a = x1
            x1 = x2
            f1 = f2
            x2 = c2 * a + c1 * b
            f2 = f(x2)
        else:
            b = x2
            x2 = x1
            f2 = f1
            x1 = c1 * a + c2 * b
            f1 = f(x1)
    if f1 < f2:
        return x1, f1
    else:
        return x2, f2


def grad(F, GradF, x, d=0.5, tol=1.e-10):
    """
    Gradient method for determining vector X
    that minimizes the function F(x),
    GradF(x) is function for grad(F),
    x is starting point.
    """
    # Line function along h
    def f(al):
        return F(x + al * h)
    gr0 = - GradF(x)
    h = gr0.copy()
    F0 = F(x)
    itMax = 500
    for i in range(itMax):
        # Minimization 1D function
        al, fMin = golden(f, 0, d)
        x = x + al * h
        F1 = F(x)
        gr1 = - GradF(x)
        if (sqrt(np.dot(gr1, gr1)) <= tol) or (abs(F0 - F1) < tol):
            return x, i + 1
        h = gr1
        gr0 = gr1.copy()
        F0 = F1
    print('Gradient method did not converge (500 iterations)')

def decLU(A):
    """
    Returns the decompositon LU f o r matrix A.
    """
    n = len(A)
    LU = np.copy(A)
    for j in range(n-1):
        for i in range(j + 1, n):
            if LU[i, j] != 0:
                u = LU[i, j] / LU[j, j]
                LU[i, j+1: n] = LU[i, j+1: n] - u * LU[j, j+1:n]
                LU[i,j] = u
    return LU

def solveLU(A, f):
    """
    Solve the linear system Ax = b
    """
    n = len(A)
    # LU decomposition
    LU = decLU(A)
    x = np.copy(f)
    # forward substition process
    for i in range(1, n):
        x[i] = x[i] - np.dot(LU[i, 0:i], x[0: i])
    # back substitution process
    for i in range(n-1, -1, -1):
        x[i] = (x[i] - np.dot(LU[i, i+1: n], x[i+1: n])) / LU[i, i]
    return x

def cg(A, f, tol=1.0e-9):
    """
    Solve the linear system Ax = b by conjugate gradient method.
    """
    n = len(f)
    x = np.zeros((n), 'float')
    r = np.copy(f)
    for i in range(n):
        r[i] = np.dot(A[i, 0: n], x[0: n]) - f[i]
    s = np.copy(r)
    As = np.zeros((n), 'float')
    for k in range(n):
        for i in range(n):
            As[i] = np.dot(A[i, 0:n], s[0: n])
        alpha = np.dot(r, r) / np.dot(s, As)
        x = x - alpha * s
        for i in range(n):
            r[i] = np.dot(A[i, 0: n], x[0: n]) - f[i]
        if np.dot(r, r) < tol**2:
            break
        else:
            beta = -np.dot(r, As) / np.dot(s, As)
            s = r + beta * s
    return x, k

def fredholm(k, f, a, b, n):
    """
    Solution Fredholm integral equation of the second kind. k(x,s) is the kernel of the integral equation,
    f(x) is the right part, 0 ‹ x,s < b.
    Method with trapezoidal quadrature formula.
    """
    h = (b-a)/n
    A = np.identity(n+1, 'float')
    r = np.zeros((n+1), 'float')
    for i in range(n+1):
        x = a+i*h
        A[i, 0] = A[i, 0] - k(x, a) * h/2
        for j in range(1, n):
            s = a+j*h
            A[i, j] = A[i, j] - k(x, s)*h
        A[i, n] = A[i, n] - k(x, b)*h/2
        r[i] = f(x)
    y = solveLU(A, r)
    return y

def fredholm1(k, f, a, b, n, tol=1.0e-9):
    """
    Solution Fredhollm integral equation of the first kind.
    k(x,s) is the kernel of the integral equation,
    f(x) is the right part, 0 < x, s < b.
    CG is iterative method with rectangle quadrature formula
    """
    h = (b - a) / n
    A = np.zeros((n, n), 'float')
    r = np.zeros((n), 'float')
    for i in range(n):
        x = a + h / 2 + i * h
        r[i] = f(x)
        for j in range(n):
            s = a + h / 2 + j * h
            A[i, j] = k(x, s) * h
    # Symmetrization
    B = np.copy(A)
    rr = np.copy(r)
    for i in range(n):
        r[i] = np.dot(B[i, 0: n], rr[0: n])
        for j in range(n):
            A[i, j] = np.dot(B[i, 0: n], B[0: n, j])
    y, iter = cg(A, r, tol=tol)
    return y, iter


if __name__ == '__main__':
    # f = lambda x: 1 + 4 / (x**2 + 1)
    # g = lambda x: x**3
    # h = lambda x: 2**(-x)
    # a = -2
    # b = 2
    # intersection_fg = root(f, g,  a, b)
    # intersection_fh = root(f,  h,  a, b)
    # intersection_gh = root( g,  h,  a, b)
    # integral_f = integral( f, min(intersection_fg, intersection_fh), max(intersection_fg, intersection_fh))
    # integral_g = integral( g, min(intersection_fg, intersection_gh), max(intersection_fg, intersection_gh))
    # integral_h = integral( h, min(intersection_fh, intersection_gh), max(intersection_fh, intersection_gh))
    # area = integral_f - integral_g - integral_h
    # drawFunction(-2, 2, f, g, h)
    # print(area)
    def F(x):
        return 10.*(x[1] - x[0]**2) ** 2 + (1 - x[0])**2

    def GradF(x):
        gr = np.zeros((2), 'float')
        gr[0] = -40.*(x[1] - x[0]**2)*x[0] - 2.*(1 - x[0])
        gr[1] = 20.*(x[1] - x[0]**2)
        return gr
    x = np.linspace(-2., 2., 101)
    y = np.linspace(-1., 3., 101)
    X, Y = np.meshgrid(x, y)
    z = F([X, Y])
    v = np.linspace(0., 10., 21)
    plt.contour(x, y, z, v, cmap=plt.cm.gray)
    plt.colorbar()
    plt.show()
    # minumum function
    x0 = np.array([0., 0.1])
    xMin, nIt = grad(F, GradF, x0)
    print(str(xMin))
    print('xMin:', xMin)
    print('Number of iterations = ', nIt)
