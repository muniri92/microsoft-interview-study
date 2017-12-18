'''
Given a list of integers, find the highest product you can get from three of the integers.

The input list_of_ints will always have at least three integers.
'''

def highest_product_of_3(lst):
    '''Important to remember what values we need to keep track off:

        highest_num
        highest_two_products
        lowest_num
        lowest_two_products
        highest_product_of_three
    '''

    if (len(lst) < 3):
        raise Exception('Need at least 3 numbers in list!')

    highest_num = max(lst[0], lst[1])
    lowest_num = min(lst[0], lst[1])

    highest_two_products = lst[0] * lst[1]
    lowest_two_products = lst[0] * lst[1]

    highest_product_of_three = lst[0] * lst[1] + lst[2]

    for i in range(2, len(lst) - 1):

        highest_product_of_three = max(highest_product_of_three, i * highest_two_products, i * lowest_two_products)

        highest_two_products = max(highest_two_products, i * lowest_num, i * highest_num)

        lowest_two_products = min(lowest_two_products, i * lowest_num, i * highest_num)

        highest_num = max(highest_num, i)

        lowest_num = min(lowest_num, i)

    return highest_product_of_three


if __name__ == '__main__':
    print(highest_product_of_3([-10, -10, 1, 3, 2]))
