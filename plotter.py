import numpy as np
import matplotlib.pyplot as plt
import sys, os

inf = 'out1.tsv'
inFile = open(inf,'r')
y = [float(line.split('\t')[1])%1 for line in inFile]
plt.scatter([x for x in range(256)], y)
plt.show()
