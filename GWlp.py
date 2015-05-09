import scipy
import math

def satLP(instance, literals):
    counter = len(instance)
    rowlen = counter + len(literals)
    A = []
    b = [0]*counter
    c = [-1] * counter
    assigned = {}
    for i in range(0, len(instance)):
        tmp = [0] * rowlen
        clause = instance[i]
        tmp[i] = 1
        for literal in clause:
            if math.fabs(literal) not in assigned.keys():
                counter+=1
                assigned[math.fabs(literal)] = counter
            if literal > 0:
                tmp[assigned[literal]] = -1
            else:
                tmp[assigned[math.fabs(literal)]] = 1
                b[i] += 1
    
    print A
    print b
    print c
