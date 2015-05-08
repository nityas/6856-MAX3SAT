import copy
def dpll(instance, setvar = [], setval={}):
    instance.sort(key = lambda s: len(s)) #sort by length,
                                          #so single var clauses are first
    counter = 0
    for clause in instance:
        if len(clause) == 1:
            counter+=1
            #setvar.append(clause[0]) #may need to check that if we have i and -i, output unsatisfiable
            #print setvar
            if clause[0] > 0:
                setval[clause[0]] = 1
            else:
                setval[clause[0] * -1] = -1
        else:
            break
    setvar.sort()
    cvar = setvar[0]
    setvar = setvar[1:]
    numsatisfied, assign = recurse(instance[counter:], cvar, setvar, setval)
    numsatisfied += counter
    print numsatisfied, assign

def recurse(instance, cvar, setvar, setval):
    notsatisfied = []
    satcounter = 0
    numsatisfiedpos = 0
    numsatisfiedneg = 0
    assignpos = 0
    assignneg = 0
    if cvar in setval.keys(): #the variable has already had it's value set, move on to next variable
                              #count number of clauses satisfied?
        cvar = cvar * setval[cvar]
        for clause in instance:
            if cvar not in clause:
                notsatisfied.append(clause)
            else:
                satcounter+=1
        if len(setvar) > 0:
            counter, assign = recurse(notsatisfied, setvar[0], setvar[1:], setval)
            return counter+satcounter, assign
        else:
            return satcounter, copy.deepcopy(setval)
    else:
        #try setting to true
        tmp = copy.deepcopy(setval)
        tmp[cvar] = 1
        for clause in instance:
            if cvar not in clause:
                notsatisfied.append(clause)
            else:
                satcounter+=1
        if len(setvar) > 0:
            numsatisfiedpos, assignpos = recurse(notsatisfied, setvar[0], setvar[1:], tmp)
            numsatisfiedpos += satcounter
        else:
            numsatisfiedpos = satcounter
            assignpos = tmp
        #try setting to false
        setval[cvar] = -1
        notsatisfied = []
        satcounter = 0
        cvar = -1 * cvar
        for clause in instance:
            if cvar not in clause:
                notsatisfied.append(clause)
            else:
                satcounter+=1
        
        if len(setvar) > 0:
            numsatisfiedneg, assignneg = recurse(notsatisfied, setvar[0], setvar[1:], setval)
            numsatisfiedneg+=satcounter
        else:
            numsatisfiedneg = satcounter
            assignneg = setval
        if numsatisfiedpos > numsatisfiedneg:
            return numsatisfiedpos, assignpos
        else:
            return numsatisfiedneg, assignneg
        
    
