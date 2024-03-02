N = int(input())

l = []

for i in range(N):
    l.append(int(input()))
    
result = len(list(set(l)))

print(result)