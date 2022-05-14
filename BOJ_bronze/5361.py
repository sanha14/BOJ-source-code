# 전투 드로이드 가격

t = int(input())
price_list =[350.34, 230.90, 190.55, 125.30, 180.90]
res = []
for i in range(t):
    need = list(map(int,input().split()))
    total = 0.00
    for j in range(5):
        total += (price_list[j] * need[j])
    print('${:.2f}'. format(total))