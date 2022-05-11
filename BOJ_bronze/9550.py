# 아이들은 사탕을 좋아해
t = int(input())

for _ in range(t):
    res = 0
    type, least = map(int, input().split())
    each_of = list(map(int, input().split()))

    for i in each_of:
        p = i // least
        res += p
    print(res)