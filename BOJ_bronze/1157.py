# 단어공부
word = input()
upper_word = word.upper()
frequency = [0]*26
alpha_list = [chr(i) for i in range(65, 91)]
# print(alpha_list)
for k in upper_word:
    frequency[alpha_list.index(k)] +=1

# print(frequency)
m = max(frequency)
if frequency.count(m) > 1:
    print('?')
else:
    print(alpha_list[frequency.index(m)])