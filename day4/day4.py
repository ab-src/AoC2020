import re

def is_int(c):
    try:
        n = int(c)
    except ValueError:
        return False
    return True

def check_passport(passport, counter, day):
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    
    for field in required_fields:
        if field not in passport:
            return counter
        if day == 2:
            if field == "byr" and is_int(passport[field]) and int(passport[field]) not in range(1920, 2003):
                return counter
            elif field == "iyr" and is_int(passport[field]) and int(passport[field]) not in range(2010, 2021):
                return counter
            elif field == "eyr" and is_int(passport[field]) and int(passport[field]) not in range(2020, 2031):
                return counter
            elif field == "hgt" and passport[field][-2:] != "cm" and passport[field][-2:] != "in":
                return counter
            elif field == "hgt" and passport[field][-2:] == "cm" and int(passport[field][:-2]) not in range(150, 194):
                return counter
            elif field == "hgt" and passport[field][-2:] == "in" and int(passport[field][:-2]) not in range(59, 77):
                return counter
            elif field == "hcl" and passport[field][0] != "#" and len(passport[field]) != 7:
                return counter
            elif field == "hcl" and passport[field][0] == "#" and len(passport[field]) == 7:
                match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', passport[field])
                if not match:
                    return counter
            elif field == "ecl" and passport[field] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                return counter
            elif field == "pid" and not isinstance(passport[field], int) and len(passport[field]) != 9:
                return counter
    return counter + 1

def day4(filename, day):
        
    passport_counter = 0
    passport = {}
    with open(filename, "r", encoding="utf-8") as input_file:
        
        for line in input_file:
            if line.isspace():
                passport_counter = check_passport(passport, passport_counter, day)
                passport.clear()
                continue
                
            attributes = line.split(" ")
            for field in attributes:
                key_value = field.split(":")
                passport[key_value[0]] = key_value[1].rstrip()
    passport_counter = check_passport(passport, passport_counter, day)
    return passport_counter
    
print(day4("input.txt", 1))
print(day4("input.txt", 2))