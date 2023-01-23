from collections import deque
from collections import Counter


class UniqueEltQueue:
    def __init__(self):
        self.counter = Counter()
        self.queue = deque()

    def enq(self, value):
        self.counter.update([value])  # O(1)
        self.queue.appendleft(value)  # O(1)

    def deq(self):
        candidate = self.queue.pop()
        
        # Counter get and queue pop operations are O(1). 
        # While loop eliminates non-unique elements and can be considered as O(1). 
        while self.counter.get(candidate) > 1:
            self.counter[candidate] -= 1    
            candidate = self.queue.pop()  
        return candidate 


class LRU_Cache:
    def __init__(self, capacity):
        # Initialize class variables
        self.cache = {}
        self.capacity = capacity
        self.use_order = UniqueEltQueue()

    def get_value(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        value = self.cache.get(key)
        if value is None:
            # Cache miss
            return -1
        # Cache hit
        self.use_order.enq(key) 
        return value

    def set_value(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key in self.cache:
            return
        if len(self.cache) == self.capacity:
            lru_key = self.use_order.deq()
            self.cache.pop(lru_key)

        self.cache[key] = value
        self.use_order.enq(key)


if __name__ == "__main__":
    pass
