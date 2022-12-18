#bubble sort

def bubbles(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

sorted_list = bubbles([3, 8, 2, 7, 1, 5])
print(sorted_list)