# 캥거루 세마리2
while True:
    try:
        a,b,c = map(int,input().split())
        print(max(b-a-1 , c-b-1))
    except EOFError:
        break