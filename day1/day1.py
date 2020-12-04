def day1_1(filename, n):
    with open(filename, "r") as input_file:
        list = sorted([int(i) for i in input_file]) 
        l = 0
        g = len(list) - 1

        while l < g:
            sum = list[l] + list[g]

            if sum == n:
                return list[l] * list[g]
            if sum < n:
                l += 1
            elif sum > n:
                g -= 1

        return 0


print(day1_1("input.txt", 2020))

def day1_2(filename, n):
    with open(filename, "r") as input_file:
        list = sorted([int(i) for i in input_file])

        for idx, i in enumerate(list):
            l = idx + 1
            g = len(list) - 1

            while l < g:
                sum = list[idx] + list[l] + list[g]
                
                if sum == n:
                    return list[idx] * list[l] * list[g]
                elif sum < n:
                    l += 1
                elif sum > n:
                    g -= 1

        return 0

print(day1_2("input.txt", 2020))
