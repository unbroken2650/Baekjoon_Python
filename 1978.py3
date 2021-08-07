import sys

n = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().split()))
cnt = 0

prime = []
prime_init = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]


for i in range(2, 1001) :
    cnt = 0
    for k in prime_init :
        if i%k ==0 : cnt = 1
    if cnt != 1 : prime.append(i)
prime = prime_init + prime

cnt = 0
for i in nums :
    if i in prime :
        cnt += 1
print(cnt)