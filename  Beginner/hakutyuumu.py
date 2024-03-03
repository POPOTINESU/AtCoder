S = input()

list = ["eraser", "erase" ,"dreamer", "dream"]

for l in list:
    if l in S:
        S = S.replace(l,'')

if len(S) == 0:
    print("YES")
else:
    print("NO")