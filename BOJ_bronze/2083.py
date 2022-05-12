# 럭비 클럽
while True:
    name, age, weight = input().split()
    if name == '#' or int(age) == 0:
        break
    if int(age) > 17 or int(weight) >= 80:
        dept = 'Senior'
    else:
        dept = 'Junior'
    print('{} {}'.format(name, dept))
