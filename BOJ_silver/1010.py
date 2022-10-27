# 다리놓기

import sys
import math

n = int(input())
build_able = sys.stdin.readline

for i in range(n):
	WE_bridge = []
	WE_bridge = list(map(int, build_able().split()))
	# WE_bridge[0] : West, WE_bridge[1] : East
	count = math.comb(WE_bridge[1], WE_bridge[0])
	print(count)
