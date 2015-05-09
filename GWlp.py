from scipy.optimize import linprog
import math
import test

def satLP(instance, literals):
    counter = len(instance)
    rowlen = counter + len(literals)
    print rowlen
    A = []
    b = [0]*counter
    c = [-1] * counter + [0] * len(literals)
    assigned = {}
    for i in range(0, len(instance)):
        tmp = [0] * rowlen
        print rowlen
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
                print i
                b[i] += 1
        A.append(tmp)
    return A, b, c

def solveLP(A, b, c):
    rowlen = len(A[0])
    bound = ()
    for i in range(0, rowlen):
        bound +=((0,1),)
    res = linprog(c, A_ub=A, b_ub=b, bounds = bound, options={"disp":True})
    print res
