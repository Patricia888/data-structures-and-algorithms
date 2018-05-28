# Not actual binary search

# def BinarySearch(sorted_array, search_key):
#     answer = -1
#     for i in range(len(sorted_array)):
#         if sorted_array[i] == search_key:
#             answer = i
#     return answer


# Stack Overflow answer:

def binary_search(array, key):
    if len(array) == 0:
        return -1

    bound_high = len(array) - 1
    bound_low = 0
    index = 0
    while bound_low <= bound_high:
        index = bound_low + (bound_high - bound_low) // 2
        if array[index] == key:
            return index
        elif array[index] < key:
            bound_low = index + 1
        else:
            bound_high = index - 1
    return -1


# Another version:

# def binarySearch(alist, item):
#     first = 0
#     last = len(alist)-1
#     found = False

#     while first <= last and not found:
#         midpoint = (first + last)//2
#         if alist[midpoint] == item:
#             found = True
#         else:
#             if item < alist[midpoint]:
#                 last = midpoint-1
#             else:
#                 first = midpoint+1

#     return found

#     testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
#     print(binarySearch(testlist, 3))
#     print(binarySearch(testlist, 13))
