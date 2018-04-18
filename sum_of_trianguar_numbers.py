"Your task is to return the sum of Triangular Numbers up-to-and-including the nth Triangular Number.

Triangular Number: "any of the series of numbers (1, 3, 6, 10, 15, etc.) obtained by continued summation of the natural numbers 1, 2, 3, 4, 5, etc."


#My solution

def sum_triangular_numbers(n):
  total = 0
  count = 0
  if n <= 0:
    return 0
  for i in range(0, n+1):
    count = count + i
    total = total + count
    print(count)
   
  print (total)
   
sum_triangular_numbers(6)  #>>>56


#Best Solution

def sum_triangular_numbers(n):
    return n*(n+1)*(n+2)/6 if n>0 else 0
