# selection sorting is an in-place comparison sort
# O(N^2) time, inefficient for large datasets
# best when memory is limited


def selection_sort(lst):
    ''' Implementation of selection sort. Efficient with space but not time. Finds the smallest unsorted index (index 0 in the first run) and compares it to all other items in the list. if an item has a smaller numeric value than the smallest unsorted index, it swaps with the smallest of all the values that are smaller. Continues until sorted. '''
    if len(lst) < 2:
        return lst

    for item in range(len(lst)):
        # smallest unsorted index
        smallest_unsorted_index = item

        # look at all unsorted items, don't look at ones before index position lst[item]
        for i in range(item+1, len(lst)):
            # if a new index value is smaller than the current, we want to swap
            # there may be multiple values smaller
            if lst[smallest_unsorted_index] > lst[i]:
                smallest_unsorted_index = i

        # when done with inner loop, swap lst[item] and lst[smallest_unsorted_index]
        temp_for_swapping = lst[item]
        lst[item] = lst[smallest_unsorted_index]
        lst[smallest_unsorted_index] = temp_for_swapping

    return lst
