# ACM 호텔
T = int(input())

res = []
for _ in range(T):
    h,w,n = map(int, input().split())

    floor = n%h
    number = n//h + 1
    if floor == 0:
        floor = h
        number = h

    print(floor * 100 + number)
    # res.append(floor * 100 + number)

