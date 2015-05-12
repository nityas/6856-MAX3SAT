import matplotlib.pyplot as plt
import json
import yaml
import numpy as np

fname="results_object_hard.json"
def k_vs_performance(data):
    rel_data = [(float(row[0]),float(row[3]),float(row[7]),float(row[11])) 
                for row in data.values()]

    data_vals = {}
    for row in rel_data:
        kval,best,gw,naive = row
        if kval in data_vals:
            data_vals[kval].append((gw/best,naive/best))
        else:
            data_vals[kval] = [(gw/best,naive/best)]

    k = []
    gw_vals = []
    naive_vals = []
    for k_val in data_vals.keys():
        k.append(k_val)
        gw_vals += [i[0] for i in data_vals[k_val]]
        naive_vals += [i[1] for i in data_vals[k_val]]

    #fig, ax = plt.subplots()
    plt.hist(gw_vals, 10, facecolor='red')
    #plt.hist(naive_vals, 10, facecolor='blue')
    plt.axis([0.9,1.0,1,100])
    plt.ylabel('Number of testcases')
    plt.xlabel('approximation')
    plt.title('GW Accuracy Distribution for Hard Random Testcase Set')
    plt.show()


def main():
    with open(fname) as data_file:
        data = yaml.safe_load(data_file)
    k_vs_performance(data)

if __name__ == '__main__':
    main()
