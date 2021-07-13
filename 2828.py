# 2021/07/13 23:17
# https://www.acmicpc.net/source/30984417

size_scrn, size_bkt  = map(int, input().split())
cnt = int(input())
loc_left = 1
loc_right = size_bkt
dis = 0
ans = 0


for _ in range(cnt) :
    loc_ap = int(input())
    if loc_left < loc_ap < loc_right : continue
    elif loc_ap < loc_left :
        dis = loc_left - loc_ap
        ans += dis
        loc_left -= dis
        loc_right -= dis
    elif loc_ap > loc_right :
        dis  = loc_ap - loc_right
        ans += dis
        loc_right += dis
        loc_left += dis

print(ans)