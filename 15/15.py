from collections import defaultdict


def solve(num_turns, data=[12, 1, 16, 3, 11, 0]):
    idxs = defaultdict(list)
    for idx, val in enumerate(data[:-1]):
        idxs[val].append(idx)

    for turn in range(len(data)+1, num_turns+2):
        last_spoken = data[-1]
        if not idxs[last_spoken]:
            data.append(0)
        else:
            last_spoken_idx = idxs[last_spoken][-1] + 1
            new_spoken = (turn - 1) - last_spoken_idx

            data.append(new_spoken)
        idxs[last_spoken].append(len(data)-2)

    return last_spoken


print(f"Part 1): {solve(2020)}")
print(f"Part 2): {solve(30000000)}")
