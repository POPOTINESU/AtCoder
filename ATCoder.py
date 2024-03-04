s = input()
ans = 0
cnt = 0
a = ["A", "T", "C", "G"]
for i in range(len(s) - cnt):
    cnt = 0
    for j in range(i, len(s)):
        if s[j] not in a:
            break
        cnt += 1
    ans = max(ans, cnt)
print(ans)