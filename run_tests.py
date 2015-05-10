import os
import time
from combo import *
import numpy as np
from literal import *

def getstats(results):
    return np.amin(results),np.amax(results),np.mean(results),np.median(results)

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
    dirtype='hard'
    for filename in os.listdir(dirtype):
        testcases.append((dirtype+'/'+filename,cnf_to_python(dirtype+'/'+filename)))
    return testcases

def run_testcases(testcases):
    time_suffix = str(int(time.time()))
    f = open('readable_results_'+time_suffix+'.txt','aw')
    resultsdict = {}
    for filename, instance in testcases:
        f.write(filename+'\n')
        f.flush()
        var_prob, status = GW(instance)
        results_gw = []
        results_naive = []
        for p in range(0,11,1):
            rounded = rand_round(instance, var_prob)
            gw_sol = satisfied_clauses(instance, rounded)
            naive_sol = naive_max_sat(instance,float(p)/10)
            results_gw.append(gw_sol)
            results_naive.append(naive_sol)

        num_clauses, num_satisfied = exact_soln_info(filename)
        k= len(instance[0])
        literals = num_literals(instance)
        resultsdict[filename] = [k, literals, num_clauses, num_satisfied, getstats(results_gw), getstats(results_naive)]
        f.write(str(resultsdict[filename])+'\n')
        if status == 1:
            f.write("Recursion depth exceeded. Need to run again\n")
        f.flush()
    f.close()
    f2 = open('results_object_'+time_suffix+'.json','aw')
    f2.write(str(resultsdict))
    f2.close()
    



def main():
    testcases = load_testcases()
    run_testcases(testcases)

if __name__ == '__main__':
        main()

