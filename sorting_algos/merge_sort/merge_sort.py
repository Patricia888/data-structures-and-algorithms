def merge_sort_the_list(lst):
    ''' Performs a merge sort on a list. Checks the length and doesn't bother sorting if the length is 0 or 1. If more, it finds the middle, breaks the list in to sublists, sorts, puts in to a single list, and then returns the sorted list '''
    # don't bother sorting if list is less than 2 length
    if len(lst) < 2:
        return lst

    # find middle of inputted list
    middle_of_list = len(lst) // 2
    # recursive part
    new_list1 = merge_sort_the_list(lst[0:middle_of_list])
    new_list2 = merge_sort_the_list(lst[middle_of_list:])

    list_for_sorting = []

    while len(new_list1) and len(new_list2):
        if new_list1[-1] > new_list2[-1]:
            list_for_sorting = [new_list1.pop()] + list_for_sorting
        else:
            list_for_sorting = [new_list2.pop()] + list_for_sorting

    sorted_list = new_list1 + new_list2 + list_for_sorting
    return sorted_list
