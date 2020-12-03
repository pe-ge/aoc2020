data = open("input.txt").read().split("\n")

right = 3
down = 1

my_c = 0
my_r = 0

width = len(data[0])
height = len(data)

num_trees = 0
while my_c < width and my_r < height:
    if data[my_r][my_c] == "#":
        num_trees += 1

    my_r += down
    my_c = (my_c + right) % width

print(num_trees)
