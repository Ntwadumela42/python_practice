"""
Given an array, find the int that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

"""

#  My solution:


def find_it(seq):
    for num in seq:
      if  (seq.count(num)) % 2 != 0:
        return (num)
        break
