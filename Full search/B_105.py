N = int(input())
count = 0
l = []
r = []

for n in range(N+1):
    if n % 2 !=0:
        r.append(n)

for z in r:
    for i in range(1,z+1):
        a,b = z/i,z%i
        if b ==0:
            l.append(i)
    if len(set(l)) == 8:
        count += 1
    l = []

print(count)
