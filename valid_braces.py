"""
Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false if it's invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}. Thanks to @arnedag for the idea!

All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

What is considered Valid?
A string of braces is considered valid if all braces are matched with the correct brace.

Examples
"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False

"""


def validBraces(string):
  count_0 = 0
  count_1 = 0
  count_2 = 0
    
    
  for x in string:
      if x == '(':
        count_0 = count_0 + 1
      elif x == ')':
        count_0 = count_0 - 1
        if count_0 == -1:
            return False
      if x == '{':
        count_1 = count_1 + 1
      elif x == '}':
        count_1 = count_1 - 1
        if count_1 == -1:
            return False
      if x == '[':
        count_2 = count_2 + 1
      elif x == ']':
        count_2 = count_2 - 1
        if count_2 == -1:
            return False
  if count_0 == 0 and count_1 == 0 and count_2 == 0:
    return True
  else:
    return False