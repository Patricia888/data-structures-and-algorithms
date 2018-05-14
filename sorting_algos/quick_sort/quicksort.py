def quicksort(lst):
    if len(lst) < 2:
        return lst

    else:
        # keep it simple, have the pivot be index[0]
        pivot = lst[0]
        # start at index[0]
        current_position = 0
        for item in range(len(lst)-1):
            # if the item is less than the pivot, swap
            if lst[item+1] < pivot:
                # swap
                lst[item+1], lst[current_position+1] = lst[current_position+1], lst[item+1]
                # increment current_position
                current_position += 1
                # swap
        lst[0], lst[current_position] = lst[current_position], lst[0]
        # split in to 2, using the current position to split
        sort_the_beginning = quicksort(lst[:current_position])
        sort_the_end = quicksort(lst[current_position+1:])
        sort_the_beginning.append(lst[current_position])
        return sort_the_beginning + sort_the_end
