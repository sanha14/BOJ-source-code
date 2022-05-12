# 과목선택
score_list1 = []
score_list2 = []
for i in range(6):
    score = int(input())
    if i >= 4:
        score_list2.append(score)
        continue
    score_list1.append(score)

score_list1.sort(reverse=True)
del score_list1[-1:]
# print(score_list1)
print(sum(score_list1) + max(score_list2))