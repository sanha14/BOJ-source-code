# 수찬은 마린보이야!
t = int(input())
if t == 0:
    print('divide by zero')
# print(record.count(10))
else:
    record = list(map(int, input().split()))
    avg = sum(record) / t
    p = 0
    for i in record:
        p += i*(1/t)
    if p == 0:
        print('divide by zero')
    else:
        res = avg / p
        print("%.2f" %res)
