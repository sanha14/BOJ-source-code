# 손익분기점

a,b,c = map(int, input().split())
# print(a,b,c)

if b >= c:
    print(-1)
else:
    print(int(a/(c-b) + 1))




