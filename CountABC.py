N = int(input())
S = input()

count = 0
ABC = "ABC"
result = True

for _ in range(N):
    if ABC in S:
        S = S.replace(ABC,'')

result = (N - len(S)) / len(ABC)

print(int(result))