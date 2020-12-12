data = open("input.txt").read().split()

direction = 90
north = 0
east = 0

def rotate(direction, action, value):
    if action == "R":
        return (direction + value) % 360
    if action == "L":
        return (direction - value) % 360

def forward(north, east, direction, value):
    if direction == 0:
        return north + value, east
    if direction == 90:
        return north, east + value
    if direction == 180:
        return north - value, east
    if direction == 270:
        return  north, east - value

for line in data:
    action = line[0]
    value = int(line[1:])

    if action == "N":
        north += value
    elif action == "S":
        north -= value
    elif action == "E":
        east += value
    elif action == "W":
        east -= value
    elif action in ("L", "R"):
        direction = rotate(direction, action, value)
    elif action == "F":
        north, east = forward(north, east, direction, value)

print(abs(north) + abs(east))
