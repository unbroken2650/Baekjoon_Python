import sys
input = sys.stdin.readline

class LList():
    class Node:
        def __init__(self, item, bef, aft): #노드 초기화
            self.item = item
            self.prev = bef
            self.next = aft

    def __init__(self): #이중 링크드 리스트 초기화
        self.head = self.Node(None, None, None)
        self.tail = self.Node(None, self.head, None)
        self.head.next = self.tail
        self.cur = self.tail

    def move_left(self) : #커서 왼쪽으로 이동
        self.cur = self.cur.prev
    
    def move_right(self) : #커서 오른쪽으로 이동
        self.cur = self.cur.next
    
    def insert(self, p, item): #커서 왼쪽에 item 추가
        t = p.prev
        n = self.Node(item, t, p)
        p.prev = n
        t.next = n

    def delete(self, x): #커서 왼쪽의 글자 삭제
        if x == None : return
        f = x.prev
        r = x.next
        f.next, r.prev = r, f

    def print_list(self): #모든 글자 출력
        p = self.head.next
        while p != self.tail:
            if p.next != self.tail:
                print(p.item, end="")
            else:
                print(p.item)
            p = p.next

c = LList()
sent = list(input().rstrip())
n = int(input().rstrip())

for i in sent : #기존 문장 입력
    c.insert(c.tail, i)
for _ in range(n) : #명령어 입력 후,
    com = list(input().split())
    target = 0
    if com[0] == "P" :
        target = com[1]
    com = com[0]
    #명령에 맞춰 실행
    if com == "L" and c.cur.prev.prev != None:
        c.move_left()
    elif com == "D" and c.cur.next != None:
        c.move_right()
    elif com == "B" and c.cur.prev.prev != None:
        c.delete(c.cur.prev)
    elif com == "P" :
        c.insert(c.cur, target)

c.print_list()
