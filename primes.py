"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def isPrime(number):
    prime = True
    for i in range(2, int(number / 2) + 1):
        if number % i == 0:
            prime = False
            break
    return prime

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("Input should be greater than 0")
    list = []
    potential_prime = 2
    while number_of_primes > len(list):
        if isPrime(potential_prime):
            list.append(potential_prime)
        potential_prime += 1
    return list
