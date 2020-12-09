def open_file(filename):
    file = open(filename, "r", encoding="utf-8")
    lines = file.read().splitlines()
    file.close()
    return lines

def calculate_previous(value, cypher, idx, preamble_length):
    for i in range(idx-preamble_length, idx-1):
        for j in range(i, idx):
            if cypher[i] == cypher[j]:
                continue
            if int(cypher[i]) + int(cypher[j]) == value:
                return True
    return False
    
def find_list(cypher, target):
    num_list = []
    nsum = 0
    for idx, value in enumerate(cypher):
        num_list.append(int(value))
        nsum += int(value)
        for next_value in cypher[idx+1:]:
            num_list.append(int(next_value))
            nsum += int(next_value)
            
            if nsum < target:
                continue
            
            if nsum > target:
                num_list.clear()
                nsum = 0
                break
            
            if nsum == target:
                return min(num_list) + max(num_list)
    return 0

def day9_1(filename, preamble_length):
    cypher = open_file(filename)
    for idx, value in enumerate(cypher):
        if idx < preamble_length:
            continue
        
        if calculate_previous(int(value), cypher, idx, preamble_length):
            continue
        else:
            return value

def day9_2(filename, target):
    cypher = open_file(filename)
    return find_list(cypher, target)   
            
print(day9_1("input.txt", 25))
print(day9_2("input.txt", 375054920))
    
    