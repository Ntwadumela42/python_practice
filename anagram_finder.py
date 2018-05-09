def anagrams(word, words):  #Takes in two arguments, the anagram base word, and a list of words: words.
    sword = ()
    final = []
    for letter in sorted(word):
      sword = sword + (letter, word.count(letter))      
    for wrd in words:
      swords = ()
      for letter in sorted(wrd):
        swords = swords + (letter, wrd.count(letter))
      if swords == sword:
          final = final + [wrd]   
    return final
