def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something before")
        func(*args, **kwargs)
        print("Something after")

    return wrapper


@my_decorator
def say_hello():
    print("Hello world")


say_hello()
