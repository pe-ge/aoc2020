data = open("input.txt").read().split("\n")

valid_passwords = 0
for policy_and_password in data:
    policy, password = policy_and_password.split(": ")
    occurrences, character = policy.split(" ")
    min_occurrence, max_occurrence = map(int, occurrences.split("-"))

    count = 0
    for ch in password:
        if ch == character:
            count += 1

    if min_occurrence <= count <= max_occurrence:
        valid_passwords += 1

print(valid_passwords)
