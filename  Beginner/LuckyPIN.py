# N = int(input())
# S = list(input())

# l = set()
# count = 0

# for i in range(N):
#     for j in range(i+1,N):
#         for z in range(j+1,N):
#             k = "".join([S[i], S[j], S[z]])
#             if k not in l:
#                 l.add(k)
#                 count += 1
# print(count)


# from bisect import bisect

# n = int(input())
# s = input()
# location = [[] for _ in range(10)]
# for i, c in enumerate(map(int, s)):
#     location[c].append(i)
# last_indices = [loc[-1] if loc else -1 for loc in location]

# ans = 0
# for loc_x in location:
#     if not loc_x:
#         continue
#     i = loc_x[0]
#     for loc_y in location:
#         ji = bisect(loc_y, i)
#         if ji >= len(loc_y):
#             continue
#         j = loc_y[ji]
#         ans += sum(j < li for li in last_indices)
# print(ans)


from bisect import bisect
n = int(input())
s = input()

# 0~9までの数字を格納する場所を作成する
location = [[] for _ in range(10)]
for i, c in enumerate(map(int,s)):
    location[c].append(i)
last_indices = [loc[-1] if loc else -1 for loc in location]

ans = 0

# 0~9の数字の配列を入れる
# 一番最初に出てくる場所をiに格納
for loc_x in location:
    if not loc_x:
        continue
    i = loc_x[0]
    for loc_y in location:
        ji = bisect(loc_y,i)
        if ji >= len(loc_y):
            continue
        j = loc_y[ji]
        ans += sum(j<li for li in last_indices)
print(ans)