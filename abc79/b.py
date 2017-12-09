#coding:utf-8

L = [2, 1]

N = int(raw_input())

for i in range(1, N+1):
    L.append(L[i]+L[i-1])

print L[N]
