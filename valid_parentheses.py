"""

Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
Constraints
0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. Furthermore, the input string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).

"""

# My solution : Time: 632ms Passed: 50 Failed: 0


def valid_parentheses(l1):
    l2 = ''
    for char in l1:
      if char == '(' or char == ')':
        l2 = l2 + char
    for p in l2:
        l2 = l2.replace('()', '')
    return l2 == ''
    
 # Best solution:
 
 def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1          #Very clever. If it counts a ) first, it will go to -1 and return False.
        if cnt < 0: return False
    return True if cnt == 0 else False
