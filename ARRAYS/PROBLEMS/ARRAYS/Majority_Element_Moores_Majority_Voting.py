def mooresMajorityVoting(arr):
    element = None
    count = 0

    for i in range(0, len(arr)):
        if count == 0:
            element = arr[i]
            count += 1
        elif arr[i] == element:
            count += 1
        else:
            count -= 1

    return element



lst = [7, 7, 5, 7, 5, 1, 5, 7, 5, 5, 7, 7, 5, 5, 5, 5]
print(mooresMajorityVoting(lst))