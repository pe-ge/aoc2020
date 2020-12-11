from itertools import product

seats = open("input.txt").read().split()

def outside(seats, row, col):
    return row < 0 or col < 0 or row >= len(seats) or col >= len(seats[0])

def get_seat(seats, row, col):
    if outside(seats, row, col):
        return "."
    return seats[row][col]

def occupied(seats, row, col):
    result = 0
    for dr, dc in product([-1, 0, 1], repeat=2):
        if dr == 0 and dc == 0:
            continue
        next_row = row
        next_col = col
        while not outside(seats, next_row, next_col):
            next_row += dr
            next_col += dc
            seat = get_seat(seats, next_row, next_col)
            if seat == "#":
                result += 1
            if seat != ".":
                break
    return result

def step(seats):
    next_seats = []
    total_occupied = 0
    for row in range(len(seats)):
        next_seats.append([])
        for col in range(len(seats[row])):
            seat = get_seat(seats, row, col)
            occ = occupied(seats, row, col)
            if seat == "L" and occ == 0:
                next_seats[-1].append("#")
            elif seat == "#" and occ >= 5:
                next_seats[-1].append("L")
            else:
                next_seats[-1].append(seat)

            if next_seats[-1][-1] == "#":
                total_occupied += 1

    return next_seats, total_occupied

while True:
    next_seats, total_occupied = step(seats)
    if next_seats == seats:
        break
    seats = next_seats

print(total_occupied)
