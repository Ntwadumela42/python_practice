"""
Implement a method that accepts 3 integer values a, b, c. The method should return true if a triangle can be built with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).

"""

# My solution:  It is a triangle if a and b, the smaller sides, are greater than c.

def is_triangle(a, b, c):
  sides = (a, b, c)
  sides = sorted(sides)
  c = sides[-1]
  b = sides[1]
  a = sides[0]
  return c < a + b

