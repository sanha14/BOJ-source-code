# FBI
idx_list = []
for i in range(1,6):
    code = input()
    if 'FBI' in code:
        idx_list.append(i)
if idx_list:
    print(*idx_list)
else:
    print("HE GOT AWAY!")

