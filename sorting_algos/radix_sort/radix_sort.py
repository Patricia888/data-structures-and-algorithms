def radix_sort(lst, base=10):
    if len(lst) < 2:
        return lst
    
    def lst_to_buckets(lst, base, iteration):
        # create buckets according to what is set as the base
        buckets = [[] for x in range(base)]
        for number in lst:
            # Find the proper digit depending on what iteration we are on
            digit = (number // (base ** iteration)) % base
            # Put the number in the proper bucket
            buckets[digit].append(number)
        return buckets
        # now sorted in buckets according to the digit

    def buckets_to_lst(buckets):
        new_lst = []
        for bucket in buckets:
            # look at all the buckets
            for number in bucket:
                # look at each number in each bucket and append
                new_lst.append(number)
        return new_lst

    maxval = max(lst)
    itr = 0
    # while the maxval is more than the iterations, keep sorting
    # meaning, until we have done an iteration for each digit in the max value of the list, keep calling these functions to sort
    while base ** itr <= maxval:
        lst = buckets_to_lst(lst_to_buckets(lst, base, itr))
        itr += 1

    return lst
