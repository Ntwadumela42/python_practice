"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldWay !

"""


# My solution: Time: 551ms Passed: 22 Failed: 0

def pig_it(phrase):
    phrase = (phrase.split())
    final = ''

    for word in phrase:
      punc = '!.?'
      if word != punc:
        final = final + (word[1:] + word [0] + 'ay') + ' '
      else:
        final = final + word
    
    final = final.replace('!ay', '!')
    final = final.replace('?ay', '?')
    final = final.replace('.ay', '.')
    return final.strip()

# My second solution: 
def pig_it(phrase):
    phrase = (phrase.split())
    final = ''
    for word in phrase:
      if word.isalpha():
        final = final + (word[1:] + word [0] + 'ay') + ' '
      else:
        final = final + word
    return final.strip()


# Best solution: Time: 574ms Passed: 22 Failed: 0.   Hah, mine was faster.
 
 def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])
 
 
