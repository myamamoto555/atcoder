#coding:utf-8

N, A, B = raw_input().split()
N = int(N)
A = int(A)
B = int(B)

count = 0
for i in range(1, N+1):
    all = 0
    for j in range(len(str(i))):
        all += int(str(i)[j])
    if all >= A and all <= B:
        count += i

print count
