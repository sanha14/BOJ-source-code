# 미국 스타일

t = int(input())
for i in range(t):
    n,k = input().split()
    if k == "kg":
        print('{:.4f} {}'.format(float(n) * 2.2046, "lb"))
    elif k == 'lb':
        print('{:.4f} {}'.format(float(n) * 0.4536, "kg"))
    elif k == 'l':
        print('{:.4f} {}'.format(float(n) * 0.2642, "g"))
    elif k == 'g':
        print('{:.4f} {}'.format(float(n) * 3.7854, "l"))