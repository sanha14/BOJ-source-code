# 잃어버린 괄호

import sys
input = sys.stdin.readline

expression = input().split('-')
arr = []
result = 0

for i in expression:
	tmp = 0
	for j in i.split('+'):
		tmp += int(j)
	arr.append(tmp)

result += arr[0]
for i in range(1, len(arr)):
	result -= arr[i]
print(result)
