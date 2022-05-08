# 부녀회장이 될테야
t = int(input())

for _ in range(t):
    floor = int(input())
    number = int(input())
    people = [i+1 for i in range(number)]  #0층 세대별인구
    if floor == 0:
        print(number)

    for i in range(floor):
        for j in range(1,number):
             people[j] += people[j-1]

    print(people[-1])
