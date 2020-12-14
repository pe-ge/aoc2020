data = open("input.txt").read().split("\n")

def to_binary_list(number, length=36):
    return bin(number)[2:].zfill(length)

def to_integer(binary_array):
    return int("".join(binary_array), 2)

def apply_mask(mask, number, length=36):
    new_number = [0] * length
    for i in range(len(mask)):
        if mask[i] == "X":
            new_number[i] = number[i]
        else:
            new_number[i] = mask[i]

    return new_number

memory = {}
for line in data:
    cmd, value = line.split(" = ")
    if cmd.startswith("mask"):
        bitmask = value
    else:
        address = int(cmd[4:-1])
        memory[address] = apply_mask(bitmask, to_binary_list(int(value)))

print(sum([to_integer(binary_value)for binary_value in memory.values()]))
