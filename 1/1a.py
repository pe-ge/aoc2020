data = list(map(int, open("input.txt").read().split()))
for i in range(len(data)-1):
    for j in range(i+1, len(data)):
        if data[i] + data[j] == 2020:
            print(data[i] * data[j])
