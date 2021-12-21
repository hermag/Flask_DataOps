def f1(func):
    def wrapper(*args, **kwargs):
        print("Started")
        val = func(*args, **kwargs)
        print("Finished")
        return val
    return wrapper

@f1
def add(x,y):
    return x+y

print(add(7,8))