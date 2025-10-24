import copy
x = [1, 2, 3]

def func(x):
    y = copy.deepcopy(x)
    y[1] = 42
    return y

y = func(x)
print(x)
print(y)