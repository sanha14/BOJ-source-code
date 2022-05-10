# 네번째 점
x_list = []
y_list = []
x4, y4 = 0,0
for i in range(1,4):
    xi,yi = map(int,input().split())
    x_list.append(xi)
    y_list.append(yi)
for i in x_list:
    if x_list.count(i) == 1:
        x4 = i

for i in y_list:
    if y_list.count(i) == 1:
        y4 = i
print(x4,y4)


