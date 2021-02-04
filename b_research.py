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
    return None

example = [21, 32, 43, 54, 67, 88, 101, 102, 210]

print(b_research(example, 43))

