"""

Reverse a string in-place.

"""

def reverse_string(str):

    lst_str = list(str)

    start = 0
    end = len(lst_str) - 1

    while start < end:
        

