# selection sorting is an in-place comparison sort
# O(N^2) time, inefficient for large datasets
# best when memory is limited

# can use with it starting with the largest value, or the smallest value


def selection_sort(lst):
    ''' Selection sort. '''
    if len(lst) < 2:
        return lst

