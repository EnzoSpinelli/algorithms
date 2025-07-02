from collections import OrderedDict
 
class LRUCache(OrderedDict):
    def __init__(self, capacity: int):
        super().__init__()           # 1
        self.capacity = capacity     # 2
 
    def get(self, key: int) -> int:
        if key not in self:          # 3
            return -1                # 4
        self.move_to_end(key)        # 5
        return self[key]             # 6
 
    def put(self, key: int, value: int) -> None:
        if key in self:              # 7
            self.move_to_end(key)    # 8
        self[key] = value            # 9
        if len(self) > self.capacity:# 10
            self.popitem(last=False) # 11
 
if __name__ == "__main__":
    # Demonstração de uso:
    cache = LRUCache(5)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))  # espera 1
    cache.put(3, 3)      # remove key=2
    print(cache.get(2))  # espera -1
    cache.put(4, 4)      # remove key=1
    print(cache.get(1))  # espera -1
    print(cache.get(3))  # espera 3
    print(cache.get(4))  # espera 4