"""

Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]

"""

# My solution:Time: 525ms Passed: 49 Failed: 1
#I cant figure out whats wrong. It works in repl.it(v 2.6) but not on Codewars(v 2.6)



array = [9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]

print (array)

cnt = 0
for x in array:
  if x is 0 or x is 0.0:
    cnt = cnt + 1
    
print (cnt)

array2 = []
for x in array:
  if x is not 0 and x is not 0.0:
    array2.append(x) 



    
for num in range(cnt):
 array2.append(0)


print (array2)



