"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    number = number_of_primes
    if number < 1 :
        raise ValueError
    list = []
    for i in range (1,number):
        for x in range (2,i):
            if i%x == 0:
                break
            else:
                list.append(i)
    print(list)

