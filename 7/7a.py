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

def find_outer_bags(all_bags, bag):
    result = set()
    for outer_bag, inner_bags in all_bags.items():
        for inner_bag in inner_bags:
            if inner_bag["bag_type"] == bag:
                result.add(outer_bag)

    return result

bags = parse_raw_data(data)

all_outer_bags = set()
bags_to_process = ["shiny gold"]
while bags_to_process:
    bag = bags_to_process.pop()
    outer_bags = find_outer_bags(bags, bag)
    all_outer_bags.update(outer_bags)
    for p in outer_bags:
        bags_to_process.append(p)


print(len(all_outer_bags))

