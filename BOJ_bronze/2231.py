# 분해합
n = int(input())

for i in range(1,n+1):
    digit_list = list(map(int,str(i)))
    res = i + sum(digit_list)
    if n == res:
        print(i)
        break
    if i == n:
        print(0)


