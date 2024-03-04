S = input()

acgt = "ACGT"
count = 0
result = 0

for s in S:
    if s in acgt:
        count += 1
        result = max(result,count)
    else:
        count = 0

print(result)