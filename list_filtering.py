"""
In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

Example
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
"""

# My solution:  I'm going to go throught the list and check if isAlpha ( checks for a-z ) remove those or create a new list with the numbers.
# code = [1,2, 123, 2568, 'a','b']
# a = 'a'
# print (a.isalpha())
# final = []
# for x in code:
#   if not str(x).isalpha():
#     final += [str(x)]
# print ([int(value) for value in final])
