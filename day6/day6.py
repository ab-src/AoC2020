def string_intersection(s1, s2, idx):
    result = []
    
    if idx == 0:
        idx += 1
        result[:] = s1.rstrip()
        return result, idx
        
    result = [c for c in s1 if c in s2]

    return result, idx

def day6_1(filename):
    count_list = []
    sum_counts = 0
    
    with open(filename, "r", encoding="utf-8") as input_file:
        answered_questions = []
        for line in input_file:
            if line.isspace():
                count_list.append(len(answered_questions))
                answered_questions.clear()
                continue
            
            for c in line:
                if c not in answered_questions and not c.isspace():
                    answered_questions.append(c)
        count_list.append(len(answered_questions))

    for i in count_list:
        sum_counts += int(i)
    
    return sum_counts
    
def day6_2(filename):
    count_list = []
    sum_counts = 0
    
    with open(filename, "r", encoding="utf-8") as input_file:
        answered_questions = []
        idx = 0
        for line in input_file:
            if line.isspace():
                count_list.append(len(answered_questions))
                answered_questions.clear()
                idx = 0
                continue
                
            answered_questions, idx = string_intersection(line.rstrip(), answered_questions, idx)

        count_list.append(len(answered_questions))
    for i in count_list:
        sum_counts += int(i)

    return sum_counts
    
print(day6_1("input.txt"))
print(day6_2("input.txt"))