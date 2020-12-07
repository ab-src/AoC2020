def find_bags(rule_list, bags, count, old_count):
    old_count = count
    remaining_lines = []
    for line in rule_list:
        match = any(bag in line for bag in bags)
        if match:
            current_bag = f'{line.split(" ")[0]} {line.split(" ")[1]}'
            if current_bag not in bags:
                count += 1
                bags.append(current_bag)
        else:
            remaining_lines.append(line)
    return remaining_lines, bags, count, old_count

def parse_child_bags(line):
    inner_bag_dict = {}
    inner_bags = line.replace(" bags", "").replace(" bag", "").replace(".", "").split("contain")[1].strip()
    inner_bags = [item.strip() for item in inner_bags.split(",")]

    if "no other" in inner_bags:
        return []
    return inner_bags

def bags_calculator(dictionary, rules, current_bag):
    if current_bag not in dictionary:
        return 0

    return sum([int(next_bag[1]) * (1 + bags_calculator(dictionary, rules, next_bag[0])) for next_bag in dictionary[current_bag].items()])

def day7_1(filename):
    count = 0
    old_count = 0
    valid_bags = ["shiny gold"]
    with open(filename, "r", encoding="utf-8") as input_file:
        remaining_rules = list(input_file)
        remaining_rules, valid_bags, count, old_count = find_bags(remaining_rules, valid_bags, count, old_count)
        
        while old_count != count:
            remaining_rules, valid_bags, count, old_count = find_bags(remaining_rules, valid_bags, count, old_count)
        
    return count
 
def day7_2(filename):
    bag_dict = {}
    bags = set()
    with open(filename, "r", encoding="utf-8") as input_file:
        rules = list(input_file)
        for line in rules:
            inner_bag_dict = {}
            current_bag = f'{line.split(" ")[0]} {line.split(" ")[1]}'
            child_bags = parse_child_bags(line)
            if len(child_bags) > 0:
                bag_dict.update({current_bag: {bag[2:]: bag[:1] for bag in child_bags}})
            bags.add(current_bag)
        count = bags_calculator(bag_dict, rules, "shiny gold")
        return count
    
print(day7_1("input.txt"))
print(day7_2("input.txt"))
