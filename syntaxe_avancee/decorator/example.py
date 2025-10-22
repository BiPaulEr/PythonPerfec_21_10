
def cached(function):
    cache = {}
    def wrapper(*args):
        if args in cache:
            print("cached used")
            return cache[args]
        
        result = function(*args)
        if len(cache) >= limit:
            print(f" suppression de {list(cache.keys())[0]}")
            cache.pop(list(cache.keys())[0])
        cache[args] = result
        return result
    return wrapper
a = 3

#@cached
def compute_sum(a, b):
    print(f"compute sum executed with {a} {b}")
    time.sleep(2)
    return a + b
compute_sum = cached(compute_sum)
#@cached
def compute_sous(a, b):
    print(f"compute sub executed with {a} {b}")
    time.sleep(2)
    return a - b

compute_sous = cached(compute_sous)


compute_sum(1, 2)

compute_sum(1, 3)
compute_sum(1, 4)
compute_sum(1, 5)
compute_sum(1, 2)

compute_sum(1, 2)