data = open("input.txt").read().split("\n")[:-1]

valid_passwords = 0
for policy_and_password in data:
    policy, password = policy_and_password.split(": ")
    positions, character = policy.split(" ")
    first_position, second_position = map(int, positions.split("-"))

    if (password[first_position - 1] == character) ^ (password[second_position - 1] == character):
        valid_passwords += 1

print(valid_passwords)
