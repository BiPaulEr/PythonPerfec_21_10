def generator(limit):
    for i in range(0, limit):
        yield i
        yield i
    print("end")


gen = generator(3)

for i in generator(3):
    print(i)

for i in generator(3):
    print(i)
