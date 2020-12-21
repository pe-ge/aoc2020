from collections import Counter

data = open("input.txt").read().split("\n")

all_allergens = {}
ingredient_counter = Counter()

for line in data:
    ingredients, allergens = line.split(" (")
    ingredients = set(ingredients.split(" "))
    for ingredient in ingredients:
        ingredient_counter[ingredient] += 1

    for allergen in allergens[:-1].split(" ")[1:]:
        allergen = allergen.replace(",", "")
        if allergen not in all_allergens:
            all_allergens[allergen] = set()
            for ingredient in ingredients:
                all_allergens[allergen].add(ingredient)
        else:

            all_allergens[allergen] = all_allergens[allergen].intersection(ingredients)

found_allergens = set()
for allergens in all_allergens.values():
    for allergen in allergens:
        found_allergens.add(allergen)

result = 0
for ingredient, count in ingredient_counter.items():
    if ingredient not in found_allergens:
        result += count

print(result)
