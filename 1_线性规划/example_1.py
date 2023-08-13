"""_summary_
    例题1.1 
"""
from scipy.optimize import linprog

c = [-4,-3]                     # 价值向量
A = [[2,1],[1,1],[0,1]]         # 不等式矩阵
b = [10,8,7]                    # 不等式向量
x1 = [0,None]
x2 = [0,None]

res = linprog(c,A,b,bounds=(x1,x2))
print(res)