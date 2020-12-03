data = open("input.txt").read().split("\n")

slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

width = len(data[0])
height = len(data)

result = 1
for right, down in slopes:
    my_c = 0
    my_r = 0
    num_trees = 0
    while my_c < width and my_r < height:
        if data[my_r][my_c] == "#":
            num_trees += 1

        my_r += down
        my_c = (my_c + right) % width

    result *= num_trees

print(result)
