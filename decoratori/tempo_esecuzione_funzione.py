from math import factorial
import time


def calculate_time(func):
    def wrapper(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"La funzione {func.__name__} ci impiega {end-begin:.3f} s")

    return wrapper


@calculate_time
def factorial_calculation(num):
    time.sleep(1)
    return factorial(num)


factorial_calculation(12)
