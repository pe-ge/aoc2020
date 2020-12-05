data = open("input.txt").read().split()

def calc_seat_id(seat):
    seat = seat.replace("F", "0")
    seat = seat.replace("B", "1")
    seat = seat.replace("L", "0")
    seat = seat.replace("R", "1")

    row = int(seat[:7], 2)
    column = int(seat[7:], 2)
    return row * 8 + column

highest_seat_id = 0
for seat in data:
    seat_id = calc_seat_id(seat)
    highest_seat_id = max(seat_id, highest_seat_id)

print(highest_seat_id)
