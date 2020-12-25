card_public_key, door_public_key = map(int, open("input.txt").read().split())

door_loop_size = 0
tmp_value = 1
while tmp_value != door_public_key:
    door_loop_size += 1
    tmp_value *= 7
    tmp_value %= 20201227

encryption_key = 1
for _ in range(door_loop_size):
    encryption_key *= card_public_key
    encryption_key %= 20201227

print(encryption_key)
