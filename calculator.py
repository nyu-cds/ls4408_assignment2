# -----------------------------------------------------------------------------
# calculator.py
'''
Origin time by Cprofiler:2.424s
Improved time by Cprofiler: 0.019s
Speedup by Cprofiler:127.57894736842105

Origin time by line-profiler:3.79763s
Improved time by line-profiler: 0.0143273s
Speedup by line-profiler:265.06250305361095s

Use numpy to improve the performance

hypotenuse is the orginal function, and hypothenuse2 is the improved function using numpy
As I replace original function in hypotenuse by numpy methods, and cProfile will not time 
numpy method specifically in hypothenuse2, I prefer using line_profiler for comparison.


Using Cprofiler for hypotenuse
1000014 function calls in 2.424 seconds


Using Cprofiler for hypotenuse2
4 function calls in 0.019 seconds

   
Using line_profiler for hypotenuse
Timer unit: 3.95062e-07 s

Total time: 3.79763 s
File: <ipython-input-2-375321e4461f>
Function: hypotenuse at line 42

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    42                                           def hypotenuse(x,y):
    43                                               """
    44                                               Return sqrt(x**2 + y**2) for two arrays, a and b.
    45                                               x and y must be two-dimensional arrays of the same shape.
    46                                               """
    47         1      2520318 2520318.0     26.2      xx = multiply(x,x)
    48         1      2473303 2473303.0     25.7      yy = multiply(y,y)
    49         1      2565631 2565631.0     26.7      zz = add(xx, yy)
    50         1      2053509 2053509.0     21.4      return sqrt(zz)


Using line_profiler for improved hypotenuse2
Timer unit: 3.95062e-07 s

Total time: 0.0143273 s
File: <ipython-input-2-375321e4461f>
Function: hypotenuse2 at line 52

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    52                                           def hypotenuse2(x,y):
    53         1         9149   9149.0     25.2  	xx=np.multiply(x,x)
    54         1         8568   8568.0     23.6  	yy=np.multiply(y,y)
    55         1         9544   9544.0     26.3  	zz=np.add(xx,yy)
    56         1         9005   9005.0     24.8  	return np.sqrt(zz)
 '''
# ----------------------------------------------------------------------------- 
import numpy as np

def add(x,y):
    """
    Add two arrays using a Python loop.
    x and y must be two-dimensional arrays of the same shape.
    """
    m,n = x.shape
    z = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            z[i,j] = x[i,j] + y[i,j]
    return z


def multiply(x,y):
    """
    Multiply two arrays using a Python loop.
    x and y must be two-dimensional arrays of the same shape.
    """
    m,n = x.shape
    z = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            z[i,j] = x[i,j] * y[i,j]
    return z


def sqrt(x):
    """
    Take the square root of the elements of an arrays using a Python loop.
    """
    from math import sqrt
    m,n = x.shape
    z = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            z[i,j] = sqrt(x[i,j])
    return z


def hypotenuse(x,y):
    """
    Return sqrt(x**2 + y**2) for two arrays, a and b.
    x and y must be two-dimensional arrays of the same shape.
    """
    xx = multiply(x,x)
    yy = multiply(y,y)
    zz = add(xx, yy)
    return sqrt(zz)

def hypotenuse2(x,y):
	#using numpy to replace the original code
	xx=np.multiply(x,x)
	yy=np.multiply(y,y)
	zz=np.add(xx,yy)
	return np.sqrt(zz)