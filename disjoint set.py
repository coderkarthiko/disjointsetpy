def init(s):
    for k in range(len(s)):
        L[k] = k


def root(s, x):
    while s[x] != x:
        x = s[s[x]]
    return x


def join(s, u, v):
    s[root(s, s[u])] = root(s, s[v])


def ret(s):
    for k in range(len(s)):
        s[k] = root(s, s[k])


N, M = [int(x) for x in input().split()]
L = [0] * N
init(L)
for i in range(M):
    a, b = [int(x) for x in input().split()]
    join(L, a, b)
ret(L)
for i in L:
    print(i, end=" ")
