# Secret Instruction
while True:
    code = input()
    code_split = list(code)
    # print(code_split)
    if code == '99999':
        break
    else:
        decode = {}
        direction = int(code_split[0]) + int(code_split[1])
        if direction % 2 == 0 and direction > 0:
            decode['right'] =''.join(code_split[2:])
            history = 'right'
        elif direction == 0:
            decode[history] = ''.join(code_split[2:])
        else:
            decode['left'] = ''.join(code_split[2:])
            history = 'left'
    for key, val in decode.items():
        print(key, val)