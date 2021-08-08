import sys

# 변수 설정 및 입력
t = int(sys.stdin.readline().rstrip())
s = 0

# 실행
for _ in range(t) :
    inp = sys.stdin.readline().strip().split()
    if len(inp) == 1 :
        com = inp[0]
    else :
        com, num = inp[0], int(inp[1])
    if com == 'add' :
        s |= 1<<num
    elif com == 'remove' :
        s &= ~(1<<num)
    elif com == 'check':
        if s & (1<<num) :
            print(1)
        else :
            print(0)
    elif com == 'toggle' :
        s ^= (1<<num)
    elif com == 'all':
        s=(1<<21)-1
    elif com == 'empty' :
        s=0
    