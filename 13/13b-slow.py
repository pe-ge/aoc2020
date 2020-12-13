data = open("example.txt").read().split()

ts = []
delta = -1
for x in data[1].split(","):
    delta += 1
    if x == "x":
        continue

    ts.append([delta, int(x)])

def check_number(number, ts):
    for t in ts:
        if (number + t[0]) % t[1] != 0:
            return False

    return True

ts = sorted(ts, key=lambda x: x[1], reverse=True)

m = 1
while True:
    number = ts[0][1] * m - ts[0][0]
    if check_number(number, ts):
        break
    m += 1

print(number)
