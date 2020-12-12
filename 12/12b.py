data = open("input.txt").read().split()

s_north = 0
s_east = 0
w_north = 1
w_east = 10

def rotate(w_north, w_east, action, value):
    for _ in range(value // 90):
        if action == "R":
            w_north, w_east = -w_east, w_north
        if action == "L":
            w_north, w_east = w_east, -w_north

    return w_north, w_east

def forward(s_north, s_east, w_north, w_east, value):
    return s_north + w_north * value, s_east + w_east * value

for line in data:
    action = line[0]
    value = int(line[1:])

    if action == "N":
        w_north += value
    elif action == "S":
        w_north -= value
    elif action == "E":
        w_east += value
    elif action == "W":
        w_east -= value
    elif action in ("L", "R"):
        w_north, w_east = rotate(w_north, w_east, action, value)
    elif action == "F":
        s_north, s_east= forward(s_north, s_east, w_north, w_east, value)

print(abs(s_north) + abs(s_east))
