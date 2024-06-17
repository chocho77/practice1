#!/usr/bin/python

import random

numbers = [random.randint(0, 10) for i in range(10)]
numbers2 = [random.randint(10, 20) for i in range(10)]

result = numbers + numbers2
result.sort()
print(result)

