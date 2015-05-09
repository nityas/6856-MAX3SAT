import sys
sys.path.insert(1, "/Library/Python/2.7/site-packages")
from scipy.optimize import linprog
from literal import *
import math
import test

def GW(instance):
    lit = literals(instance)
    A, b, c, assign = satLP(instance, lit)
    var_prob = solveLP(A, b, c, assign)
    return var_prob
    
def satLP(instance, literals):
    counter = len(instance)
    rowlen = counter + len(literals)
    A = []
    b = [0]*counter
    c = [-1] * counter + [0] * len(literals)
    assigned = {}
    for i in range(0, len(instance)):
        tmp = [0] * rowlen
        clause = instance[i]
        tmp[i] = 1
        for literal in clause:
            if math.fabs(literal) not in assigned.keys():
                assigned[int(math.fabs(literal))] = counter
                counter+=1
            if literal > 0:
                tmp[assigned[literal]] = -1
            else:
                tmp[assigned[int(math.fabs(literal))]] = 1
                b[i] += 1
        A.append(tmp)
    inverse_assign = {}
    for i in assigned.keys():
        inverse_assign[assigned[i]] = i
    return A, b, c, inverse_assign

def solveLP(A, b, c, assigned):
    rowlen = len(A[0])
    bound = ()
    for i in range(0, rowlen):
        bound +=((0,1),)
    res = linprog(c, A_ub=A, b_ub=b, bounds = bound, options={"disp":True})
    x = res.x
    num_clauses = len(b)
    var_LP_val = {}
    for i in range(num_clauses, rowlen):
        var_LP_val[assigned[i]] = x[i]
    return var_LP_val
        
