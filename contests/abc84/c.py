# coding:utf-8

N = int(raw_input())
C = []
S = []
F = []

for i in range(N-1):
    c, s, f = map(int, raw_input().split())
    C.append(c)
    S.append(s)
    F.append(f)

res = []

for i in range(N-1):
    t = 0
    for j in range(i, N-1):
        if S[j] >= t: 
            t = 0
            t += S[j] + C[j]
        elif t % F[j] == 0:
            t += C[j]
        else:
            t = S[j] + F[j] * ((t - S[j]) / F[j]) + F[j] + C[j]
    print t

print 0
