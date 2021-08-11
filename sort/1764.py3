import sys

# 변수 설정 및 입력
d, b = map(int, sys.stdin.readline().split())
dud = set()
bo = set()

for _ in range(d) :
    dud.add(sys.stdin.readline().rstrip())
for _ in range(b) :
    bo.add(sys.stdin.readline().rstrip())

tot = list(dud & bo)
tot.sort()
print(len(tot))
for i in tot :
    print(i)
