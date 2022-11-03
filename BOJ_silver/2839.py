# 설탕 배달

N = int(input())

pack = 0
while N >= 0:
    if N % 5 == 0:
        print(pack + N//5)
        break
    N -= 3
    pack += 1
else:
    print(-1)
