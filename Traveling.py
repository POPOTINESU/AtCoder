N = int(input())

x_l = 0
y_l = 0

pre_t = 0

# for n in range(N):
#     t,x,y = map(int,input().split())
#     for i in range(t - num):
#         if x > x_l:
#             x_l += 1
#         elif x < x_l:
#             x_l -= 1
#         else:
#             if y > y_l:
#                 y_l += 1
#             elif y < y_l:
#                 y_l -= 1
#             else:
#                 y_l += 1
#     num = t

# if x == x_l and y == y_l:
#     print("Yes")
# else:
#     print("No")

for _ in range(N):
    t,x,y = map(int,input().split())
    
    dist =  abs(x - x_l) + abs(y - y_l)
    time_diff = t - pre_t
    
    if dist > time_diff or (time_diff - dist) % 2 != 0:
        print("No")
        exit()
        
    pre_t, x_l, y_l = t,x,y

print("Yes")