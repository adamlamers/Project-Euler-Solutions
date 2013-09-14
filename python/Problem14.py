#Adam Lamers
#Project Euler Problem 14
#STATUS: SOLVED

def Collatz(start):
    count = 0
    while start != 1:
        #print start
        if(start % 2 == 0):
            start = start / 2
            count += 1
        else:
            start = (start*3)+1
            count += 1
        if(start == 1):
            #print start
            count += 1
            
    return count

highestCount = 0
for i in range(1, 1000000):
    collatz = Collatz(i)
    if collatz > highestCount:
        highestCount = collatz
        print i
    else:
        continue
print highestCount
    