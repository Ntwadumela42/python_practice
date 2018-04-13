"""The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. Each of them has a single 100, 50 or 25 dollars bill. An "Avengers" ticket costs 25 dollars.

Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

Can Vasya sell a ticket to each person and give the change if he initially has no money and sells the tickets strictly in the order people follow in the line?

Return YES, if Vasya can sell a ticket to each person and give the change with the bills he has at hand at that moment. Otherwise return NO.

###Examples:

### Python ###

tickets([25, 25, 50]) # => YES 
tickets([25, 100]) 
         # => NO. Vasya will not have enough money to give change to 100 dollars"""
         
         
def tickets(people):
    n25 = n50 = n100 = 0                               #Set the count of 25, 50, and 100 dollar bills to 0.
    for e in people:                                   # For bills in the people input.
        if   e==25            : n25+=1                 # If the bill is 25, add 1 to the 25 count.
        elif e==50            : n25-=1; n50+=1         # If the bill is a 50, subtract a 25 and add a 50.
        elif e==100 and n50>0 : n25-=1; n50-=1         # If the bill is a 100 and the 50 count is positive, subtract 25 and 50.
        elif e==100 and n50==0: n25-=3                 # If the bill is 100 and no 50s, subtract 3 25s.
        if n25<0 or n50<0:                             # If the count of 25 or 50 is below zero, not enough change.
            return 'NO'
    return 'YES'                                       # Else, return Yes, enough change. 
