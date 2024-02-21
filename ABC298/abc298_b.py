import copy

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

rotA = copy.deepcopy(A)
for i in range(4): # 4回繰り返すと元通りなので
    for j in range(N):
        for k in range(N):
            rotA[j][k] = A[N-1-k][j]

    flag = True # 成り立たなかったらFalse
    for j in range(N):
        for k in range(N):
            if rotA[j][k] == 1 and B[j][k] == 0:
                flag = False
                break
        if flag == False:
            break
    
    if flag:
        print("Yes")
        exit()

    A = copy.deepcopy(rotA) # 次のAは回転したもの，コピーに注意

print("No")
