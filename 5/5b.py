data = open("input.txt").read().split()

def calc_seat_id(seat):
    seat = seat.replace("F", "0")
    seat = seat.replace("B", "1")
    seat = seat.replace("R", "1")
    seat = seat.replace("L", "0")

    row = int(seat[:7], 2)
    column = int(seat[7:], 2)
    return row * 8 + column

all_seat_ids = []
for seat in data:
    seat_id = calc_seat_id(seat)
    all_seat_ids.append(seat_id)

min_seat_id = min(all_seat_ids)
max_seat_id = max(all_seat_ids)
for my_seat_id in range(min_seat_id, max_seat_id+1):
    if my_seat_id not in all_seat_ids:
        print(my_seat_id)
