import random

#######
#generate a random assignment with each var set to 
#true with probability p, where p is either a list
#of assignment probabilites or a single value
#######
def round(inp,p):
	num_literals = num_literals(inp)
	if type(p) is float:
		p_is_list = False
	elif (type(p) is dict) and (len(p) == num_literals):
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

def num_literals(inp):
	return len(literals(inp))

def literals(inp):
	return list(set([abs(literal) for clause in inp for literal in clause]))

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




