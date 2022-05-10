# 블랙잭
import random
n,m = map(int,input().split())
card_list = list(map(int,input().split()))
cnt = 0
sum_list = []
# print(card_list)

for _ in range(n*(n-1)*(n-2)):
    random_choice = random.sample(card_list,3)
    if sum(random_choice) <=m:
        sum_list.append(sum(random_choice))

print(max(sum_list))
