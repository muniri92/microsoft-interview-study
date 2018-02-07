"""

Write a function for finding the index of the "rotation point," which is where I started working from the beginning of the dictionary. This list is huge (there are lots of words I don't know) so we want to be efficient here.

words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote',  # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]

Since the list is mostly ordered, immediately think binary search

"""

def find_rotation_point(lst):
    if len(lst) == 0:
        raise Exception("List of words can't be empty!")

    start_point = 0
    end_point = len(lst) - 1
    first = lst[0]

    while start_point < end_point:
        
        mid_point = start_point + ((end_point - start_point) // 2)

        if lst[mid_point] >= first:
            start_point = mid_point
        else:
            end_point = mid_point
        
        if (start_point + 1) == end_point:
            return end_point


if __name__ = __main__:
    perfect_list = ['asymptote', 'babka', 'banoffee', 'engender', 'karpatka', 'othellolagkage', 'ptolemaic', 'retrograde', 'supplant', 'undulate', 'xenoepist']
    odd_list = ['othellolagkage', 'ptolemaic', 'retrograde', 'supplant', 'undulate', 'xenoepist', 'z', 'asymptote', 'babka', 'banoffee', 'engender', 'karpatka']
    even_list = ['othellolagkage', 'ptolemaic', 'retrograde', 'supplant', 'undulate', 'xenoepist','asymptote', 'babka', 'banoffee', 'engender']
    empty_list = []

    print(find_rotation_point(perfect_list)) # 0
    print(find_rotation_point(odd_list)) # 7
    print(find_rotation_point(even_list)) # 6
    print(find_rotation_point(empty_list)) # 0
    

