import sys

# 변수 설정 및 입력
n, m = map(int, sys.stdin.readline().split())
poke = {}
poke_list = []
for i in range(1, n+1) :
    name = sys.stdin.readline().rstrip()
    poke_list.append(name)
    poke[name] = i

for i in range(m) :
    ques = sys.stdin.readline().rstrip()
    try:
        ques = int(ques)
        print(poke_list[ques-1])
    except ValueError: 
        print(poke[ques])
