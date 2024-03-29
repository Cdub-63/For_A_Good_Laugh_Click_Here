"""
The Sieve of Eratosthenes is one of the oldest-known algorithms, and it’s still helpful for deriving prime numbers! The algorithm is attributed to Eratosthenes, a Greek mathematician born in the third century BCE.
"""
# import math library
import math
 
def sieve_of_eratosthenes (limit):
  # handle edge cases
  if (limit <= 1):
    return []
 
  # create the output list
  output = [True] * (limit+1)
 
  # mark 0 and 1 as non-prime
  output[0] = False
  output[1] = False
 
  # iterate up to the square root of the limit
  for i in range(2, math.floor(math.sqrt(limit))):
    if (output[i] == True):
      j = i ** 2    # initialize j to square of i
 
      # mark all multiples of i as non-prime
      while j <= limit:
        output[j] = False
        j += i
 
  # remove non-prime numbers
  output_with_indices = list(enumerate(output))
  trues = [index for (index,value) in output_with_indices if value == True]
  return trues
 
primes = sieve_of_eratosthenes(20)
print(primes) # return [2, 3, 5, 7, 11, 13, 17, 19]
