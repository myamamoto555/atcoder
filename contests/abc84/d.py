#coding:utf-8

# 0以上整数x「未満」の素数をリストに格納して返す
def primes(x):
    if x < 2: return []

    primes = [i for i in range(x)]
    primes[1] = 0 # 1は素数ではない

    # エラトステネスのふるい
    for prime in primes:
        if prime > math.sqrt(x): break
        if prime == 0: continue
        for non_prime in range(2 * prime, x, prime): primes[non_prime] = 0

    return [prime for prime in primes if prime != 0]

Q = int(raw_input())
LR = []
minl = 0
maxr = 0
for i in range(Q):
    l, r = map(int, raw_input().split())
    if minl > l:
        minl = l
    if maxl < l:
        maxl = l
    LR.append((l, r))


res = primes(maxr+1)

for l,r in LR:
    
print count
