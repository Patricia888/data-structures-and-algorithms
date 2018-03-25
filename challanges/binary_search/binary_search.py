def BinarySearch(sorted_array, search_key):
    answer = -1
    for i in range(len(sorted_array)):
        if sorted_array[i] == search_key:
            answer = i
    return answer
