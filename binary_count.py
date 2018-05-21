'''
Write a function that takes an (unsigned) integer as input, and returns the number of bits that are equal to one in the binary representation of that number.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
'''

# My solution:

def countBits(n):
  return str(bin(n)).count('1')  # str isn't necessary.  Take a number, turn it into binary and count the '1's.  Straight forward.

