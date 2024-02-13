import random

import numpy as np

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Generate a random integer between 1 and 10 (inclusive)
list = []
plist = []
for i in range(10):
    random_int = random.randint(1, 50)
    if(is_prime(random_int)):
        plist.append(random_int)
    list.append(random_int)  #dont use add

print(plist)
print(list)
if is_prime(np.sum(plist)):
    print("The sum of primes is prime")
else:
    print("Sum of primes is not prime")
