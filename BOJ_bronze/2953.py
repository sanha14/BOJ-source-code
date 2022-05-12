# 나는 요리사다
score_list = []
for i in range(5):
    score = list(map(int, input().split()))
    score_list.append(sum(score))

print(score_list)
m = max(score_list)
i = score_list.index(m)
print(i+1,m)
