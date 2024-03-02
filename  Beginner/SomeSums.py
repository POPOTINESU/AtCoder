N,A,B = map(int,input().split())

total = 0

for i in range(N+1):
    if A <= sum(map(int,str(i))) <= B:
        total += i

print(total)