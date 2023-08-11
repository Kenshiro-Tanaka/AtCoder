A, B = map(int, input().split())

for C in range(256): # 0-255だから256までだった
    if A^C == B:
        print(C)
        break

# 別解
# A XOR A = 0 より A XOR C = B の両辺に A XOR をとると C = A XOR B であることから
# print(A^B) だけでいい 
