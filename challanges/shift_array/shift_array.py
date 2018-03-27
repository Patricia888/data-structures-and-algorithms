def insertShiftArray(given_array, added_value):
    new_array = []

    array_midpoint = len(given_array) // 2
    for i in range(len(given_array) + 1):
        if i < array_midpoint:
            new_array += [given_array[i]]
        elif i == array_midpoint:
            new_array += [added_value]
        else:
            new_array += [given_array[i - 1]]
    return new_array
