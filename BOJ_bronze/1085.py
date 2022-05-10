# 직사각형에서 탈출

x,y,w,h = map(int,input().split())

while x>0 and y>0:
    if x>=w or y>=h:
        break
    to_right = w-x
    to_left = x
    to_up = h-y
    to_down = y
    print(min(to_right,to_left,to_up,to_down))
    break