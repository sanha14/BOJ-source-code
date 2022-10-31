# 통계학

import sys

n = int(input())
nums = sys.stdin.read().splitlines()

def simple_statics(nums):
	freq_dict = {}
	# 산술평균
	avg = round(sum(nums) / len(nums))
	# 중앙값
	mid = sorted(nums)[len(nums) // 2]
	# 최빈값
	for i in nums:
		if i in freq_dict:
			freq_dict[i] += 1
		else:
			freq_dict[i] = 1
	freq = sorted(freq_dict.items(), key=lambda x: (x[0], -x[1]))
	if freq[0][1] == freq[1][1]:
		freq = freq[1][0]
	else:
		freq = freq[0][0]

	# 범위
	rng = max(nums) - min(nums)

	return avg, mid, freq, rng

print(simple_statics(nums))
