def b_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        i = (low + high) // 2
        if list[i] == item:
            return i
        if list[i] > item:
            high = i - 1
        else:
            low = i + 1
    return i

example = [2, 15, 23, 34, 35, 44, 51, 76, 88, 100]

print(b_search(example, 35))
