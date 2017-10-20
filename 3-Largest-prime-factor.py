# def primes(n):
#     if n <= 2:
#         return []
#     sieve = [True]*(n+1)
#     for x in range(3, int(n**0.5)+1, 2):
#         for y in range(3, (n//x)+1, 2):
#             sieve[(x*y)] = False

#     return [2]+[i for i in range(3, n, 2) if sieve[i]]

n = 600851475143
i = 2

while i * i < n:
    while n % 2 == 0:
        n = n / i
    i = i + 1

print(int(n))
