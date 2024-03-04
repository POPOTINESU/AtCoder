N,M = map(int,input().split())

l = []
result = 0
c = 0

for i in range(N):
    #すべてのカラオケの点数を入力
    A = list(map(int,input().split()))
    #全員のデータを格納
    l.append(A)


for T1 in range(M):
    for T2 in range(T1,M):
        #N人目の人が2曲選んで選定
        for j in range(N):
            max_score = max(l[j][T1],l[j][T2])
            result += max_score
        c = max(c,result)
        result = 0

print(c)