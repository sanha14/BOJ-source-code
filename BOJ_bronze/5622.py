# 다이얼
num_alpha_dict = {2:['A','B','C'], 3:['D','E','F'],4:['G','H','I'], 5:['J','K','L'],6:['M','N','O'],7:['P','Q','R','S'],8:['T','U','V'], 9:['W','Y','X','Z']}
T = input()
T_split = list(T)

dial = []

for i in T_split:
    for j in range(8):
        if i in list(num_alpha_dict.values())[j]:
            # print(j + 2)
            dial.append(j+2)
        else:
            pass
# print(dial)
print(sum(dial)+len(dial))

