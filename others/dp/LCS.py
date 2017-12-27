# coding:utf-8

# 最長共通部分列
# LCS(Longest Common Subsequence problem)

def lcs(X, Y):
    X = ' ' + X
    Y = ' ' + Y
    c = [[0 for i in range(len(Y))] for j in range(len(X))]
    maxl = 0
    for i in range(1, len(X)):
        for j in range(1,len(Y)):
            if X[i] == Y[j]:
                c[i][j] = c[i-1][j-1] + 1
            elif c[i][j-1] >= c[i-1][j]:
                c[i][j] = c[i][j-1]
            else:
                c[i][j] = c[i-1][j]
            maxl = max(maxl, c[i][j])
    print maxl

if __name__ == '__main__':
    X = 'TCCAGATGG'
    Y = 'TCACA'
    lcs(X, Y)
