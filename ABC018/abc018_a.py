A = [int(input()) for i in range(3)]

sA = sorted(A,reverse=True)
print(sA.index(A[0])+1) # A[0]がsAの何番目か
print(sA.index(A[1])+1)
print(sA.index(A[2])+1)
