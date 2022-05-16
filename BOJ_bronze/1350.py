# 진짜 공간
N = int(input())
size = list(map(int, input().split()))
cluster = int(input())
cnt = 0

for s in size:
    if s % cluster > 0:
        cnt += s // cluster + 1
    else:
        cnt += s // cluster

print(cluster*cnt)