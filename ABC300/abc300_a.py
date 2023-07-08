N, A, B = map(int, input().split())
C = list(map(int, input().split()))

print(C.index(A+B)+1) # 選択肢番号はindex+1
