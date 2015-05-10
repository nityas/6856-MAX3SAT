import copy
import sys
##An exact Max-SAT solver
def dpll(instance, set_var, set_val={}):
    sys.setrecursionlimit(1500)
    instance.sort(key = lambda s: len(s)) #sort by length,
                                          #so single var clauses are first
    counter = 0
    for clause in instance:
        if len(clause) == 1:
            counter+=1
            #set_var.append(clause[0]) #may need to check that if we have i and -i, output unsatisfiable
            #print set_var
            if clause[0] > 0:
                set_val[clause[0]] = 1
            else:
                set_val[clause[0] * -1] = -1
        else:
            break
    set_var.sort()
    cvar = set_var[0]
    set_var = set_var[1:]
    num_satisfied, assign = recurse(instance[counter:], cvar, set_var, set_val)
    num_satisfied += counter
    return (num_satisfied, assign)

def recurse(instance, cvar, set_var, set_val):
    notsatisfied = []
    satcounter = 0
    num_satisfied_pos = 0
    num_satisfied_neg = 0
    assign_pos = 0
    assign_neg = 0
    if cvar in set_val.keys(): #the variable has already had it's value set, move on to next variable
                              #count number of clauses satisfied?
        cvar = cvar * set_val[cvar]
        for clause in instance:
            if cvar not in clause:
                notsatisfied.append(clause)
            else:
                satcounter+=1
        if len(set_var) > 0:
            counter, assign = recurse(notsatisfied, set_var[0], set_var[1:], set_val)
            return counter+satcounter, assign
        else:
            return satcounter, copy.deepcopy(set_val)
    else:
        #try setting to true
        tmp = copy.deepcopy(set_val)
        tmp[cvar] = 1
        for clause in instance:
            if cvar not in clause:
                notsatisfied.append(clause)
            else:
                satcounter+=1
        if len(set_var) > 0:
            num_satisfied_pos, assign_pos = recurse(notsatisfied, set_var[0], set_var[1:], tmp)
            num_satisfied_pos += satcounter
        else:
            num_satisfied_pos = satcounter
            assign_pos = tmp
        #try setting to false
        set_val[cvar] = -1
        notsatisfied = []
        satcounter = 0
        cvar = -1 * cvar
        for clause in instance:
            if cvar not in clause:
                notsatisfied.append(clause)
            else:
                satcounter+=1
        
        if len(set_var) > 0:
            num_satisfied_neg, assign_neg = recurse(notsatisfied, set_var[0], set_var[1:], set_val)
            num_satisfied_neg+=satcounter
        else:
            num_satisfied_neg = satcounter
            assign_neg = set_val
        if num_satisfied_pos > num_satisfied_neg:
            return num_satisfied_pos, assign_pos
        else:
            return num_satisfied_neg, assign_neg
        
    
def brute_force(instance, set_var):
    pass
