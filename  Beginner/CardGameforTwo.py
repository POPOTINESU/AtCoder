N = int(input())

list = list(map(int,input().split()))
list.sort(reverse=True)

amount = 0

for i in range(N):
    if i % 2 == 0:
        amount += list[i]
    else:
        amount -= list[i]
        
print(amount)