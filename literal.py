import random
import pycosat

#generate a random assignment
def round(inp,p):
	num_literals = num_literals(inp)
	assignment = [0 for i in range(num_literals)]
	for literal in range(num_literals):
		r = random.random()
		# set to false
		if random > p:
			assignment[literal-1]= -1*literal
		# set to true with probability p
		else:
			assignment[literal-1] = 1*literal
	return assignment


def num_literals(inp):
	return max([abs(item) for sublist in inp for item in sublist])

def num_clauses(inp):
	return len(inp)

def satisfied_clauses(inp, assignment):
	satisfied_clauses = 0
	for clause in inp:
		for literal in clause:
			if cmp(literal*assignment[literal-1],0) > 0:
				satisfied_clauses += 1
				break
	return satisfied_clauses




