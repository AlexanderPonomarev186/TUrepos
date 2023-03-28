import math
import random


def primenumgenerator(n) -> list:
    result = []
    i = 1
    while len(result) < n:
        flag = True
        for g in range(2, int(i / 2) + 1):
            if i % g == 0:
                flag = False
        if flag: result.append(i)
        i += 1
    return result


def gcd(n, m):
    if m == 0:
        return n
    else:
        return gcd(m, n % m)


def task(n, m):
    return gcd(n,m) == 1

# def gcdExtended(a, b):
#     if a == 0 :
#         return b,0,1
#     gcd,x1,y1 = gcdExtended(b%a, a)
#     x = y1 - (b//a) * x1
#     y = x1
#     return gcd,x,y
#
# def asd(a: int, m: int):
#     gcd, x, y = gcdExtended(a, m)
#     if gcd == 1:
#         print((x % m + m) % m)
#     else:
#         print(-1)

def crypting(x: str):
    prime_nums = primenumgenerator(20)
    q = prime_nums[random.randint(4, 19)]
    p = prime_nums[random.randint(4, 19)]
    while p == q:
        q = prime_nums[random.randint(4, 19)]
        p = prime_nums[random.randint(4, 19)]
    n = p*q
    eul = (p-1)*(q-1)
    e = random.randint(2, eul-1)
    d = e
    while e == d:
        e = random.randint(2, eul - 1)
        while not task(e, eul):
            e = random.randint(2, eul-1)
        d = pow(e, -1, eul)
    public_key = (e, n)
    private_key = (d, n)
    result = []
    for i in x:
        result.append(ord(i)**e%n)
    return result, public_key, private_key


def decrypt(x, d, n):
    temp_res = [i**d%n for i in x]
    return temp_res

message, pub_key, pr_key = crypting("This is test message")

print([chr(i) for i in decrypt(message, pr_key[0], pr_key[1])], pr_key, pub_key)