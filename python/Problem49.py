import math

#sieve of eratosthenes
def prime_sieve(num):
    a = [True for x in range(num)]
    a[0] = False

    for i in range(2, int(math.sqrt(num)+0.5)):
        if a[i] is True:
            for j in range(i**2, num, i):
                a[j] = False
    return a

primes_from_1000_to_10000 = []
for prime_number, prime in enumerate(prime_sieve(10000)):
    if prime_number > 999 and prime_number < 10000 and prime:
        primes_from_1000_to_10000.append(prime_number)

def is_permutation(number, number2):
    if number == number2:
        return False

    num1 = ''.join(sorted(str(number)))
    num2 = ''.join(sorted(str(number2)))

    if num1 == num2:
        return True

    return False


primes_with_3_permutations = []
for i in range(len(primes_from_1000_to_10000)):
    prime = primes_from_1000_to_10000[i]
    permutations = []
    for j in range(len(primes_from_1000_to_10000)):
        prime2 = primes_from_1000_to_10000[j]
        if is_permutation(prime, prime2):
            permutations.append(prime2)
    if len(permutations) == 3:
        primes_with_3_permutations.append(permutations)


for prime_set in primes_with_3_permutations:
    distance1 = 0
    distance2 = 0
    distance1 = prime_set[1] - prime_set[0]
    distance2 = prime_set[2] - prime_set[1]

    if distance1 == distance2:
        print(prime_set)


