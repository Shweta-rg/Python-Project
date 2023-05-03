import time
current_time = time.time()
print(current_time)


def speed_calc_decorator(function):
    # print("I am outer")
    def wrapper():
        print("i am inner")
        start_time = time.time()
        print(start_time)

        function()
        print("after function")

        end_time = time.time()

        print(end_time)
        print(f"{function.__name__} run speed: {end_time - start_time}s")
        # return diffof
    # print("after 6")
    return wrapper

# def decorater(funct):
#   def wrapper()
#   time.sleep
#     function()
#   return wrapper


@speed_calc_decorator
def fast_function():
    print("inside fast funct")
    for i in range(10000000):
        i * i
    print("exit fast")


def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()
