# coding;utf-8

N, A, B = map(int, raw_input().split())

pl1_price = A * N
pl2_price = B

if pl1_price > pl2_price:
    print pl2_price
else:
    print pl1_price

