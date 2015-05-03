def dpll(instance, setvar = [], setval={}):
    instance.sort(key = lambda s: len(s)) #sort by length,
                                          #so single var clauses are first
    for clause in instance:
        if len(clause) == 1:
            setvar.append(clause[0]) #may need to check that if we have i and -i, output unsatisfiable
            print setvar
            if clause[0] > 0:
                setval[clause[0]] = 1
            else:
                setval[clause[0] * -1] = -1
        else:
            break
    setvar.sort()
    for i in range(1, maxValOfVariable):
        
    
    
