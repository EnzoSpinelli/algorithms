from collections import OrderedDict
 
class LRUcache (OrderedDict):
    def __init__ (self, capacity):
        super().__init__()
        self.capacity = capacity
 
    def get (self, key):
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]
   
    def put (self, key, value):
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)
 
if __name__ == "__main__":
    cache = LRUcache(5)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))  # espera 1
    cache.put(3, 3)      # remove key=2
    print(cache.get(2))  # espera -1
    cache.put(4, 4)      # remove key=1
    print(cache.get(1))  # espera -1
    print(cache.get(3))  # espera 3
    print(cache.get(4))  # espera 4