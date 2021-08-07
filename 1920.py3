import sys

def binsrch(li, t, start, end) :
    while start<=end:
        mid = (start+end)//2
        if li[mid] == t : return mid
        elif li[mid] > t : end = mid -1
        else : start = mid + 1
    return None

n = int(sys.stdin.readline().rstrip())
li = list(map(int, sys.stdin.readline().split()))
li.sort()
m = int(sys.stdin.readline().rstrip())
tli = list(map(int, sys.stdin.readline().split()))

for i in range(m) :
    res = binsrch(li, tli[i], 0, n-1)
    if res == None : print(0)
    else : print(1)