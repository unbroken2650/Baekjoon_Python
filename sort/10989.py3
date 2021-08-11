import sys

n = int(sys.stdin.readline().rstrip())
nums = [0] * 10001

for i in range(n) :
    t = int(sys.stdin.readline().rstrip())
    nums[t] += 1

for i in range(10001) :
    if nums[i] != 0 : 
        for _ in range(nums[i]) :
            sys.stdout.write(str(i)+"\n")
