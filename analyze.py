import numpy as np
import pandas as pd

ROWS = 5
COLUMNS = 5
DEPTH = 4

DATA_SEPARATOR = "\t"

data = np.zeros((ROWS, COLUMNS, DEPTH))
avg = np.zeros((ROWS, COLUMNS))

with open("allresults", 'r') as results:
    experiment = 0
    for idx, line in enumerate(results.readlines()):
        methodResult = [float(s.strip()) for s in line.split("\t")[1:]]
        if methodResult == []:
            experiment += 1
            continue
        method = idx % (ROWS+1)
        data[method, :, experiment] = methodResult

avg = np.sum(data, axis=2)/DEPTH
print(avg)
