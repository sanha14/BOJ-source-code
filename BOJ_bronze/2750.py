# 수 정렬하기
n = int(input())
num_list = []

for i in range(n):
    a = int(input())
    num_list.append(a)
# print(num_list)

def bubble_sort_asc(num_list):
    n = len(num_list)
    if n > 0:
        for i in range(n-1,-1,-1):
            for j in range(0,i):
                if num_list[j] > num_list[j+1]:
                    num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
        return(num_list)

res = bubble_sort_asc(num_list)
for i in res:
    print(i)