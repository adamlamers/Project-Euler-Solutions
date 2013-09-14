#Adam Lamers
#Project Euler Problem 20
#STATUS:SOLVED

#n! means n x (n - 1) x ... x 3 x 2 x 1
#
#Find the sum of the digits in the number 100!

def fact(x): return (1 if x==0 else x * fact(x-1))
prob = str(fact(100))
answer = 0

for i in range(0, len(prob)):
    x = int(prob[i])
    answer += x
print answer