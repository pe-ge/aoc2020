from math import sqrt

data = open("input.txt").read().split("\n\n")
tiles = {}

for d in data:
    tile_desc, *tile = d.split("\n")
    tile_id = int(tile_desc.split(" ")[1][:-1])
    tiles[tile_id] = tile


def generate_rotations_and_flips(tile):
    orig_tile = [list(line) for line in tile]
    orig_flipped_vertically = [list(reversed(line)) for line in orig_tile]
    orig_flipped_horizontally = [list(line) for line in reversed(orig_tile)]
    orig_flipped_diagonally = [list(reversed(line)) for line in reversed(orig_tile)]
    rot_tile = [[tile[x][y] for x in range(len(tile))] for y in range(len(orig_tile[0]))]
    rot_flipped_vertically = [list(reversed(line)) for line in rot_tile]
    rot_flipped_horizontally = [list(line) for line in reversed(rot_tile)]
    rot_flipped_diagonally = [list(reversed(line)) for line in reversed(rot_tile)]

    return [
        orig_tile, orig_flipped_vertically, orig_flipped_horizontally, orig_flipped_diagonally,
        rot_tile, rot_flipped_vertically, rot_flipped_horizontally, rot_flipped_diagonally
    ]


def extend_tiles_with_rotations_and_flips(tiles):
    for tile_id, tile in tiles.items():
        tiles[tile_id] = generate_rotations_and_flips(tile)

    return tiles

def check_tile_in_image(image, tile, image_row, image_col):
    tile_size = len(tile)
    # check above
    if image_row - 1 >= 0:
        _, tile_above = image[image_row - 1][image_col]
        for col_idx in range(tile_size):
            if tile[0][col_idx] != tile_above[-1][col_idx]:
                return False
    # check left
    if image_col - 1 >= 0:
        _, tile_left = image[image_row][image_col - 1]
        for row_idx in range(tile_size):
            if tile[row_idx][0] != tile_left[row_idx][-1]:
                return False

    return True

def backtrack(image, image_row, image_col, all_tiles, used_tiles):
    if image_row == len(image):
        return True

    for tile_id, tile_rots in all_tiles.items():
        if tile_id in used_tiles:
            continue
        used_tiles.add(tile_id)

        for tile_rot in tile_rots:
            if not check_tile_in_image(image, tile_rot, image_row, image_col):
                continue

            image[image_row][image_col] = (tile_id, tile_rot)
            next_image_row = image_row
            next_image_col = image_col + 1
            if next_image_col == len(image[image_row]):
                next_image_row += 1
                next_image_col = 0
            if backtrack(image, next_image_row, next_image_col, all_tiles, used_tiles):
                return True
            image[image_row][image_col] = None

        used_tiles.remove(tile_id)

    return False


tiles = extend_tiles_with_rotations_and_flips(tiles)

image_size = int(sqrt(len(tiles)))
image = []
for _ in range(image_size):
    image.append([])
    for _ in range(image_size):
        image[-1].append(None)

backtrack(image, 0, 0, tiles, set())

tile_size = len(tile)
tmp_image = {}
for image_row_idx, image_row in enumerate(image):
    for image_col_idx, (_, image_tile) in enumerate(image_row):
        for tile_row_idx in range(1, tile_size-1):
            for tile_col_idx in range(1, tile_size-1):
                final_image_row_idx = image_row_idx * (tile_size - 2) + tile_row_idx - 1
                final_image_col_idx = image_col_idx * (tile_size - 2) + tile_col_idx - 1
                tmp_image[(final_image_row_idx, final_image_col_idx)] = image_tile[tile_row_idx][tile_col_idx]

image_size = int(sqrt(len(tmp_image)))
final_image = []
for row_idx in range(image_size):
    final_image.append([])
    for col_idx in range(image_size):
        final_image[-1].append(tmp_image[(row_idx, col_idx)])

monster = [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   "
]
monster_width = len(monster[0])
monster_height = len(monster)

monster_idxs = set()
for monster_row_idx, monster_row in enumerate(monster):
    for monster_col_idx, monster_char in enumerate(monster_row):
        if monster_char == "#":
            monster_idxs.add((monster_row_idx, monster_col_idx))


def search_monster(image):
    monster_start_idxs = []
    for image_row_idx in range(0, image_size-monster_height+1):
        for image_col_idx in range(0, image_size-monster_width+1):
            monster_found = True
            for monster_row_idx, monster_col_idx in monster_idxs:
                pixel = image[image_row_idx + monster_row_idx][image_col_idx + monster_col_idx]
                if pixel != "#":
                    monster_found = False
                    break

            if monster_found:
                monster_start_idxs.append((image_row_idx, image_col_idx))

    return monster_start_idxs


for final_image in generate_rotations_and_flips(final_image):
    monster_start_idxs = search_monster(final_image)
    if len(monster_start_idxs) == 0:
        continue
    monster_pixels = set()
    for monster_start_row_idx, monster_start_col_idx in monster_start_idxs:
        for monster_row_idx, monster_col_idx in monster_idxs:
            monster_pixels.add((monster_start_row_idx + monster_row_idx, monster_start_col_idx + monster_col_idx))
    result = 0
    for row_idx in range(len(final_image)):
        for col_idx in range(len(final_image[0])):
            pixel = final_image[row_idx][col_idx]
            if pixel == "#" and (row_idx, col_idx) not in monster_pixels:
                result += 1

    print(result)
    break
