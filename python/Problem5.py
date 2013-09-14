#Adam Lamers
#Project Euler Problem 5
#STATUS:SOLVED

#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
#What is the smallest number that is evenly divisible by all of the numbers from 1 to 20?


done = 0
counter = 0
error = 0

while not done:
    counter += 1
    if(counter % 1 != 0): continue
    if(counter % 2 != 0): continue
    if(counter % 3 != 0): continue
    if(counter % 4 != 0): continue
    if(counter % 5 != 0): continue
    if(counter % 6 != 0): continue
    if(counter % 7 != 0): continue
    if(counter % 8 != 0): continue
    if(counter % 9 != 0): continue
    if(counter % 10 != 0): continue
    if(counter % 11 != 0): continue
    if(counter % 12 != 0): continue
    if(counter % 13 != 0): continue
    if(counter % 14 != 0): continue
    if(counter % 15 != 0): continue
    if(counter % 16 != 0): continue
    if(counter % 17 != 0): continue
    if(counter % 18 != 0): continue
    if(counter % 19 != 0): continue
    if(counter % 20 != 0): continue
    break
print counter
    
    