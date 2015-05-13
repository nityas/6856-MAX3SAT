import matplotlib.pyplot as plt
import json
import yaml
import numpy as np

fname="results_object_80v.json"
fname2="results_object_70v.json"
def k_vs_performance(data):
    rel_data = [(float(row[1]),float(row[3]),float(row[7]),float(row[11])) 
                for row in data.values()]

    data_vals = {}
    for row in rel_data:
        kval,best,gw,naive = row
        if kval in data_vals:
            data_vals[kval].append((gw/best,naive/best))
        else:
            data_vals[kval] = [(gw/best,naive/best)]

    k = []
    gw_means = []
    naive_means = []
    for k_val in data_vals.keys():
        k.append(k_val)
        gw_means.append(np.mean([i[0] for i in data_vals[k_val]]))
        naive_means.append(np.mean([i[1] for i in data_vals[k_val]]))
    gw_means.reverse()
    naive_means.reverse()
    k.reverse()
    fig, ax = plt.subplots()
    ax.set_xticks([k[i]+2.5 for i in range(len(k))])
    ax.set_xticklabels( ('70','80') )
    r1 = plt.bar(k, gw_means, 2.5, color='r')
    r2 = plt.bar([k[i]+2.5 for i in range(len(k))], naive_means, 2.5, color='b')
    plt.axis([65,90,0.75,1.0])
    ax.legend( (r1[0], r2[0]), ('GW', 'Naive') )
    plt.ylabel('approximation')
    plt.xlabel('num_vars')
    plt.title('Accuracy vs. Number of Variables for Competition 3-MAX SAT')
    plt.show()


def main():
    with open(fname) as data_file:
        data = yaml.safe_load(data_file)
    with open(fname2) as data_file:
        data2 = yaml.safe_load(data_file)
    data3 = data.copy()
    data3.update(data2)
    k_vs_performance(data3)

if __name__ == '__main__':
    main()
