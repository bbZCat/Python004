# HomeWork01
"""
区分以下类型哪些是容器序列哪些是扁平序列，哪些是可变序列哪些是不可变序列：
list
tuple
str
dict
collections.deque
"""
answer = """ 
容器序列：list、tuple、collections.deque、dict
扁平序列：str
可变序列：list、dict、collections.deque
不可变序列：tuple、str
"""

print('='*75)
print("HomeWork01:")
print(answer)

# HomeWork02
"""
自定义一个 python 函数，实现 map() 函数的功能
"""

# The map function


def mymap(func, iterable):
    for each in iterable:
        yield func(each)

# Test function


def foo(x):
    return x*3


# Run

print('='*75)
print("HomeWork02:")
result = map(foo, range(10))
for each in result:
    print(f'Result is: {each}')


# HomeWork03
"""
实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。
"""
# The decorator


import random
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def innfun(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        print(f'Function {func.__name__} take {end - start} seconds to run.')
        return ret
    return innfun


# Apply to test function foo


@timer
def foo(var1, var2, var3=None):
    time.sleep(random.randint(1, 5))


# Run


print('='*75)
print("HomeWork03:")
foo(1, 2, 100)
