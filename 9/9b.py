data = list(map(int, open("input.txt").read().split("\n")))

preamble = 25

for i in range(preamble, len(data)):
    num = data[i]
    found = False
    for j in range(i-preamble, i):
        for k in range(j+1, i):
            if data[j] + data[k] == num:
                found = True
                break
        if found:
            break
    if not found:
        invalid = num
        break

for i in range(len(data)):
    s = data[i]
    for j in range(i+1, len(data)):
        s += data[j]
        if s > invalid:
            break
        if s == invalid:
            l = data[i:j+1]
            print(min(l) + max(l))
            break
