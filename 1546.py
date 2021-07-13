# 2021/07/03 20:39
# https://www.acmicpc.net/source/30614300

n = int(input())

def avg(li) :
    answer = sum(a, 0)/n
    return answer


a = list(map(int, input().split()))
mx = max(a)

for i in range(n) :
    a[i] /= mx
    a[i] *= 100

print(avg(a))
