groups = open("input.txt").read().split("\n\n")

count = 0
for group in groups:
    count += len(set(group.replace("\n", "")))

print(count)
