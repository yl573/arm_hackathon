import datetime
import random
class MyCache:
    """"""
    def __init__(self,size):
        """Constructor"""
        self.cache = {}
        self.max_cache_size =size 

    def __contains__(self, key):
        """
        Returns True or False depending on whether or not the key is in the 
        cache
        """
        return key in self.cache

    def update(self, key, value):
        """
        Update the cache dictionary and optionally remove the oldest item
        """
        if key not in self.cache and len(self.cache) >= self.max_cache_size:
            self.remove_oldest()
 
        self.cache[key] = {'time': datetime.datetime.now(),
                           'value': value}

    def remove_oldest(self):
        """
        Remove the entry that has the oldest accessed date
        """
        oldest_entry = None
        for key in self.cache:
            if oldest_entry is None:
                oldest_entry = key
            elif self.cache[key]['time'] <= self.cache[oldest_entry][
                'time']:
                oldest_entry = key
        self.cache.pop(oldest_entry)

    @property
    def size(self):
        """
        Return the size of the cache
        """
        return len(self.cache)
    def printout(self):
        print(self.cache)

cache=MyCache(2)
cache.update(1,[1,2])
cache.update(2,[3,4])
cache.update(3,[4,5])
cache.update(4,[6,7])
cache.printout()

