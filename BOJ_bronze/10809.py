# 알파벳찾기

word = input()
alpha_list = []

for i in range(97, 123):
    alpha_list.append(chr(i))

# print(alpha_list)
for i in alpha_list:
    try:
        print(word.index(i), '', end='')
    except:
        print(-1,'', end='')


