"""
My friend John and I are members of the "Fat to Fit Club (FFC)". John is worried because each month a list with the weights of members is published and each month he is the last on the list which means he is the heaviest.

I am the one who establishes the list so I told him: "Don't worry any more, I will modify the order of the list". It was decided to attribute a "weight" to numbers. The weight of a number will be from now on the sum of its digits.

For example 99 will have "weight" 18, 100 will have "weight" 1 so in the list 100 will come before 99. Given a string with the weights of FFC members in normal order can you give this string ordered by "weights" of these numbers?

Example:
"56 65 74 100 99 68 86 180 90" ordered by numbers weights becomes: "100 180 90 56 65 74 68 86 99"

When two numbers have the same "weight", let us class them as if they were strings and not numbers: 100 is before 180 because its "weight" (1) is less than the one of 180 (9) and 180 is before 90 since, having the same "weight" (9) it comes before as a string.

All numbers in the list are positive numbers and the list can be empty.

Notes
it may happen that the input string have leading, trailing whitespaces and more than a unique whitespace between two consecutive numbers
Don't modify the input
For C: The result is freed.

"""
# My solution: currently stuck.  I'm thinking about creating a dictionary with the weighted values.
import operator
l1 = "103 123 4444 99 2000"
dic = {}
final = []
print (type(l1))
l1 = l1.split()
print (type(l1))
print (l1)

 
def adder_upper(num):  #This function adds each digit together to  get the number weight.
  total = 0  
  for x in str(num):
    total += int(x)
  return (total)
for number in l1:               #Adds each number from the list to a dictionary and puts its weighted value as the key.
  dic[number] = adder_upper(number)
print (adder_upper(123))

print (dic)


x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_dic = sorted(dic.items(), key=operator.itemgetter(1))
print (sorted_dic)
print (type(sorted_dic))

for key in sorted_dic:
  final.append(key[0])
final = str(final)  
final = final.replace(",", "")       #Removing all the excess characters.
final = final.replace('[', '')
final = final.replace(']', '')
final = final.replace("'", '')
print (final)
  
