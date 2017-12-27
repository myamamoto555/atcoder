# coding:utf-8

import bisect

N = int(raw_input())
A = sorted(map(int, raw_input().split()))
B = sorted(map(int, raw_input().split()))
C = sorted(map(int, raw_input().split()))

count = 0

for mid in B:
    lower_bound = bisect.bisect_left(A, mid)
    upper_bound = N - bisect.bisect_right(C, mid)
    count += lower_bound * upper_bound

print count
