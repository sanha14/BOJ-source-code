# 차량번호판 1

s = input()
ans = 1

def carnumber(s):

	if len(s) == 1 and s == 'c':
		ans = 26
		return ans;
	elif len(s) == 1 and s == 'd':
		ans = 10
		return ans;

	ans = 1
	for i in range(len(s)):
		if s[i] == 'c':
			if i == 0:
				ans *= 26
			else:
				if s[i-1] == 'c':
					ans *= 25
				else:
					ans *= 26
		elif s[i] == 'd':
			if i == 0:
				ans *= 10
			else:
				if s[i-1] == 'd':
					ans *= 9
				else:
					ans *= 10

	return ans;

print(carnumber(s))
