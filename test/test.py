import os

def cnf_to_python(file):
	f=open(file)
	instance = []
	for line in f.readlines():
		line.replace('	',' ')
		line.strip('\n')
		line_tokens = line.split(' ')
		if line_tokens[0] in 'cp':
			continue
		else:
			instance.append([int(i) for i in line_tokens[0:-1]])
	return instance

#creates an array of testcases
def load_testcases():
	testcases = []
	for filename in os.listdir('testcases'):
		testcases.append(cnf_to_python(filename))
	return testcases

def run_testcases(testcases):
	

def main():
	testcases = load_testcases()
	run_testcases(testcases)

if __name__ == '__main__':
	main()

