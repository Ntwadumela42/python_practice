'''
Snail Sort
Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
This image will illustrate things more clearly:



NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as [[]]

'''

#My solution: This was a really fun lvl 4 Kata.

def snail(array):
    if array == [[]]:
        return []
    if len(array) == 1:
        for x in array:
            return x
    array_1 = array
    snail = []
    while len(array_1) > 0:
      snail += array_1.pop(0)   #Snake takes off first row.
      length = len(array_1)  #>>>4 
      state = length
      for _ in range(length - 1): #Snake going down the right column
        snail += [array_1[length - state][-1]]
        del array_1[length - state][-1] # Deletes the number from the array after the snake picks it up.
        state -= 1
      snail += array_1[-1][::-1]  # Snake picks up the last row in reverse order. 
      del array_1[-1]
      length = len(array_1)
      state = length
      print (array_1)
      count = 1
      for _ in range(length - 1): #Snake going up the left column.
        snail += [array_1[length - count][0]]
        del array_1[length - count][0]
        count += 1
      if len(array_1) == 1:
        snail += array_1.pop(0)
        return (snail)
# The best solution is gross:

"""
def snail(array):
    return list(array[0]) + snail(zip(*array[1:])[::-1]) if array else []
    '''
