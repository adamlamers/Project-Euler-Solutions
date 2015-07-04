
import math

def prime_sieve(num):
    a = [True for x in range(num)]
    a[0] = False
    a[1] = False

    for i in range(2, int(math.sqrt(num)+0.5)):
        if a[i] is True:
            for j in range(i**2, num, i):
                a[j] = False
    return a

primes = []
prime_test = prime_sieve(10000000)
for prime_number, prime in enumerate(prime_sieve(10000000)):
    if prime:
        primes.append(prime_number)

total = 0
max_len = 0
highest_list = []
for i in range(len(primes)):
    prime_list = []
    for j in range(3, len(primes) - i):
        total += primes[j]

        if total <= 10000000:
            prime_list.append(primes[j])
        else:
            break

    if len(prime_list) > max_len:
        max_len = len(prime_list)
        highest_list = prime_list

print(max_len)

tot = 0
for prime in highest_list:
    tot += prime

print(tot)
print(highest_list)
