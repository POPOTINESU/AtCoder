
list = list(map(int,input().split()))
list.sort(reverse=True)

count = 0
amount = 0

for i in list:
    if count % 2 == 0:
        amount += i
        count += 1
    else:
        amount -= i  
        count += 1
print(amount)