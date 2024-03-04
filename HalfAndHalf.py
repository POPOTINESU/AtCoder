#Aピザの値段
#Bピザの値段
#C= ABピザの値段
#X Aピザの枚数
#Y Bピザの枚数


A,B,C,X,Y = map(int,input().split ())

X_count = 0
Y_count = 0


A_count = 0
B_count = 0
C_count = 0

while X_count <= X and Y_count <= Y:
    if A + B > C * 2:
        while X_count <= X or Y_count <= Y:
            X_count += 0.5
            Y_count += 0.5
            C_count += 1
    
    while X_count <= X:
        A_count += 1
        X_count += 1
    while Y_count <= Y:
        B_count += 1
        Y_count += 1

result = A_count * A + B_count * B + C_count * C
print(result)