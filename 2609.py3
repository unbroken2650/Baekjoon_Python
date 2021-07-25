import math

m, n = map(int, input().split())

gcd = math.gcd(m, n)
lcm = gcd*(m/gcd)*(n/gcd)

print(gcd)
print(int(lcm))