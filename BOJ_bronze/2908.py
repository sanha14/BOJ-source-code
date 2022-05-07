# 상수
n,m = input().split()

num_list = []
rev_n = int(n[::-1])
num_list.append(rev_n)
rev_m = int(m[::-1])
num_list.append(rev_m)

print(max(num_list))

