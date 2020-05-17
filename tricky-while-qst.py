Write a function called stop_at_four that iterates through a list of numbers. Using a while loop, append each number to a new list until the number 4 appears. The function should return the new list.

list1 = [7, 34, 22, 1, 11, 4, 32]

def stop_at_four(lst):
    new_list = []
    accum = 0
    
    while accum < len(lst) and lst[accum] != 4:
        new_list.append(lst[accum])
        accum += 1
    return new_list

print(stop_at_four(list1))
