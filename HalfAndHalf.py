# Aピザの値段
# Bピザの値段
# C= ABピザの値段
# X Aピザの枚数
# Y Bピザの枚数

def calculate_cost(A, B, C, X, Y):
    X_count = 0
    Y_count = 0
    A_count = 0
    B_count = 0
    C_count = 0
    
    def cal_C():
        nonlocal X_count, Y_count, C_count
        while X_count < X and Y_count < Y:
            X_count += 0.5
            Y_count += 0.5
            C_count += 1
    
    def cal_A():
        nonlocal X_count, A_count
        while X_count < X:
            A_count += 1
            X_count += 1
    
    def cal_B():
        nonlocal Y_count, B_count
        while Y_count < Y:
            B_count += 1
            Y_count += 1

    if A + B > C * 2:
        cal_C()
    cal_A()
    cal_B()
    result1 = A_count * A + B_count * B + C_count * C

    X_count = 0
    Y_count = 0
    A_count = 0
    B_count = 0
    C_count = 0

    cal_A()
    cal_B()
    result2 = A_count * A + B_count * B

    X_count = 0
    Y_count = 0
    A_count = 0
    B_count = 0
    C_count = 0

    while X_count < X or Y_count < Y:
        X_count += 0.5
        Y_count += 0.5
        C_count += 1
    result3 = C_count * C

    return min(result1, result2, result3)


A, B, C, X, Y = map(int, input().split())
result = calculate_cost(A, B, C, X, Y)
print(result)
