# 2021/07/03 20:31
# https://www.acmicpc.net/source/30614049
sn = list(input())
sn = list(map(ord, sn))

alp = list(range(65, 90+1))
ans = list()
ans2 = list()

#making capital
for i in range(0, len(sn)) :
    if sn[i]>91 :
        sn [i] -= 32

#
for i in range(len(alp)) :
    ans.append(sn.count(alp[i]))

b = ans.index(max(ans))

if ans.count(max(ans)) == 1 :
    print(chr(alp[b]))
else : print("?")
