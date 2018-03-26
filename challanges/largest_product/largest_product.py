def largest_product(array):
    running_largest_product = 0

    for i in range(len(array)):
        inner_product = array[i][0] * array[i][1]
        if inner_product > running_largest_product:
            running_largest_product = inner_product
    return running_largest_product
