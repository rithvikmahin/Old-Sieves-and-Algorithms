#2015 

n = int(input("Enter a number: "))
numbers = list(range(2, n+1)) #Creates list from 2 to n

p = 2
count = numbers.index(p)

while p**2 <= n:

    for elem in numbers[p+numbers.index(p)::p]:    #Goes through list in incremenets of p to find multiples
        numbers[numbers.index(elem)] = 0    #Removes composite numbers

    if numbers[count+1] > p:
        p = numbers[count+1]    #Chooses next starting point that is not a multiple, AKA is prime
        continue

    else:
        count += 1

print(list(filter(None, numbers)))
