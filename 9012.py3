import sys

n = int(sys.stdin.readline().rstrip())
ps = ""
cnt = 1
for _ in range(n) :
    ps = sys.stdin.readline().rstrip()
    while True :
        while cnt == 1 :
            cnt = 0
            for i in range(len(ps)) :
                if i > len(ps)-2 : break
                if ps[i] == "(" and ps[i+1] == ")" :
                    ps = ps[0:i]+ps[i+2:len(ps)]
                    cnt = 1
                    break
        if cnt == 0 : break
    if len(ps) != 0 : print("NO")
    else : print("YES")
    cnt = 1
