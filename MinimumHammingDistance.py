import random
import sys
import numpy as np
import pandas as pd
from hamming_parctice import hamming

df = pd.read_csv('sample.csv', names=['work', 'bin'])


minimum = sys.maxsize
count = 0
for i in range(0, df.shape[0]):
	for j in range(i+1, df.shape[0]):
		hd = hamming(df.iloc[i,1], df.iloc[j,1])
		print(count, "(", df.iloc[i,0], df.iloc[j,0],")hamming_distane:", hd)
		if minimum > hd:
			minimum = hd;
		count += 1
print("min hamming distance",minimum)
