data = open("input.txt").read().split("\n")

all_allergens = {}

for line in data:
    ingredients, allergens = line.split(" (")
    ingredients = set(ingredients.split(" "))

    for allergen in allergens[:-1].split(" ")[1:]:
        allergen = allergen.replace(",", "")
        if allergen not in all_allergens:
            all_allergens[allergen] = set()
            for ingredient in ingredients:
                all_allergens[allergen].add(ingredient)
        else:

            all_allergens[allergen] = all_allergens[allergen].intersection(ingredients)

def remove_one_ingredient(all_allergens, removed_ingredients):
    ingredient_to_remove = None
    for allergen, ingredients in all_allergens.items():
        if len(ingredients) == 1:
            ingredient_to_remove = list(ingredients)[0]
            if ingredient_to_remove not in removed_ingredients:
                break

    if ingredient_to_remove is None:
        return

    for allergen, ingredients in all_allergens.items():
        if len(ingredients) == 1:
            continue

        if ingredient_to_remove in ingredients:
            ingredients.remove(ingredient_to_remove)

    return ingredient_to_remove


removed_ingredients = set()
while True:
    removed_ingredient = remove_one_ingredient(all_allergens, removed_ingredients)
    removed_ingredients.add(removed_ingredient)

    stop = True
    for all_allergen in all_allergens.values():
        if len(all_allergen) > 1:
            stop = False

    if stop:
        break

allergen_ingredient_pair = []
for allergen, ingredients in all_allergens.items():
    ingredient = list(ingredients)[0]
    allergen_ingredient_pair.append((allergen, ingredient))

allergen_ingredient_pair = list(sorted(allergen_ingredient_pair, key=lambda x: x[0]))

result = ""
for allergen, ingredient in allergen_ingredient_pair:
    result += ingredient + ","
print(result[:-1])
