#Adam Lamers
#Project Euler Problem 1
#STATUS:SOLVED

endval = 0
for i in range(0, 1000):
    if(i%3 == 0):
        print i
        endval += i
    elif(i%5 == 0):
        print i
        endval += i
print endval