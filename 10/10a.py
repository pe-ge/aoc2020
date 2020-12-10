import numpy as np
from collections import Counter

data = np.loadtxt("input.txt", dtype="int")
data = np.sort(np.append(data, [0, max(data)+3]))

diffs = Counter(np.diff(data))
print(diffs[1] * diffs[3])
