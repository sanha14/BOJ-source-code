# 문자열반복
T = int(input())
ans_list = []
for i in range(T):
    n,s = input().split()
    res = ''
    for k in s:
        res += k*int(n)
    ans_list.append(res)

for i in ans_list:
    print(i)
