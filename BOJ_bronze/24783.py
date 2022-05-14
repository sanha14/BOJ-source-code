# Number Fun
t = int(input())
for i in range(t):
    a,b,c = map(int,input().split())
    if a+b == c:
        print('Possible')
    elif abs(a-b) == c:
        print('Possible')
    elif a*b == c:
        print('Possible')
    elif a/b == c:
        print('Possible')
    elif b/a == c:
        print('Possible')
    else:
        print('Impossible')

