#Adam Lamers
#Project Euler Problem 4
#STATUS:SOLVED

#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
#
#Find the largest palindrome made from the product of two 3-digit numbers.

def reverseString(s):
    return s[::-1]


x1 = 1
x2 = 1
answerFile = open("Problem4.txt", "w")

for x in range(100, 1000):
    for y in range(100, x):
        x1 = x
        x2 = y
    
    
    
        #print x1, "*", x2
        x3 = x1 * x2
        

        if(str(x3) == reverseString(str(x3))):
            answerFile.write("PALINDROMIC ")
            answerFile.write(str(x3))
            answerFile.write("\n")
    