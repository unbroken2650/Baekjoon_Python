import sys

nan = list()

for _ in range(9):
    nan.append(int(sys.stdin.readline()))

fake = sum(nan) - 100

for i in range(9):
    for j in range(i, 9):
        if nan[i] != nan[j]:
            if nan[i] + nan[j] == fake:
                num1 = nan[i]
                num2 = nan[j]
                break

nan.remove(num1)
nan.remove(num2)
nan.sort()

for i in nan :
    print(i)
