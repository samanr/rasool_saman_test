import collections
import datetime

class cache:

    def __init__(self, size, timeout):
        """constructor"""
        self.size = size
        self.cache = collections.OrderedDict()
        self.timeout = timeout
        self.lastAccess = datetime.datetime.now()

    def get(self, key):
        """get value corresponding to key, move pair to front. -1 if it does not exist"""
        try:
            self.expired()
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return -1

    def set(self, key, value):
        """add key and value to dict. Remove last if full"""
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.size:
                self.cache.popitem(last=False)
        self.cache[key] = value

    def join(self, other):
        """join two cache together"""
        self.cache = {**self.cache, **other.cache}

    def expired(self):
        """clear cache if exceeds timeout"""
        if self.lastAccess + datetime.timedelta(seconds=self.timeout) < datetime.datetime.now():
            self.clear()

    def display(self):
        """print all key value pairs"""
        for key, value in self.cache.items():
            print(key, value)

    def clear(self):
        """clears cache"""
        self.cache.clear()


cache1 = cache(5, 30)
cache2 = cache(5, 30)
cache1.set(1, 1)
cache1.set(2, 2)
cache2.set(3, 3)
cache2.set(4, 4)
cache1.display()