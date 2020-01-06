# 创建一个模块，包含一个阶乘函数f1(n)、一个列表删值函数f2(lst,x),一个等差数列求和函数f3(a,d,n)

def f1(n):
    y = 1
    for i in range(1,n+1):
        y = y * i
    return y
# 创建阶乘函数f1(n)

def f2(lst,x):
    while x in lst:
        lst.remove(x)
    return x
# 创建列表删值函数f2(lst,x)

def f3(a,d,n):
    an = a
    s = 0
    for i in range(n-1):
        an = an + d
        s = s + an
    return s
# 创建等差数列求和函数f3(a,d,n)
# 创建模块testmodel2，包括三个函数