import sys

#변수 설정 및 입력
n = int(sys.stdin.readline().rstrip())
conf = []
cnt = 0
for _ in range(n) :
    conf.append(list(map(int, sys.stdin.readline().split())))

#정렬
conf = sorted(conf, key=lambda conf:conf[0])
conf = sorted(conf, key=lambda conf:conf[1])

#회의시간 확인
last = 0
for i, j in conf :
    if last <= i:
        cnt += 1
        last = j
print(cnt)
