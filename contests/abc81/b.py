#coding:utf-8

N = int(raw_input())
As = map(int, raw_input().split())

count = 0
flag = 0

while True:
    for i in range(N):
        if As[i] % 2 == 0:
            As[i] = As[i] / 2
        else:
            flag = 1
            break
    if flag == 1:
        break
    else:
        count += 1

print count
