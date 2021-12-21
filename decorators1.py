def f1(func):
    def wrapper():
        print("Started")
        func()
        print("Finished")
    return wrapper

# x=f1(f)
# x()

@f1
def f():
    print("Hello, world")

f()


