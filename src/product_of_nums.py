'''
You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.

Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.

For example, given:
    [1, 7, 3, 4]
your function would return:
    [84, 12, 28, 21]
by calculating
    [7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]

DO NOT USE DIVISION IN YOUR SOLUTION
'''


# def get_products_of_all_ints_except_at_index(lst):
#     '''Brute force way to answer question, uses division.'''
#     new_lst = []
#     all_sum = 1
#     for val in lst:
#         all_sum *= val
#     for idx, val in enumerate(lst):
#         new_val = all_sum / lst[idx]
#         new_lst.append(new_val)
#     return new_lst


def get_products_of_all_ints_except_at_index(lst):
    '''O(n) space and time.'''
    new_lst = []
    count = 1
    for idx, val in enumerate(lst):
        new_lst.append(count)
        count = count * val

    i = len(lst) - 1
    count = 1
    while i >= 0:
        new_lst[i] *= count
        count *= lst[i]
        i -= 1

    return new_lst


if __name__ == '__main__':
    print(get_products_of_all_ints_except_at_index([1, 7, 3, 4]))
