"""Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

a being 1, b being 2, etc.

As an example:

alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" as a string.""

#Here is my solution, although im sure a more elegant approach exists. 
#Questions before I look at the best solution: How do I assign the letters a number easily?
#How does my answer compare to the best as far as processing speed? (How inefficient is my answer) 


def letter_to_number(letter):
  if letter == 'a':
    return 1
  elif letter == 'b':
    return 2
  elif letter == 'c':
    return 3
  elif letter == 'd':
    return 4
  elif letter == 'e':
    return 5
  elif letter == 'f':
    return 6
  elif letter == 'g':
    return 7
  elif letter == 'h':
    return 8
  elif letter == 'i':
    return 9
  elif letter == 'j':
    return 10
  elif letter == 'k':
    return 11
  elif letter == 'l':
    return 12
  elif letter == 'm':
    return 13
  elif letter == 'n':
    return 14
  elif letter == 'o':
    return 15
  elif letter == 'p':
    return 16
  elif letter == 'q':
    return 17
  elif letter == 'r':
    return 18
  elif letter == 's':
    return 19
  elif letter == 't':
    return 20
  elif letter == 'u':
    return 21
  elif letter == 'v':
    return 22
  elif letter == 'w':
    return 23
  elif letter == 'x':
    return 24
  elif letter == 'y':
    return 25
  elif letter == 'z':
    return 26
  

  
  
def alphabet_position(s):
    final = ''
    for char in s:
      final = final + str(letter_to_number(char.lower())) + ' '
    newstr = final.replace("None", "")
    newstr1 = newstr.replace("  ", ' ')
    newstr1 = newstr1.replace('   ', '')
    newstr1 = newstr1[:-1]
    if newstr1.isspace():                       #This gets awfully hacky just to fulfill the tests.
        newstr1 = ''
    return newstr1
    
#Things refreshed: string.replace("old", "new")

#Best voted solution: 
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())  #25 ms faster than mine.
    
#Most readable, 50 ms faster than mine.
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def alphabet_position(text):
    if type(text) == str:
        text = text.lower()
        result = ''
        for letter in text:
            if letter.isalpha() == True:
                result = result + ' ' + str(alphabet.index(letter) + 1)
        return result.lstrip(' ')
