import random
from combo import *

def literals(inp):
	return list(set([abs(literal) for clause in inp for literal in clause]))

def num_literals(inp):
	return len(literals(inp))

def num_clauses(inp):
	return len(inp)

#counts number of satisfied clauses
def satisfied_clauses(inp, assignment):
	satisfied_clauses = 0
	for clause in inp:
		for literal in clause:
			if cmp(literal*assignment[literal],0) > 0:
				satisfied_clauses += 1
				break
	return satisfied_clauses

#Actual solver
def naive_max_sat(inp,p=0.5):
	rounded_assignment = rand_round(inp,p)
	return satisfied_clauses(inp,rounded_assignment)


#######
#generate a random assignment with each var set to 
#true with probability p, where p is either a list
#of assignment probabilites or a single value
#######
def rand_round(inp,p=0.5):
	num_lit = num_literals(inp)
	if type(p) is float:
		p_is_list = False
	elif (type(p) is dict) and (len(p) == num_lit):
		p_is_list = True
	else:
		return "invalid p"

	assignment = {}
	for literal in literals(inp):
		r = random.random()
		if p_is_list:
			p_x = p[literal]
		else:
			p_x = p
		# set to false
		if random > p_x:
			assignment[literal]= -1
		# set to true with probability p
		else:
			assignment[literal] = 1
	return assignment
