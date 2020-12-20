# HomeWork01
"""
��������������Щ������������Щ�Ǳ�ƽ���У���Щ�ǿɱ�������Щ�ǲ��ɱ����У�
list
tuple
str
dict
collections.deque
"""
answer = """ 
�������У�list��tuple��collections.deque��dict
��ƽ���У�str
�ɱ����У�list��dict��collections.deque
���ɱ����У�tuple��str
"""

print('='*75)
print("HomeWork01:")
print(answer)

# HomeWork02
"""
�Զ���һ�� python ������ʵ�� map() �����Ĺ���
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
ʵ��һ�� @timer װ��������¼����������ʱ�䣬ע����Ҫ���Ǻ������ܻ���ղ�����������
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
