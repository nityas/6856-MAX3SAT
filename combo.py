from literal import *
from GWlp import *

def combo_max_sat(inp,p=0.5):
	gw_sol = gw_max_sat(inp)
	result_str = "\nGW Solution: "+ gw_sol

	naive_sol = naive_max_sat(inp,p)
	result_str += "\nNaive Approx Solution: "+ naive_sol

	dpll_sol = dpll(inp, literals(inp))[0]
	result_str += "\nExact Solution: "+ naive_sol

	if gw_sol > naive_sol:
		result_str += "\nGW Better: "+ gw_sol
	elif gw_sol == naive_sol:
		result_str += "\nEqual: "+ gw_sol
	else:
		result_str += "\nNaive Better: "+ naive_sol
	return result_str