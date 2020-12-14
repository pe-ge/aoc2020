data = open("input.txt").read().split("\n")

def to_binary_list(number, length=36):
    return bin(number)[2:].zfill(length)

def to_integer(binary_list):
    return int("".join(binary_list), 2)

def apply_mask(mask, address, length=36):
    new_address = [0] * length
    for i in range(len(mask)):
        if mask[i] == "0":
            new_address[i] = address[i]
        else:
            new_address[i] = mask[i]

    return new_address

def update_memory(memory, address, value, idx=0):
    if idx == len(address):
        memory[to_integer(address)] = value
        return

    if address[idx] == "X":
        for bit in ("0", "1"):
            address[idx] = bit
            update_memory(memory, address, value, idx+1)
        address[idx] = "X"
    else:
        update_memory(memory, address, value, idx+1)

memory = {}
for line in data:
    cmd, value = line.split(" = ")
    if cmd.startswith("mask"):
        bitmask = value
    else:
        address = to_binary_list(int(cmd[4:-1]))
        address = apply_mask(bitmask, address)
        update_memory(memory, address, to_binary_list(int(value)))

print(sum([to_integer(binary_list)for binary_list in memory.values()]))
