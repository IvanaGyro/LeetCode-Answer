from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        item = self.d[key]
        self.d.move_to_end(key)
        return item
        
    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d.move_to_end(key)
        elif len(self.d) == self.capacity:
            self.d.popitem(last=False)
        self.d.update({key:value})

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)