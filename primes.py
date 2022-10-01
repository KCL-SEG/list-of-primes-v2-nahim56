"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes < 1 :
        raise ValueError
    list = []
    x = 2
    limit = 0
    while number_of_primes!=limit:
     for i in range (2,x):
        if x%i == 0:
            break
     else:
         list.append(x)
         limit+=1
     x += 1
    return list

