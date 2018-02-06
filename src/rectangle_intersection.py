"""
Write a function to find the rectangular intersection of two given love rectangles.

As with the example above, love rectangles are always "straight" and never "diagonal." 
More rigorously: each side is parallel with either the x-axis or the y-axis.
"""

"""Helper func to find the overlap given 2 points and their lenghts."""
def _find_overlap(point1, len1, point2, len2):

    heighest_start = max(point1, point2)
    lowest_end = min(point1 + len1, point2 + len2)

    if heighest_start >= lowest_end:
        return (None, None)
    
    overlap = lowest_end - heighest_start

    return (heighest_start, overlap)


def rectangle_intersection(rect1, rect2):

    y_start, y_overlap = _find_overlap(rect1['bottom_y'], rect1['width'], rect2['bottom_y'], rect2['width'])
    x_start, x_overlap = _find_overlap(rect1['left_x'], rect1['height'], rect2['left_x'], rect2['height'])  

    if not y_start or not x_start:
        return {
            'left_x': None,
            'bottom_y': None,
            'width': None,
            'height': None,
        }
    return {
        'left_x': x_start,
        'bottom_y': y_start,
        'width': y_overlap,
        'height': x_overlap,
    }

if __name__ == '__main__':

    rect1 = {
        # coordinates of bottom-left corner
        'left_x': 1,
        'bottom_y': 1,

        # width and height
        'width': 6,
        'height': 3,
    }
    rect2 = {
        # coordinates of bottom-left corner
        'left_x': 2,
        'bottom_y': 5,

        # width and height
        'width': 3,
        'height': 6,
    }

    print(rectangle_intersection(rect1, rect2))
