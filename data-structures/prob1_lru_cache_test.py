from prob1_lru_cache import LRU_Cache
import itertools



def test_empty_cache():
    print("Testing empty cache...")
    lru_cache = LRU_Cache(5)
    print(lru_cache.get_value(1))  # Returns -1 because the cache is empty, or rather, 1 is not present in the cache.

def test_small_cache():
    print("Testing small cache...")
    lru_cache = LRU_Cache(5)

    lru_cache.set_value(1, 1)
    lru_cache.set_value(2, 2)
    lru_cache.set_value(3, 3)
    lru_cache.set_value(4, 4)

    print(lru_cache.get_value(1))  # returns 1
    print(lru_cache.get_value(2))  # returns 2
    print(lru_cache.get_value(9))  # returns -1 because 9 is not present in the cache

    lru_cache.set_value(5, 5) 
    lru_cache.set_value(6, 6)

    print(lru_cache.get_value(3))  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry


def test_big_cache():
    print("Testing big cache...")
    NR_OF_OPS = 10 ** 6
    CAPACITY = 10
    lru_cache = LRU_Cache(CAPACITY)

    count = 0
    for i in itertools.cycle(range(CAPACITY)):
        lru_cache.set_value(count, count)
        count += 1
        if count == NR_OF_OPS:
            break
        
    print(lru_cache.cache)
    if not all((lru_cache.get_value(NR_OF_OPS - i) == NR_OF_OPS - i for i in range(1, CAPACITY + 1))):
        print("get_value method fail")  # should not print
    else:
        print("get_value method pass")  

    lru_cache.set_value(CAPACITY, CAPACITY)

    print(lru_cache.get_value(0))  # returns -1 because 0 is not present in the cache. 
    print(lru_cache.get_value(CAPACITY))  # returns CAPACITY



if __name__ == "__main__":
    test_empty_cache()
    test_small_cache()
    test_big_cache()