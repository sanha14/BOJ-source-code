# e 계산
def facto(n):
    if n <= 1:
        return 1
    return n * facto(n - 1)

sum =  0.0
print("n e")
print("- -----------")
for i in range(10):
    sum += 1 / facto(i)
    if i == 0 or i == 1:
        print("{} {}" .format(i, int(sum)))
    elif i == 2:
        print(i, end=" ")
        print(round(sum, 2))
    else:
        print("{} {:.9f}" .format(i, sum))
