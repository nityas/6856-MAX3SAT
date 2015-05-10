from literal import *
from GWlp import *
from dpll import *
import subprocess

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
    print literals(inp)
    print len(literals(inp))
    print "#yolo"
    #dpll_sol = dpll(inp, literals(inp))[0]
    #result_str += "\nExact Solution: "+ str(naive_sol)
    if gw_sol > naive_sol:
        result_str += "\nGW Better: "+ str(gw_sol)
    elif gw_sol == naive_sol:
        result_str += "\nEqual: "+ str(gw_sol)
    else:
        result_str += "\nNaive Better: "+ str(naive_sol)
    return result_str+="\n\n"

def exact_soln_info(filename):
    args = ["java", "-jar", "sat4j-maxsat.jar","testcases/"+filename]
    out = subprocess.check_output()
    num_unsatisfied = re.findall("objective function=.*",out)[0].split('=')[1])
    num_clauses = re.findall(" org.sat4j.minisat.constraints.cnf.OriginalWLClause => .*",out)[0].split('=>')[1])
    num_satisfied = num_clauses - num_unsatisfied
    result_str = "EXACT SOLUTION: \ntotal clauses: "+num_clauses+"clauses satisfied: "+num_satisfied
    return result_str

