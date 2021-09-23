"""
i = n
while i > 0:
	k = 2 + 2
	i = i // 2

"""

import timeit
import math

def count(n):
    i = 0
    while True:
        n = n // 2
        i += 1
        if n == 0:
            break
    return i

def find_steps(n):
    if n == 0:
        return 0
    else:
        i = 1
        while True:
            if 2 ** (i - 1) <= n <= 2 ** i - 1:
                return i
                break
            i += 1

def find_steps_2(n):
    return int(math.log(n, 2)) + 1

t1 = timeit.Timer("count(1000000)", "from __main__ import count")
print("count ", t1.timeit(number=1000), "milliseconds")

t2 = timeit.Timer("find_steps(1000000)", "from __main__ import find_steps")
print("find ", t2.timeit(number=1000), "milliseconds")

t3 = timeit.Timer("find_steps_2(1000000)", "from __main__ import find_steps_2")
print("find_2 ", t3.timeit(number=1000), "milliseconds")

for i in range(1, 100001):
    print(str(i) + ': ' + str(count(i)) + '   ' + str(find_steps(i)) + '   ' + str(find_steps_2(i)))

"""
So the big O notation is:
    2 * [log(n, 2)]

"""
