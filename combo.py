from literal import *
from GWlp import *

def combo_soln(inp,p=0.5):
	gw_sol = GW(inp)
	naive_sol = naive_max_sat(inp,p)
	if gw_sol > naive_sol:
		return ("gw",gw_sol,naive_sol)
	elif gw_sol == naive_sol:
		return ("same",gw_sol,naive_sol)
	else:
		return ("naive",gw_sol,naive_sol)
