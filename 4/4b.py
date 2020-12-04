import re
passports = open("input.txt").read().split("\n\n")

def validate_byr(value):
    return 1920 <= int(value) <= 2002

def validate_iyr(value):
    return 2010 <= int(value) <= 2020

def validate_eyr(value):
    return 2020 <= int(value) <= 2030

def validate_hgt(value):
    unit = value[-2:]
    if unit not in ("cm", "in"):
        return False

    height = int(value[:-2])
    if unit == "cm" and not(150 <= height <= 193):
        return False
    if unit == "in" and not(59 <= height <= 76):
        return False

    return True

def validate_hcl(value):
    pattern = r"^#[a-f0-9]{6}$"
    result = re.findall(pattern, value)
    return bool(result)

def validate_ecl(value):
    return value in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")

def validate_pid(value):
    pattern = r"^[0-9]{9}$"
    result = re.findall(pattern, value)
    return bool(result)

def validate_cid(value):
    return True

def validate_items(items):
    for item in items:
        name, value = item.split(":")
        if name == "byr":
            if not validate_byr(value):
                return False

        elif name == "iyr":
            if not validate_iyr(value):
                return False

        elif name == "eyr":
            if not validate_eyr(value):
                return False

        elif name == "hgt":
            if not validate_hgt(value):
                return False

        elif name == "hcl":
            if not validate_hcl(value):
                return False

        elif name == "ecl":
            if not validate_ecl(value):
                return False

        elif name == "pid":
            if not validate_pid(value):
                return False

        elif name == "cid":
            if not validate_cid(value):
                return False

        else:
            return False

    return True

valid_passwords = 0
for passport in passports:
    items = passport.split()

    if (len(items) == 8 or (len(items) == 7 and "cid:" not in passport)) and validate_items(items):
        valid_passwords += 1

print(valid_passwords)
