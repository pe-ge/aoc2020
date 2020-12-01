data = list(map(int, open("input.txt").read().split()))
for i in range(len(data)-2):
    for j in range(i+1, len(data)-1):
        for k in range(j+1, len(data)):
            if data[i] + data[j] + data[k] == 2020:
                print(data[i] * data[j] * data[k])
