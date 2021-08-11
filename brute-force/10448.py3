import sys

#1000이하의 삼각수로 이루어진 리스트
tri_num = [n*(n+1)//2 for n in range(1, 46)]
eureka = [0] * 1001

#유레카수를 모두 계산
for i in tri_num :
    for j in tri_num :
        for k in tri_num :
            if i+j+k <= 1000 :
                eureka[i+j+k] = 1

#입력
n = int(sys.stdin.readline().rstrip())

for _ in range(n) :
    print(eureka[int(input())])
