"""
Write a class TempTracker with these methods:

insert()—records a new temperature
get_max()—returns the highest temp we've seen so far
get_min()—returns the lowest temp we've seen so far
get_mean()—returns the mean ↴ of all temps we've seen so far
get_mode()—returns a mode ↴ of all temps we've seen so far
Optimize for space and time. Favor speeding up the getter methods get_max(), get_min(), get_mean(), and get_mode() over speeding up the insert() method.

get_mean() should return a float, but the rest of the getter methods can return integers. 
Temperatures will all be inserted as integers. We'll record our temperatures in Fahrenheit, so we can assume they'll all be in the range 0..110.

If there is more than one mode, return any of the modes.
"""

class TempTracker(object):

    def __init__(self):
        self.temp_list = []
        self.temp_min = 0
        self.temp_max = 0
        self.temp_total = 0.0
        self.mode = None
        self.mean = None
        self.size = 0
        self.seen = [0] * 111
        self.max_seen = 0
    
    def insert(self, val):
        if not isinstance(val, int):
            return None
        
        # gotta fix this
        self.seen[val] += 1
        if self.seen[val] > self.max_seen:
            self.mode = val
            self.max_seen = self.seen[val]

        if self.size == 0:
            self.temp_min = val
            self.temp_max = val
        
        self.temp_list.append(val)
        self.temp_total += val
        self.size += 1
        self.mean = self.temp_total / self.size

        # check for new max
        if self.temp_max < val:
            self.temp_max = val
        
        # check for new min
        if self.temp_min > val:
            self.temp_min = val
        
    def get_max(self):
        return self.temp_max

    def get_min(self):
        return self.temp_min

    def get_mean(self):
        return self.mean
    
    def get_mode(self):
        return self.mode