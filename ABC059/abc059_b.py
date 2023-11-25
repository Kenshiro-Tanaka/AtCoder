A = list(input())
B = list(input())

flag = 0 # A=Bのとき0, A>Bのとき1, A<Bのとき2
if len(A) > len(B):
    flag = 1
elif len(A) < len(B):
    flag = 2
else:
    for i in range(len(A)):
        if int(A[i]) > int(B[i]):
            flag = 1
            break
        elif int(A[i]) < int(B[i]):
            flag = 2
            break
        
print("GREATER" if flag == 1 else "LESS" if flag == 2 else "EQUAL")
