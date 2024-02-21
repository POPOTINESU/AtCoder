A = int(input())
B = int(input())
C = int(input())
X = int(input())

five_hundred = 500
one_hundred = 100
fifty = 50
add = 1
count = 0

for a in range(A + add):
    for b in range(B + add):
        for c in range(C + add):
            total = five_hundred * a + one_hundred * b + fifty * c
            if total == X:
                count += 1

print(count)