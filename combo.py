from literal import *
from GWlp import *
from dpll import *
import subprocess
import time
import re

# def combo_soln(inp,gw_sol, p=0.5):
#       naive_sol = naive_max_sat(inp,p)
#       if gw_sol > naive_sol:
#               return ("gw",gw_sol,naive_sol)
#       elif gw_sol == naive_sol:
#               return ("same",gw_sol,naive_sol)
#       else:
#               return ("naive",gw_sol,naive_sol)


def combo_max_sat(inp, gw_sol, p=0.5):
    result_str = "\nGW Solution: "+ str(gw_sol)

    naive_sol = naive_max_sat(inp,p)
    result_str += "\nNaive Approx Solution: "+ str(naive_sol)
    if gw_sol > naive_sol:
        result_str += "\nGW Better: "+ str(gw_sol)
    elif gw_sol == naive_sol:
        result_str += "\nEqual: "+ str(gw_sol)
    else:
        result_str += "\nNaive Better: "+ str(naive_sol)
    return result_str+"\n\n"

def exact_soln_info(filename):
    args = ["java", "-jar", "sat4j-maxsat.jar",filename]
    t1 = time.time()
    out = subprocess.check_output(args)
    t2 = time.time()
    num_unsatisfied = re.findall("objective function=.*",out)[0].split('=')[1]
    num_clauses = int(re.findall(" org.sat4j.minisat.constraints.cnf.OriginalWLClause => .*",out)[0].split('=>')[1])
    num_satisfied = num_clauses - int(num_unsatisfied)
    #result_str = "\nEXACT SOLUTION:\ntotal clauses: "+num_clauses+"\nclauses satisfied: "+str(num_satisfied)
    return num_clauses,num_satisfied,t2-t1
