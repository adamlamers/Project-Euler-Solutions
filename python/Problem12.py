#Adam Lamers
#Triangle Numbers
#STATUS:UNSOLVED


def TriangleNum(end):
    count = 0
    start = 1
    for i in range(start, (end+1)):
        count += i
        
    return count

def GetFactors(num):
    divisorCount = 0
    for i in range(1, (num+1)):
        if(num % i == 0):
            divisorCount += 1
            
    return divisorCount

x = 1
while x:    
    if(GetFactors(TriangleNum(x)) > 500):
        print x
        x = 0
    else:
        x += 1
    
        