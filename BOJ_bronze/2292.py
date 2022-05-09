# 벌집

_pass = 1
N = int(input())
wall = 1
while N > wall :
    wall += 6*_pass
    _pass += 1
print(_pass)