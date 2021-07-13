# 2021/07/06 00:00
# https://www.acmicpc.net/source/30687860

n = list(map(int, list(input())))

a = sorted(n, reverse=True)
a = list(map(str, a))
a = ''.join(a)
print(int(a))
