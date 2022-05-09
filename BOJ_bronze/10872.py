# 팩토리얼

n = int(input())

def facto(n):
    f = 1
    if n == 0 or n == 1:
        f = 1

    if n > 0:
        f = facto(n-1) * n
    return f

print(facto(n))

