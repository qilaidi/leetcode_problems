class LRUCache:
    """504ms太慢，只打败10%，空间也太多，只打败20%"""
    def __init__(self, capacity: int):
        self.capacity_record = [None] * capacity
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache.keys():
            return -1
        else:
            self.capacity_record.remove(key)
            self.capacity_record.insert(0, key)
            return self.cache[key]


    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            self.cache[key] = value
            self.capacity_record.remove(key)
            self.capacity_record.insert(0, key)
        elif self.capacity_record[-1] == None:
            self.capacity_record.pop()
            self.capacity_record.insert(0, key)
            self.cache[key] = value
        elif self.capacity_record[-1] != None:
            del self.cache[self.capacity_record.pop()]
            self.capacity_record.insert(0, key)
            self.cache[key] = value

if __name__ == '__main__':
    cache = LRUCache(2)
    print(cache.put(1, 1))
    print(cache.put(2, 2))
    print(cache.get(1))       # returns 1
    print(cache.put(3, 3))    # evicts key 2
    print(cache.get(2))     # returns -1 (not found)
    print(cache.put(4, 4))    # evicts key 1
    print(cache.get(1))     # returns -1 (not found)
    print(cache.get(3))       # returns 3
    print(cache.get(4))       # returns 4
    cache1 = LRUCache(2)
    print(cache1.put(2, 1))
    print(cache1.put(2, 2))
    print(cache1.get(2))
    print(cache1.put(1, 1))
    print(cache1.put(4, 1))
    print(cache1.get(2))



    #
    # ["LRUCache", "put", "put", "get", "put", "put", "get"]
    # [[2], [2, 1], [2, 2], [2], [1, 1], [4, 1], [2]]
