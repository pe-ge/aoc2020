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
        print(num)
        break
