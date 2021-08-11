import sys

#단어 개수 받기 + 2차원 배열 생성
n = int(input())
word = [[] for _ in range(n)]
n_word = []

#단어들 입력 받기
for i in range(n):
    word[i] = list(sys.stdin.readline())

#단어 병합
for i in range(n) :
    word[i] = ''.join(word[i])

#중복 제거(by set)
set_word = set(word)
word = list(set_word)

#단어 정렬
word.sort()

# 단어 글자수 수집
for i in range(len(word)) :
    n_word.append(len(word[i]))


#글자수 순으로 출력
for i in range(max(n_word)+1) :
    for j in range(len(word)) :
        if len(word[j]) == i : print(word[j], end="")
