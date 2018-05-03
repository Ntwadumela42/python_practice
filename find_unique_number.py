"""
There is an array with some numbers. All numbers are equal except for one. Try to find it!

findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55
It’s guaranteed that array contains more than 3 numbers.

The tests contain some very huge arrays, so think about performance.
"""

#My solution:  Time: 2315ms Passed: 55 Failed: 0

def find_uniq(array):
    array = sorted(array)
    first = array[0]
    last = array[-1]
    
    if array.count(first) == 1:
      return (first)
    else:
      return (last)
      
#Best solution:  Time: 2047ms Passed: 55 Failed: 0
def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b
