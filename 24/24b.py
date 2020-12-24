from math import inf
from collections import defaultdict

raw_steps = open("input.txt").read().split()


def parse_raw_steps(steps):
    idxs = {}

    # first find ne, nw, se, sw
    while True:
        ne_idx = steps.index("ne") if "ne" in steps else inf
        nw_idx = steps.index("nw") if "nw" in steps else inf
        se_idx = steps.index("se") if "se" in steps else inf
        sw_idx = steps.index("sw") if "sw" in steps else inf

        idx = min(ne_idx, nw_idx, se_idx, sw_idx)

        if idx == inf:
            break
        else:
            idxs[idx] = steps[idx:idx+2]
            steps = steps.replace(steps[idx:idx+2], "XX", 1)

    # then find e, w
    while True:
        e_idx = steps.index("e") if "e" in steps else inf
        w_idx = steps.index("w") if "w" in steps else inf

        idx = min(e_idx, w_idx)

        if idx == inf:
            break
        else:
            idxs[idx] = steps[idx]
            steps = steps.replace(steps[idx], "X", 1)

    return [idxs[idx] for idx in sorted(idxs.keys())]


def flip_tile(grid, steps):
    q, r = 0, 0

    for step in steps:
        if step == "ne":
            q += 1
            r -= 1
        elif step == "nw":
            r -= 1
        elif step == "se":
            r += 1
        elif step == "sw":
            q -= 1
            r += 1
        elif step == "e":
            q += 1
        elif step == "w":
            q -= 1

    grid[(q, r)] = not grid[(q, r)]


def is_black(grid, q, r):
    return (q, r) in grid and grid[(q, r)]


def one_day(grid):
    new_grid = grid.copy()
    neighbours = [(0, -1), (-1, 0), (-1, 1), (0, 1), (1, 0), (1, -1)]

    for q, r in grid:
        for dq, dr in neighbours:
            if (q+dq, r+dr) not in new_grid:
                new_grid[(q+dq, r+dr)] = False

    grid = new_grid
    new_grid = grid.copy()
    for q, r in grid:
        count_black = 0
        for dq, dr in neighbours:
            if is_black(grid, q+dq, r+dr):
                count_black += 1

        black = is_black(grid, q, r)
        if black and (count_black == 0 or count_black > 2):
            new_grid[(q, r)] = False
        elif not black and (count_black == 2):
            new_grid[(q, r)] = True

    return new_grid


grid = defaultdict(bool)
parsed_steps = [parse_raw_steps(steps) for steps in raw_steps]

for steps in parsed_steps:
    flip_tile(grid, steps)

for _ in range(100):
    grid = one_day(grid)

print(sum(grid.values()))
