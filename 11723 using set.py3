import sys

# 변수 설정 및 입력
t = int(sys.stdin.readline().rstrip())
s = set()

# 실행
for _ in range(t) :
    inp = sys.stdin.readline().strip().split()
    if len(inp) == 1 :
        com = inp[0]
        if com == 'all':
            s = set([i for i in range(1, 21)])
        elif com == 'empty' :
            s = set()

    else :
        com, num = inp[0], int(inp[1])
    
        if com == 'add' :
            s.add(num)
        elif com == 'remove' :
            s.discard(num)
        elif com == 'check':
            print(1 if num in s else 0)
        elif com == 'toggle' :
            if num in s :
                s.discard(num)
            else : s.add(num)
    