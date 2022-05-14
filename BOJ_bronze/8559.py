# Potęga
import sys
n = int(sys.stdin.readline())
if n == 0:
    res = 1
elif n%4 == 0:
    res = 6
elif n%4 == 1:
    res = 2
elif n%4 == 3:
    res = 8
elif n%4 == 2:
    res = 4

print(res)