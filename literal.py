import random

def round(literal,p):
	num_literals = num_literals(literal)
	assignment = []
	for literal in range(num_literals):
		r = random.random()
		# set to false
		if random > p:
			assignment.append(-1*literal)
		else:
			assignment.append(1*literal)
	return assignment


def num_literals(literal):
	return max([abs(item) for sublist in a for item in sublist])

def num_clauses(literal):
	return len(literal)