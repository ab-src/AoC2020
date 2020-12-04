def tree_counter(row, loc, count):
    if row[loc] == "#":
        return count + 1
    else:
        return count

def day3_1(filename):
    with open(filename, "r", encoding="utf-8") as input_file:
        x_loc = 0
        tree_count = 0
        
        for row in input_file:
            tree_count = tree_counter(row, x_loc, tree_count)
            x_max = len(row.rstrip()) - 1
            
            for i in range(0, 3):
                x_loc += 1
                if x_loc > x_max:
                    x_loc = 0
                
        return tree_count
        
print(day3_1("input.txt"))

def day3_2(filename, slopes):
    with open(filename, "r", encoding="utf-8") as input_file:
        reader = input_file.readlines()
        product = 1
        
        for slope in slopes:
            x_loc = 0
            tree_count = 0
            
            for row in reader[::slope[1]]:
                tree_count = tree_counter(row, x_loc, tree_count)
                x_max = len(row.rstrip()) - 1
                
                for i in range(0, slope[0]):
                    x_loc += 1
                    if x_loc > x_max:
                        x_loc = 0
            product *= tree_count
            
        return product
        
print(day3_2("input.txt", [[1,1], [3,1], [5,1], [7,1], [1,2]]))