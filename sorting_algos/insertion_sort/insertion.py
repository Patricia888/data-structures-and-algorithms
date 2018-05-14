# insertion sort
# time: O^2


# for loop goes 'forward'
# while loop goes 'backward'


def insertion_sort(lst):
    if len(lst) < 2:
        return lst

    for i in range(1, len(lst)):
        while lst[i] < lst[i - 1]:
            # this is an inplace swap
            # give them each a new value (swap)
            lst[i], lst[i - 1] = lst[i - 1], lst[i]
            if (i - 1) == 0:
                break
            i -= 1

    return lst
