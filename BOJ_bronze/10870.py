# 피보나치 수5
n = int(input())
def fibo(n):
    fb = 0
    if n <= 1:
        return n
    if n > 0:
        return fibo(n-2) + fibo(n-1)
print(fibo(n))