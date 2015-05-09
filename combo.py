from literal import *
from GWlp import *

# def combo_soln(inp,gw_sol, p=0.5):
# 	naive_sol = naive_max_sat(inp,p)
# 	if gw_sol > naive_sol:
# 		return ("gw",gw_sol,naive_sol)
# 	elif gw_sol == naive_sol:
# 		return ("same",gw_sol,naive_sol)
# 	else:
# 		return ("naive",gw_sol,naive_sol)

def combo_max_sat(inp, gw_sol, p=0.5):
	result_str = "\nGW Solution: "+ int(gw_sol)

	naive_sol = naive_max_sat(inp,p)
	result_str += "\nNaive Approx Solution: "+ int(naive_sol)

	dpll_sol = dpll(inp, literals(inp))[0]
	result_str += "\nExact Solution: "+ int(naive_sol)

	if gw_sol > naive_sol:
		result_str += "\nGW Better: "+ int(gw_sol)
	elif gw_sol == naive_sol:
		result_str += "\nEqual: "+ int(gw_sol)
	else:
		result_str += "\nNaive Better: "+ int(naive_sol)
	return result_str
