#ATM
people = int(input())
time = list(map(int, input().split()))
time.sort()

accum = []
for i in range(people):
	if i == 0:
		accum.append(time[i])
	else:
		accum.append(accum[i-1] + time[i])

result = sum(accum)
print(result)
