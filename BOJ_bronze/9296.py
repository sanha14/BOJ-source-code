# Grading Exams
t = int(input())
for i in range(1,t+1):
    q_num = int(input())
    cnt = 0
    ans = list(map(str,input()))
    respond = list(map(str,input()))
    # print(ans, respond)
    for j in range(q_num):
        if ans[j] != respond[j]:
            cnt += 1
    print("Case {}: {}" .format(i, cnt))