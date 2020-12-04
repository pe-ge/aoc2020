passports = open("input.txt").read().split("\n\n")

valid_passports = 0
for passport in passports:
    items = passport.split()
    if len(items) == 8 or (len(items) == 7 and "cid:" not in passport):
        valid_passports += 1

print(valid_passports)
