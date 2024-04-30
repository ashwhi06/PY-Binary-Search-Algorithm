# code your iterative algorithm here

def binary_search(lst, target):
    first  = 0
    last = len(lst) - 1
    found = False
    
    while first <= last and not found:
        midpoint = (first + last) // 2
        if lst[midpoint] == target:
            found = True
        else:
            if lst[midpoint] < target:
                first = midpoint + 1
            else:
                last = midpoint - 1
    return found

test_list = [5, 8, 12, 14, 19, 22, 27, 30, 31]

print("The binary search results return as:",binary_search(test_list, 12))