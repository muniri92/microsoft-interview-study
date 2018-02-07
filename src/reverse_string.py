"""

Reverse a string in-place.

"""

def reverse_string(str):

    if not isinstance(str, string):
        raise TypeError('Must input a list to reverse')

    lst_str = list(str)
    start = 0
    end = len(lst_str) - 1

    while start < end:
        lst_str[start], lst_str[end] = lst_str[end], lst_str[start]
        start += 1
        end -= 1
    
    return ''.join(lst_str)

if __name__ == '__main__':
    reverse_string(None) # raise TypeError
    reverse_string([1, 2, 3]) # raise TypeError
    reverse_string('12345') # '54321'
    reverse_string('1') # '1'
    reverse_string('13') # '31'