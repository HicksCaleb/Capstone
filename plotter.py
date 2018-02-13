import numpy as np
import matplotlib.pyplot as plt
import sys, os

#inf = 'out4.tsv'
inf = sys.argv[1]
inFile = open(inf,'r')
y = [float(line.split('\t')[1])%1 for line in inFile]
plt.scatter([x for x in range(len(y))], y)
plt.show()
