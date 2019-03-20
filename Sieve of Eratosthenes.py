import timeit
n = int(input("Enter a number: "))
numbers = list(range(2, n+1)) #Creates list from 2 to n

start = timeit.timeit()
invalid = []
primes = []

p = 2
count = numbers.index(p)

while p**2 <= n:

    for elem in numbers[numbers.index(p**2)::p]:    #Goes through list in incremenets of p to find multiples
        if elem >= p**2:
            invalid.append(elem)    #Removes composite numbers

    if numbers[count+1] > p:
        p = numbers[count+1]    #Chooses next starting point that is not a multiple, AKA is prime
        continue

    else:
        count += 1

for elem in numbers:
    if elem not in invalid:
        primes.append(elem)

print(primes)

end = timeit.timeit()
print(start-end)