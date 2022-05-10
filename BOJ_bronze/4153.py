# 직각삼각형
while True:
    a = list(map(int,input().split()))
    if sum(a) == 0:
        break
    d = max(a)
    a.remove(d)
    if a[0]**2 + a[1]**2 == d**2:
        print('right')
    else:
        print('wrong')