# 수들의 합

def answer():
	s = int(input())
	be_s = 0
	n = 0
	for i in range(1, s+1):
		be_s += i
		n += 1
		if be_s > s:
			n -= 1
			break;
	print(n)

answer()

