from math import inf
data = open("input.txt").read().split()

cycle = set()
num_rows = len(data)
num_cols = len(data[0])
for row_idx, row in enumerate(range(-(num_rows - 1) // 2, (num_rows - 1) // 2 + 1)):
    for col_idx, col in enumerate(range(-(num_cols - 1) // 2, (num_cols - 1) // 2 + 1)):
        if data[row_idx][col_idx] == "#":
            cycle.add((0, row, col))


def get_next_cycle(cycle):
    next_cycle = set()
    (min_level, max_level), (min_row, max_row), (min_col, max_col) = get_ranges(cycle)

    for level in range(min_level-1, max_level + 2):
        for row in range(min_row-1, max_row + 2):
            for col in range(min_col-1, max_col + 2):
                active_neighbours = 0
                for dl in range(-1, 2):
                    for dr in range(-1, 2):
                        for dc in range(-1, 2):
                            if (dl, dr, dc) == (0, 0, 0):
                                continue

                            new_level = level + dl
                            new_row = row + dr
                            new_col = col + dc
                            active_neighbours += 1 if (new_level, new_row, new_col) in cycle else 0

                if (level, row, col) in cycle:
                    if active_neighbours in (2, 3):
                        next_cycle.add((level, row, col))
                else:
                    if active_neighbours == 3:
                        next_cycle.add((level, row, col))

    return next_cycle

def get_ranges(cycle):
    min_level = inf
    min_row = inf
    min_col = inf
    max_level = -inf
    max_row = -inf
    max_col = -inf
    for (level, row, col) in cycle:
        max_level = max(max_level, level)
        max_row = max(max_row, row)
        max_col = max(max_col, col)
        min_level = min(min_level, level)
        min_row = min(min_row, row)
        min_col = min(min_col, col)

    return (min_level, max_level), (min_row, max_row), (min_col, max_col)


for _ in range(6):
    cycle = get_next_cycle(cycle)

print(len(cycle))
