from collections import Counter
import numpy as np

data = np.loadtxt("input.txt", dtype="int")
data = np.sort(np.append(data, [0, max(data)+3]))

diffs = "".join(map(str, list(np.diff(data))))

diffs = diffs.replace("1111", "7")
diffs = diffs.replace("111", "4")
diffs = diffs.replace("11", "2")

c = Counter(diffs)
print(7**c["7"] * 2**(2*c["4"]) * 2**c["2"])
