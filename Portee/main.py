#from rigolo import *
test = 90
def fct(a):
    cache = {}
    cache2 = 4
    def fct2():
        nonlocal cache2
        global test
        cache.update({"a":2})
        cache2 = 99
        test = 10000000

    fct2()
    print(cache)
    print(cache2) #4



fct("a")
print(test)
liste = [1, 2, 3]

print(len(liste)) # 1  #3