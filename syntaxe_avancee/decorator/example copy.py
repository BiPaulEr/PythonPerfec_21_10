def cached():
    cache = {}
    def wrapper(*args):
        print("show")
    wrapper()

cached()

open