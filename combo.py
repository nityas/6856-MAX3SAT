from literal import *
from GWlp import *
from dpll import *

# def combo_soln(inp,gw_sol, p=0.5):
#       naive_sol = naive_max_sat(inp,p)
#       if gw_sol > naive_sol:
#               return ("gw",gw_sol,naive_sol)
#       elif gw_sol == naive_sol:
#               return ("same",gw_sol,naive_sol)
#       else:
#               return ("naive",gw_sol,naive_sol)

def combo_max_sat(inp, gw_sol, dpll_sol, p=0.5):
        result_str = "\nGW Solution: "+ str(gw_sol)

        naive_sol = naive_max_sat(inp,p)
        result_str += "\nNaive Approx Solution: "+ str(naive_sol)
        print "finished naive"
        result_str += "\nExact Solution: "+ str(dpll_sol)

        if gw_sol > naive_sol:
                result_str += "\nGW Better: "+ str(gw_sol)
        elif gw_sol == naive_sol:
                result_str += "\nEqual: "+ str(gw_sol)
        else:
                result_str += "\nNaive Better: "+ str(naive_sol)
        result_str+="\n\n"
        return result_str
