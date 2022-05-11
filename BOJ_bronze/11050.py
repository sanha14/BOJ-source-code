# 이항 계수1
n,k = map(int, input().split())

def facto(n):
    f = 1
    if n == 0 or n == 1:
        f = 1
    if n > 0:
        f = facto(n - 1) * n
    return f

if k == 0:
    print(1)
else:
    res = facto(n) / facto(k) *1/facto(n-k)
    print(int(res))