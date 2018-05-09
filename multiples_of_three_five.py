"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Note: If the number is a multiple of both 3 and 5, only count it once.
"""

# My solution:

def solution(number):
  final_sums = []
  total = 0
  for num in range(number):
    if num * 3 < number:
      final_sums = final_sums + [(num *3)]
      print (num * 3)
  for num in range(number):
    if num * 5 < number:
      final_sums = final_sums + [(num *5)]
      print (num * 5)
  
  
  for x in set(final_sums):
    total = total + x
  return total
