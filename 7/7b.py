data = open("input.txt").read().split("\n")

def parse_raw_data(data):
    bags = {}
    for line in data:
        outer_bag, inner_bags = line[:-1].split(" bags contain ")
        bags[outer_bag] = []
        if inner_bags == "no other bags":
            continue

        inner_bags = inner_bags.replace(" bags", "")
        inner_bags = inner_bags.replace(" bag", "")
        inner_bags = inner_bags.split(", ")
        for inner_bag in inner_bags:
            quantity, bag_type = inner_bag.split(" ", 1)
            bags[outer_bag].append({"quantity": int(quantity), "bag_type": bag_type})

    return bags

bags = parse_raw_data(data)

bags_to_process = ["shiny gold"]
count = 0
while bags_to_process:
    outer_bag = bags_to_process.pop()

    for inner_bag in bags[outer_bag]:
        quantity = inner_bag["quantity"]
        bag_type = inner_bag["bag_type"]
        count += quantity
        for c in range(quantity):
            bags_to_process.append(bag_type)

print(count)
