from string import ascii_lowercase
groups = open("input.txt").read().split("\n\n")

count = 0
for group in groups:
    yes_answers = set(ascii_lowercase)
    for answers in group.split("\n"):
        answers = set(answers)
        yes_answers = yes_answers.intersection(answers)
    count += len(yes_answers)

print(count)
