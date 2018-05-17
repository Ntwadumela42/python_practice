# proper_fractions(5)==4
number = 25
# count = 0
# numerator = 1
# for numerator in range(number-1):
#   if number % numerator != 0:
#     count += 1
#     numerator += 1
#   else:
#     numerator += 1
  
# print (count)

#factor_find
proper = 0
factors = []
for i in range(1, number + 1):
       if number % i == 0:
           factors += str(i)
print (list(set(factors)))

factors = list(set(factors))
for x in factors:
  if x == "1":
    factors.remove('1')
print (factors)
final = []

numerator = 1
for numerator in range(number):
  for num in factors:
    if numerator % int(num) != 0:
      print ("Found a proper %s / %s" % (numerator, num))
      final = final + [numerator]
      
      numerator += 1
      
    else:
      numerator += 1

print (final)
print (len(factors))

for _ in (final):
  if (final.count(_)) == len(factors):
    proper += 1
print (proper)
