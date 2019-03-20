#2015

import math

n = int(input("Enter a number: "))

floor = math.floor(n/2)
numbers = list(range(1, floor))


for i in range(1, floor):
    for j in range(i, floor):
        if i+j+(2*i*j) < floor and i+j+(2*i*j) in numbers:
            numbers.pop(numbers.index(i+j+(2*i*j)))

for elem in numbers:
    numbers[numbers.index(elem)] = (2*elem)+1

numbers.append(2)
print(sorted(numbers))

