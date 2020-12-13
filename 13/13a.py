from math import ceil
data = open("input.txt").read().split()

my_timestamp = int(data[0])
buses = [int(x) for x in data[1].split(",") if x != "x"]

best_float = 0
best = None
for bus in buses:
    wait_for_bus = my_timestamp / bus
    wait_for_bus_float = float(str(wait_for_bus-int(wait_for_bus))[1:])
    if wait_for_bus_float > best_float:
        best = bus
        best_float = wait_for_bus_float

print((ceil(my_timestamp / best) * best - my_timestamp) * best)
