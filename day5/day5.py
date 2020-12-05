def seating_calc(char, min_seat, max_seat):
    if char in ["F", "L"]:
        max_seat = max_seat - ((max_seat - min_seat) // 2) - 1
    elif char in ["B", "R"]:
        min_seat = min_seat + ((max_seat - min_seat) // 2) + 1
    return min_seat, max_seat

def day5_1(filename):
    highest_seat_id = 0
    
    with open(filename, "r") as input_file:
        for seating in input_file:
            min_seat = row_num = col_num = 0
            max_seat = 127
            
            for char in seating.rstrip()[:-3]:
                min_seat, max_seat = seating_calc(char, min_seat, max_seat)
                
            if min_seat == max_seat:
                row_num = min_seat
            else:
                return "Cannot find row"
            
            min_seat = 0
            max_seat = 7
            for char in seating.rstrip()[-3:]:
                min_seat, max_seat = seating_calc(char, min_seat, max_seat)
                
            if min_seat == max_seat:
                col_num = min_seat
            else:
                return "Cannot find column"
            
            seat_id = (row_num * 8) + col_num
            
            if seat_id > highest_seat_id:
                highest_seat_id = seat_id
    return highest_seat_id
    
def day5_2(filename):
    my_row_num = 0
    my_col_num = 0
    seat_list = [[] for i in range(128)]
    
    with open(filename, "r") as input_file:
        for seating in input_file:
            min_seat = row_num = col_num = 0
            max_seat = 127
            
            for char in seating.rstrip()[:-3]:
                min_seat, max_seat = seating_calc(char, min_seat, max_seat)
                
            if min_seat == max_seat:
                row_num = min_seat
            else:
                return "Cannot find row"
            
            min_seat = 0
            max_seat = 7
            for char in seating.rstrip()[-3:]:
                min_seat, max_seat = seating_calc(char, min_seat, max_seat)
                
            if min_seat == max_seat:
                col_num = min_seat
            else:
                return "Cannot find column"
            
            seat_list[row_num].append(col_num)

    for idx, row in enumerate(seat_list):
        if row == []:
            continue
        for col in range(0, 8):
            if col not in row and col+1 in row and col-1 in row:
                my_row_num = idx
                my_col_num = col
    return (my_row_num * 8) + my_col_num
    
print(day5_1("input.txt"))
print(day5_2("input.txt"))