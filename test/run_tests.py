import os

def cnf_to_python(file):
	f=open(file)
	instance = []
	for line in f.readlines():
		line.replace('\t',' ')
		line.strip('\n')
		line_tokens = line.split(' ')
		if 'c' in line_tokens[0] or 'p' in line_tokens[0]:
			continue
		else:
			line_tokens = [int(i) for i in line_tokens[0:-1]]
			if len(line_tokens) == 0:
				continue
			instance.append(line_tokens)
	return instance

#creates an array of testcases
def load_testcases():
	testcases = []
	for filename in os.listdir('testcases'):
		testcases.append(cnf_to_python('testcases/'+filename))
	return testcases

def run_testcases(testcases):
	f = open('results_'+str(int(time.time()))+'.txt','a')
	for instance in testcases:
		for p in range(0.1,1,0.1):
			result = combo_soln(testcase, p)
			f.write(str(result)) 
	f.close()



def main():
	testcases = load_testcases()
	run_testcases(testcases)

if __name__ == '__main__':
	main()

