#Adam Lamers
#Project Euler Problem 16
#STATUS:SOLVED

#2^(15) = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
#What is the sum of the digits of the number 2^(1000)?

prob = str(pow(2, 1000))
answer = 0
print prob, "\n"
for i in range(0, len(prob)):
    x = int(prob[i])
    answer += x
print answer