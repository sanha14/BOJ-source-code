# 박사 과정
t = int(input())
for i in range(t):
    expression = input()
    if expression[0] == 'P':
        print('skipped')
    elif expression.find('+') != -1:
        n1, n2 = map(int, expression.split('+'))
        print(n1+n2)