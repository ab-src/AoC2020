def day2_1(filename):
    with open(filename, "r", encoding="utf-8") as input_file:
        rule_count = 0
        for line in input_file:
            values = line.replace(":", "").split(" ")
            min_count = int(values[0].split("-")[0])
            max_count = int(values[0].split("-")[1])
            match_char = values[1]
            password = values[2]
            count = 0
            
            for char in password:
                if char == match_char:
                    count += 1
                
            if count > max_count:
                continue
            elif count < min_count:
                continue
            else:
                rule_count += 1
        return rule_count
        
print(day2_1("input.txt"))

def day2_2(filename):
    with open(filename, "r", encoding="utf-8") as input_file:
        rule_count = 0
        for line in input_file:
            values = line.replace(":", "").split(" ")
            position_one = int(values[0].split("-")[0]) - 1
            position_two = int(values[0].split("-")[1]) - 1
            match_char = values[1]
            password = values[2]
            
            if bool(password[position_one] == match_char) ^ bool(password[position_two] == match_char):
                rule_count += 1 
                
        return rule_count
        
print(day2_2("input.txt"))
