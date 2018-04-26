"""Write a reverseWords function that accepts a string a parameter, and reverses each word in the string. Any spaces in the string should be retained.

Example:

reverse_words("This is an example!") # returns  "sihT si na !elpmaxe"
reverse_words("double  spaces") # returns  "elbuod  secaps"


"""

def reverse_words(str):
  string_length = len(str.split())                         #Calculate the number of words.
  final = ''
  for n in range(0, string_length):                        #From range 0 to the calculated length
    final = final + (string.split()[(n)][::-1]) + ' '      #Adds the reversed word to the final string.
    
  return final  
