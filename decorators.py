import time
import functools

def hello(func):
    def inner():
        print('Hello')
        func()
    return inner

@hello    #decorator
def name():
    print("Ganesh")

# parameter

def pretty_sumab(func):
    def wrapper(a,b):
        print(str(a) + " + " + str(b) + " is ",end="")
        return func(a,b)
    return wrapper

@pretty_sumab
def sumab(a,b):
    sum = a+b
    print(sum)

#A decorator can be used to measure how long a function takes to execute.

def measure_time(func):
    def wrapper(*arg):
        t = time.time()
        res = func(*arg)
        print("Function took " + str(time.time()-t) + " seconds to run")
        return res
    return wrapper

@measure_time
def myfun(n):
    time.sleep(n)


#decorators with arrgument

def repeated(num_time):
    def decorator_repeat(func):
        @ functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_time):
                result  = func(*args, **kwargs)
            #return result
        return wrapper
    return decorator_repeat     


@repeated(num_time=4)
def greet(name):
    print("Hello ", name)

if __name__=="__main__":
    # obj = hello(name) 
    # obj()  
    #name()   
    #sumab(6,7)  
    #myfun(5)
    greet("Ganesh")