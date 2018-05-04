"""
Sum of Pairs
Given a list of integers and a single sum value, return the first two values (parse from the left please) in order of appearance that add up to form the sum.

sum_pairs([11, 3, 7, 5],         10)
#              ^--^      3 + 7 = 10
== [3, 7]

sum_pairs([4, 3, 2, 3, 4],         6)
#          ^-----^         4 + 2 = 6, indices: 0, 2 *
#             ^-----^      3 + 3 = 6, indices: 1, 3
#                ^-----^   2 + 4 = 6, indices: 2, 4
#  * entire pair is earlier, and therefore is the correct answer
== [4, 2]

sum_pairs([0, 0, -2, 3], 2)
#  there are no pairs of values that can be added to produce 2.
== None/nil/undefined (Based on the language)

sum_pairs([10, 5, 2, 3, 7, 5],         10)
#              ^-----------^   5 + 5 = 10, indices: 1, 5
#                    ^--^      3 + 7 = 10, indices: 3, 4 *
#  * entire pair is earlier, and therefore is the correct answer
== [3, 7]
Negative numbers and duplicate numbers can and will appear.

NOTE: There will also be lists tested of lengths upwards of 10,000,000 elements. Be sure your code doesn't time out.

"""

ints = [2, 1, 4, 8, 7, 3, 15] # 8, 1 -- 7
s = 8
iints = [1, -2, 3, 0, -6, 1]
# ints = [1, 2, 3, 4, 1, 0]
# def sum_pairs(ints, s):
# 	pass

index = 0

found = 0

def add(x):
  for num in x:
    if (num + x[index]) == s:
    
      print (num)
      print (x[index])
      found = 1

add(ints)

if found == 0:
  index = index + 1
  add(ints)
  
  
print (iints[1] + iints[2])
