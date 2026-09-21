#HIGHER ORDER FUNCTIONS:
# Lambda, map(), filter() & reduce()

from functools import reduce

#practice programs on these functions:-

#1. Double Every Number
"""
nums = [1, 2, 3, 4, 5] 
double = list(map(lambda n: 2*n, nums))
print(double)
"""

#2. Keep the Positives
"""
nums = [-3, 5, -1, 8, 0, -7, 2]
pos = list(filter(lambda n: n>0, nums))
print(pos)
"""

#3. Cube with Lambda
"""
num = [2,3,5]
cube = lambda x: x**3
for i in num:
    print(cube(i))
"""

#4. Uppercase All
"""
words = ["python", "lambda", "map"]
up = list(map(lambda x: x.upper(), words))
print(up)
"""

#5. Filter the Odds
"""
odd = list(filter(lambda x: x%2!=0, range(1,21)))
print(odd)
"""

#6. Sum with reduce
"""
nums = [5, 10, 15, 20]
sum = reduce(lambda a,b: a+b, nums)
max = reduce(lambda a,b: a if a>b else b, nums)
print(sum)
print(max)
"""

#7. Sort by Last Letter
"""
names = ["Amit", "Neha", "Ravi", "Sara"]
sort = sorted(names, key = lambda n: n[-1])
print(sort)
"""

#8. Clean the Prices
"""
raw = ["$100", "$250", "$99"]
clean = list(map(lambda n: n.replace("$", ""), raw))
print(clean)
print(above)
"""

