def open_file(filename):
    file = open(filename, "r", encoding="utf-8")
    lines = file.read().splitlines()
    file.close()
    return lines

def adjacent_check(matrix, x_max, y_max, x_loc, y_loc, char):
    adj_count = 0
    for x in range(max(0, x_loc-1), min(x_max, x_loc+2)):
        for y in range(max(0, y_loc-1), min(y_max, y_loc+2)):
            if (x_loc, y_loc) == (x, y):
                continue
            if matrix[x][y] == char:
                adj_count += 1
                
    return adj_count
    
def empty_seat_validation(seating_plan, new_seating_plan, x_max, y_max, x, y):
    count = adjacent_check(seating_plan, x_max, y_max, x, y, "#")
    if count == 0:
        new_seating_plan[x][y] = "#"
    else:
        print(new_seating_plan[x][y], x, y, count)
    return new_seating_plan

def filled_seat_validation(seating_plan, new_seating_plan, x_max, y_max, x, y):
    count = adjacent_check(seating_plan, x_max, y_max, x, y, "#")
    if count >= 4:
        new_seating_plan[x][y] = "L"
    return new_seating_plan

def day11_1(filename):
    seating_plan = [list(i) for i in open_file(filename)]
    x_max = len(seating_plan)
    y_max = max(len(i) for i in seating_plan)
    new_seating_plan = [[0 for i in range(y_max)] for j in range(x_max)]
    while new_seating_plan != seating_plan:
        new_seating_plan = [x[:] for x in seating_plan]
        for x in range(0, x_max):
            for y in range(0, y_max):
                if seating_plan[x][y] == ".":
                    continue
                elif seating_plan[x][y]  == "L":
                    new_seating_plan = empty_seat_validation(seating_plan, new_seating_plan, x_max, y_max, x, y)
                elif seating_plan[x][y]  == "#":
                    new_seating_plan = filled_seat_validation(seating_plan, new_seating_plan, x_max, y_max, x, y)
        seating_plan = [x[:] for x in new_seating_plan]
    empty_seat_count = 0    
    for x in new_seating_plan:
        for y in new_seating_plan:
            if y == "L":
                empty_seat_count += 1
                
    return empty_seat_count
            
            
print(day11_1("input_test.txt"))