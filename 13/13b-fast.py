# rosettacode.org/wiki/Chinese_remainder_theorem

from functools import reduce

def egcd(m, n):
    old_r, r = m, n
    old_t, t = 0, 1

    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_t, t = t, old_t - q * t

    return old_t

data = open("input.txt").read().split()

n = []
a = []
for idx, val in enumerate(data[1].split(",")):
    if val == "x":
        continue
    n.append(int(val))
    a.append(-idx)

N = reduce(lambda x, y: x * y, n)

solution = 0
for i in range(len(n)):
    s = egcd(n[i], N//n[i])
    solution += a[i] * s * (N // n[i])

print(solution % N)
