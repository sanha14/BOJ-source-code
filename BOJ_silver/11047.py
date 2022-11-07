# 동전0

value = list(map(int, input().split()))
coin = []

for i in range(value[0]):
	coin.append(int(input()))

coin.sort(reverse=True)
result = 0

for i in coin:
	if value[1] == 0:
		break
	else:
		result += value[1] // i
		value[1] = value[1] % i

print(result)
