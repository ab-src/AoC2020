def open_file(filename):
    file = open(filename, "r", encoding="utf-8")
    lines = file.read().splitlines()
    file.close()
    return lines

def find_next_adapter(joltage, adapters, one_diff, two_diff, three_diff):
    found_adapters = []
    for value in adapters:
        if value > joltage and value <= (joltage + 3):
            found_adapters.append(value)
            
    for value in sorted(found_adapters):
        if value - joltage == 1:
            one_diff += 1
            joltage += 1
        elif value - joltage == 2:
            two_diff += 1
            joltage += 2
        elif value - joltage == 3:
            three_diff += 1
            joltage += 3
    
        adapters.remove(value)
        
    return adapters, joltage, one_diff, two_diff, three_diff

def find_sums(adapters, max_jolts, sub_list=[]):
    s = sum(sub_list)
    
    if s == max_jolts:
        print(f"sum({sub_list})={max_jolts}")
    if s >= max_jolts:    
        return
    
    for idx in range(len(adapters)):
        value = adapters[idx]
        rest_of_list = adapters[idx+1:]
        sub_list.append(value)
        find_sums(rest_of_list, max_jolts, sub_list)
        
def find_combinations(adapters):
    adapters = sorted(adapters)
    combinations = {0: 1}
    for value in adapters:
        combinations[value] = 0
        combinations[value] += combinations.get(value - 1, 0)
        combinations[value] += combinations.get(value - 2, 0)
        combinations[value] += combinations.get(value - 3, 0)

    return combinations[adapters[-1]]
       
def day10_1(filename):
    adapters = [int(i) for i in open_file(filename)]
    joltage = one_diff = two_diff = 0
    three_diff = 1
    max_jolts = max(adapters)
    while joltage < max_jolts:
        adapters, joltage, one_diff, two_diff, three_diff = find_next_adapter(joltage, adapters, one_diff, two_diff, three_diff)
    return one_diff * three_diff
    
def day10_2(filename):
    adapters = [int(i) for i in open_file(filename)]
    return(find_combinations(adapters))
    
print(day10_1("input.txt"))
print(day10_2("input.txt"))
