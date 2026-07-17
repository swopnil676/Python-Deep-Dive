import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time() # Start time
        result = func(*args, **kwargs) # Calls the decorated function
        end_time = time.time() # End time

        print(f"Function {func.__name__!r} took: {end_time - start_time:.4f} sec")
        return result

    return wrapper

# @timer
def example_function(n):
    return f"The Sum is {sum(range(n))}"

example_function = timer(example_function)

print(example_function(1000000))